#from google.appengine.ext import ndb
import datetime
import urlfetch
from jinja_templates import jinja_environment
import json
import logging
import model
from my_encrypting import SECRET, my_decrypt, my_encrypt, my_encode
import os
import random
from sqlalchemy.exc import NoResultFound

server = os.environ['SERVER']

class Source(object):
    @property
    def data(self):
        try:
            logging.info(f"Querying cache for '{self._key}': start")
            stored = model.db.session.execute(model.db.select(model.Cache).filter_by(key=self._key)).scalar_one()
            logging.info("Querying cache: item found")
            self._data = {}
            if stored.json:
                self._data = json.loads(stored.json)
        except NoResultFound:
            logging.info("Querying cache: nothing found")
        return self._data

    @property
    def key(self):
        return self._key

    @property
    def category(self):
        return self._category

    @property
    def jinja_template(self):
        try:
            return self._jinja_template
        except AttributeError:
            self.preload_jinja_template()
            logging.info("Loaded template for rendering card %s because it wasn't preloaded" % self._key)
            return self._jinja_template

    def preload_jinja_template(self):
        self._jinja_template = jinja_environment.from_string(self._template)
        logging.info("Preloaded template for rendering card %s" % self._key)

    def pick(self, cookies, historical, random_in_sequence=False):
        """
         historical contains:
         - the card key
         - for daily and blog cards: the data
         - for sequence and datestamped cards: the item
        """
        try:
            logging.info("Picking card for %s." % (self._key))
            historical_dict = {}
            if historical:
                historical_dict = json.loads(my_decrypt(SECRET, historical))
                try:
                    if historical_dict['key'] != self._key:
                        # just don't print cards that are not requested
                        logging.info("Got historical data not for %s" % self._key)
                        return {}
                except KeyError:
                    logging.error("No key in historical data")
                    item = None
            # load from datastore
            data = self.data
            # for daily and blog cards, there is no item (make it a fallback as well)
            item = None
            # for daily and sequence cards, there is no oldNews (make it a fallback as well)
            oldNews = False
            # default for historical reference
            historical_reference = historical
            if self._type == 'sequence':
                logging.info("Card is sequence")
                # for sequence cards, select an item
                if historical:
                    try:
                        logging.info("Reading historical data")
                        item = historical_dict['item']
                    except KeyError:
                        logging.error("No item in historical data")
                        return {}
                else:
                    try:
                        #logging.info("Fetching first item")
                        #item = data['items'][0]  # take the first by default
                        logging.info("Fetching random item")
                        count = len(data['items'])
                        randomIndex = random.randint(0, count-1)
                        try:
                            item = data['items'][randomIndex]
                        except KeyError:
                            logging.error("Error finding random item")
                            return {}  # this should not happen, unless some card isn't initialized
                    except KeyError:
                        logging.error("No items in sequence")
                        return {}  # this should not happen, unless some card isn't initialized
                    else:
                        if random_in_sequence:
                            pass  # random is already default!
                        elif cookies.get(self._key):
                            url = cookies.get(self._key)  # this is the URL last clicked by the user
                            logging.info("There is a cookie: %s" % url)
                            takeIt = False
                            for i in data['items']:
                                if takeIt:
                                    item = i
                                    logging.info("Selected %s item based on cookie %s: %s" % (self._key, url, i['url']))
                                    break
                                if i['url'] == url:  # this item has been viewed by the user; take the next one
                                    takeIt = True
                            if not takeIt:
                                # this should not happen (or only after sync): the cookie didn't match any item
                                logging.warning("Could not select %s item because cookie %s didn't match any item." % (self._key, url))
                                item = data['items'][0]
                                takeIt = True
                        else:
                            logging.info("No cookies: selected first %s item: %s" % (self._key, item['url']))
                    historical_reference = my_encrypt(SECRET, json.dumps({
                        "key": self._key,
                        "item": item
                    }))
            elif self._type == 'blog':
                logging.info("Card is blog")
                if historical:
                    try:
                        logging.info("Reading historical data")
                        data = historical_dict['data']
                    except KeyError:
                        logging.error("No data in historical data")
                        return {}
                else:
                    if not data:
                        logging.error("No data")
                        return {}
                    # for blog items, check if the item has already been seen
                    if cookies.get(self._key):
                        id = cookies.get(self._key)  # this is the URL (or other identifier) last clicked by the user
                        logging.info("There is a cookie: %s" % id)
                        if id == data['id']:
                            oldNews = True
                            logging.info("Hiding %s item because it's old news: %s" % (self._key, id))
                    historical_reference = my_encrypt(SECRET, json.dumps({
                        "key": self._key,
                        "data": data
                    }))
            elif self._type == 'datestamped':
                logging.info("Card is datestamped")
                if historical:
                    try:
                        logging.info("Reading historical data")
                        item = historical_dict['item']
                    except KeyError:
                        logging.error("No item in historical data")
                        return {}
                else:
                    # for datestamped items, the item has a 'date' element with format dd-mm-yyyy that
                    # has to be matched to today's date
                    today = datetime.date.today().strftime("%d-%m-%Y")
                    for i in data['items']:
                        if i['date'] == today:
                            logging.info("Item for today found")
                            item = i
                            break
                    else:
                        logging.info("No item for today found")
                        return {}
                    historical_reference = my_encrypt(SECRET, json.dumps({
                        "key": self._key,
                        "item": item
                    }))
            elif self._type == 'daily':
                logging.info("Card is daily")
                if historical:
                    try:
                        logging.info("Reading historical data")
                        data = historical_dict['data']
                    except KeyError:
                        logging.error("No data in historical data")
                        return {}
                else:
                    if not data:
                        logging.error("No data")
                        return {}
                    historical_reference = my_encrypt(SECRET, json.dumps({
                        "key": self._key,
                        "data": data
                    }))
            # return the context data
            context = {
                'data': data,
                'item': item,
                'oldNews': oldNews,
                'historical_reference': historical_reference
            }
            logging.info("Picked %s" % context['item'])
            return context
        except KeyError as e:
            logging.error("Nothing picked. Wrong or missing data for %s [KeyError %s]." % (self._key, e))
            return {}

    def html(self, cookies, historical):
        # this is where the cards are rendered
        logging.info("Rendering card html for %s." % (self._key))
        picked = self.pick(cookies, historical)
        # render html
        template = self.jinja_template
        try:
            content = template.render(
                data=picked['data'],
                item=picked['item'],
                oldNews=picked['oldNews'],
                my_encode=lambda x: my_encode(x),
                link_url=server + '/link/' + picked['historical_reference'],
                historical_url=my_encode(server + '/link/' + picked['historical_reference']),
                server=server
            )
        except (KeyError, TypeError) as e:
            logging.error("Rendering template failed for %s [KeyError %s]." % (self._key, e))
            return "<!-- Rendering template failed for %s [KeyError %s]. -->" % (self._key, e)
        else:
            logging.info("Rendered card html")
            return content

    def sync(self):
        try:
            self.harvestSync()
            # harvestSync() is not implemented on all cards
        except AttributeError:
            logging.exception("AttributeError in harvestSync()")
            pass
        except:
            logging.exception("Some error occurred in harvestSync()")
            pass
        else:
            stored = model.Cache()
            stored.key = self._key
            stored = model.db.session.merge(stored)
            stored.json = json.dumps(self._data).encode('utf-8')
            try:
                stored.image = urlfetch.get(self._data[self._blob]).content
            except (KeyError, AttributeError):
                pass
            model.db.session.commit()

    def init(self):
        try:
            self.harvestInit()
            # harvestInit() is not implemented on all cards
        except AttributeError:
            pass
        else:
            stored = model.Cache()
            stored.key = self._key
            stored = model.db.session.merge(stored)
            stored.json = json.dumps(self._data).encode('utf-8')
            model.db.session.commit()


class Card(Source):
    pass

class Radio(Source):
    def html(self, cookies):
        return super(Radio, self).html(cookies, None)

import API_keys
from collection import cards
from datetime import datetime
from datetime import timedelta
from flask import Response
from jinja_templates import jinja_environment
import json
import logging
import model
from my_encrypting import SECRET, my_encrypt, my_encode
import os
import random
import urllib.request, urllib.error, urllib.parse


def randomHandler(request, key=None):
    try:
        logging.info("Rendering random card for %s." % key)
        # find card class for key
        card = cards.find_card(key)
        stored = model.db.session.execute(model.db.select(model.Cache).filter_by(key=key)).scalar_one()
        if stored.json:
            data = json.loads(stored.json)
        oldNews = False
        if card._type == 'sequence':
            count = len(data['items'])
            randomIndex = random.randint(0, count-1)
            try:
                item = data['items'][randomIndex]
            except KeyError:
                logging.fatal("Error finding random item for %s." % key)
                raise
        else:
            logging.fatal("Cannot render random card for %s." % key)
            return
        historical_reference = my_encrypt(SECRET, json.dumps({
            "key": key,
            "item": item
        }))
        template = jinja_environment.from_string(card._template)
        try:
            content = template.render(
                data=data,
                item=item,
                oldNews=oldNews,
                my_encode=lambda x: my_encode(x),
                link_url=os.environ['SERVER'] + '/link/' + historical_reference,
                historical_url=my_encode(os.environ['SERVER'] + '/link/' + historical_reference),
                server=os.environ['SERVER']
            )
        except KeyError as e:
            logging.error("Rendering template failed for %s [KeyError %s]." % (key, e))
            return
        else:
            flask_response = Response(content)
            flask_response.headers['Access-Control-Allow-Origin'] = '*'
            return flask_response
    except KeyError as e:
        logging.error("Wrong or missing data for %s [KeyError %s]." % (key, e))
        return


def randomCardHandler(request, category=None):
    logging.info("Rendering random card for %s." % category)
    # find cards for category
    cards_list = cards.find_cards_per_category(category)
    random.shuffle(cards_list)
    for card in cards_list:
        the_card = card
        picked = the_card.pick(request.cookies, None)
        if picked and not picked['oldNews']:
            template = jinja_environment.from_string(the_card._template)
            try:
                content = template.render(
                    data=picked['data'],
                    item=picked['item'],
                    oldNews=picked['oldNews'],
                    my_encode=lambda x: my_encode(x),
                    link_url=os.environ['SERVER'] + '/link/' + picked['historical_reference'],
                    historical_url=my_encode(os.environ['SERVER'] + '/link/' + picked['historical_reference']),
                    server=os.environ['SERVER']
                )
            except KeyError as e:
                logging.error("Rendering template failed for %s [KeyError %s]." % (category, e))
                continue
            else:
                flask_response = Response(content)
                flask_response.headers['Access-Control-Allow-Origin'] = '*'
                return flask_response
    else:
        logging.error("No card found for %s." % category)
        return


def dailyFeedHandler(request):
    logging.info("Rendering daily feed.")
    current_time = datetime.now()
    today = (datetime.now() - timedelta(hours=6)).strftime("%Y-%m-%d")
    # (a new day starts at 06:00)
    stored = model.db.session.execute(model.db.select(model.DailyFeed).filter_by(key="dailyfeed")).scalar_one()
    if not stored.day == today:
        logging.info("It's a new day for dailyfeed: " + today)
        cards_list = cards.find_cards_per_category(None)
        random.shuffle(cards_list)
        for card in cards_list:
            the_card = card
            if the_card._key in ["koningsoord","radiomariavlaanderen"]:
                continue
            picked = the_card.pick(request.cookies, None, random_in_sequence=True)
            if picked:
                try:
                    stored.url = "https://alledaags.gelovenleren.net/link/" + picked['historical_reference']
                    HCTI_API_ENDPOINT = "https://hcti.io/v1/image"
                    HCTI_API_USER_ID = '168a7c20-2578-4d22-87ac-15aa0e684c2b'
                    data = {'url': stored.url, 'selector': "div.item", 'ms_delay': "1000"}
                    passman = urllib.request.HTTPPasswordMgrWithDefaultRealm()
                    passman.add_password(None, HCTI_API_ENDPOINT, HCTI_API_USER_ID, API_keys.HCTI_API_KEY)
                    authhandler = urllib.request.HTTPBasicAuthHandler(passman)
                    opener = urllib.request.build_opener(authhandler)
                    urllib.request.install_opener(opener)
                    req = urllib.request.Request(url=HCTI_API_ENDPOINT, data=data, method='POST')
                    res = urllib.request.urlopen(HCTI_API_ENDPOINT)
                    json_data = res.read()
                    image_data = json.loads(json_data)
                    stored.image_url = image_data['url']
                    if picked['item']:
                        stored.title = "Alledaags Geloven : " + picked['item']['name'] + " - " + picked['item']['title']
                        stored.description = picked['item']['title']
                    else:
                        stored.title = "Alledaags Geloven : " + picked['data']['name'] + " - " + picked['data']['title']
                        stored.description = picked['data']['title']
                except KeyError as e:
                    logging.error("Picking a card for the daily feed failed for %s [KeyError %s]." % (the_card._key, e))
                    continue
                else:
                    stored.day = today
                    stored.pubDate = current_time.strftime("%a, %d %b %Y %H:%M:%S +0000")
                    model.db.session.commit()
                    break
        else:
            logging.error("No card found for Daily Feed.")
            return
    template = jinja_environment.get_template('dailyfeed.rss')
    content = template.render(
        title=stored.title,
        description=stored.description,
        url=stored.url,
        image=stored.image_url,
        pubDate=stored.pubDate
    )
    flask_response = Response(content)
    flask_response.headers['Cache-Control'] = 'public,max-age=%s' % 900
    flask_response.headers['Content-Type'] = 'text/xml; charset=utf-8'
    return flask_response

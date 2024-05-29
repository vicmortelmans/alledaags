from collection.data import *
from collection.source import Card


class Trente(Card):
    def __init__(self):
        self._key = "trente"
        self._category = "catechism"
        self._type = "sequence"
        self._data = {}
        self._template = """
            <div class="item" id="{{item['key']}}">
                <div class="card catechism">
                    <a target="_blank" href="{{item['url']}}" onclick="document.cookie='{{item['key']}}={{item['url']}}; expires=Fri, 31 Dec 9999 23:59:59 GMT;'">
                        <div class="filled-image">
                            <img src="{{item['image']}}"/>
                        </div>
                        <div class="title">{{data['name']}}</div>
                        <div class="caption">{{item['heading']}}</div>
                        <div class="text">{{item['title']}}</div>
                    </a>
                    <div class="actions">
                        <a target="_blank" href="https://trente.gelovenleren.net/7-kalender/suggesties/">
                            <div class="button">KOMENDE ZONDAG</div>
                        </a>
                    </div>
                    <div class="actions">
                        <a target="_blank" onclick="load_card('{{item['key']}}');">
                            <div class="action-button"></div>
                        </a>
                        {% set url = my_encode(item['url']) %}
                        {% set title = my_encode(data['name'] + ": " + item['title'] + ' via alledaags.gelovenleren.net') %}
                        {% set short_title = my_encode(data['name'] + ": " + item['title']) %}
                        <a target="_blank" href="https://www.facebook.com/sharer/sharer.php?u={{historical_url}}&title={{title}}">
                            <div class="icon"><img src="/static/facebook-box.png"/></div>
                        </a>
                        <a target="_blank" href="https://twitter.com/intent/tweet?url={{historical_url}}&text={{short_title}}">
                            <div class="icon"><img src="/static/twitter-box.png"/></div>
                        </a>
                         <a target="_blank" href="{{link_url}}">
                            <div class="icon"><img src="/static/link.png"/></div>
                        </a>
                   </div>
                </div>
            </div>
        """

    def harvestInit(self):
        data = {
            'name': "Romeinse Catechismus",
            'key': self._key
        }
        items = []
        # load from feed
        try:
            feed = "http://trente.gelovenleren.net/index.xml"
            harvest = getRSS(feed)
            feeditems = harvest['item']
            if not isinstance(feeditems, list): feeditems = [feeditems]
            for feeditem in feeditems:
                if 'deel' in feeditem['link']:
                    url = feeditem['link']
                    xpath = "//article//h2"
                    harvest2 = getHtml(url, xpath)
                    for h2 in harvest2['h2']:
                        item = {}
                        item['name'] = "Romeinse Catechismus"  # this is a required field
                        item['image'] = "/static/saints_in_heaven.jpg"  # this is a required field
                        item['title'] = h2['content'].strip()
                        item['heading'] = feeditem['title']
                        item['url'] = url + h2['a']['href']
                        item['id'] = item['url']
                        item['key'] = self._key
                        items.append(item)
        except (TypeError, KeyError, IndexError) as e:
            title = "Trente: sync error"
            message = "No complete data found on %s (%s)" % (feed, str(e))
            logging.error(title + " : " + message)
            report_error_by_mail(title, message)
            self._data = {}
        # store
        data['items'] = items
        self._data.update(data)

from collection.data import *
from collection.source import Card


class GoudenBoek(Card):
    def __init__(self):
        self._key = "goudenboek"
        self._category = "contemplation"
        self._type = "sequence"
        self._data = {}
        self._template = """
            <div class="item" id="{{item['key']}}">
                <div class="card contemplation">
                    <a target="_blank" href="{{item['url']}}" onclick="document.cookie='{{item['key']}}={{item['url']}}; expires=Fri, 31 Dec 9999 23:59:59 GMT;'">
                        {% if 'image' in item %}
                        <div class="filled-image">
                            <img src="{{item['image']}}"/>
                        </div>
                        {% endif %}
                        <div class="title">{{data['name']}}</div>
                        <div class="text">{{item['title']}}</div>
                    </a>
                    <div class="actions">
                        <a target="_blank" onclick="load_card('{{item['key']}}');">
                            <div class="action-button"></div>
                        </a>
                        {% set url = my_encode(item['url']) %}
                        {% set title = my_encode(data['name'] + ": " + item['title'] + ' via alledaags.gelovenleren.net') %}
                        {% set short_title = my_encode(data['name'] + ": " + item['title']) %}
                        <a target="_blank" href="https://www.facebook.com/sharer/sharer.php?u={{historical_url}}&title={{title}}">
                            <div class="icon"><img src="/var/facebook-box.png"/></div>
                        </a>
                        <a target="_blank" href="https://twitter.com/intent/tweet?url={{historical_url}}&text={{short_title}}">
                            <div class="icon"><img src="/var/twitter-box.png"/></div>
                        </a>
                        {% if 'image' in item %}
                        <a target="_blank" href="https://pinterest.com/pin/create/bookmarklet/?media={{image}}&url={{url}}&is_video=false&description={{title}}">
                            <div class="icon"><img src="/var/pinterest.png"/></div>
                        </a>
                        {% endif %}
                         <a target="_blank" href="{{link_url}}">
                            <div class="icon"><img src="/var/link.png"/></div>
                        </a>
                   </div>
                </div>
            </div>
        """

    def harvestInit(self):
        data = {
            'name': "Volmaakte Godsvrucht",
            'key': self._key
        }
        items = []
        # load from feed
        try:
            feed = "https://gelovenleren.net/categories/gouden-boek/index.xml"
            harvest = getRSS(feed)
            feeditems = harvest['item']
            if not isinstance(feeditems, list): feeditems = [feeditems]
            for feeditem in feeditems:
                item = {}
                item['title'] = feeditem['title']
                item['url'] = feeditem['link']
                item['id'] = item['url']
                item['key'] = self._key
                if 'enclosure' in feeditem:
                    item['image'] = feeditem['enclosure']['url']
                else:
                    item['image'] = "https://alledaags.gelovenleren.net/var/goudenboek.jpg"
                items.append(item)
        except (TypeError, KeyError, IndexError) as e:
            title = "GoudenBoek: sync error"
            message = "No complete data found on %s (%s)" % (feed, str(e))
            logging.error(title + " : " + message)
            report_error_by_mail(title, message)
            self._data = {}
        # store
        items.reverse()
        data['items'] = items
        self._data.update(data)

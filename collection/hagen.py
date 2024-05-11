from collection.data import *
from collection.source import Card


class Hagen(Card):
    def __init__(self):
        self._key = "hagen"
        self._category = "contemplation"
        self._type = "blog"
        self._data = {}
        self._template = """
            {% if data %}
            <div class="item{% if oldNews %} oldNews{% endif %}">
                <div class="card contemplation">
                    <a target="_blank" href="{{data['url']}}" onclick="document.cookie='{{data['key']}}={{data['url']}}; expires=Fri, 31 Dec 9999 23:59:59 GMT;'">
                        <div class="filled-image">
                            <img src="{{data['image']}}"/>
                        </div>
                        <div class="title">{{data['name']}}</div>
                        <div class="text">{{data['title']}}</div>
                    </a>
                    <div class="actions">
                        {% set url = my_encode(data['url']) %}
                        {% set title = my_encode("Hagenpreken: " + data['title'] + ' via alledaags.gelovenleren.net') %}
                        {% set short_title = my_encode("Hagenpreken: " + data['title']) %}
                        <a target="_blank" href="https://www.facebook.com/sharer/sharer.php?u={{historical_url}}&title={{title}}">
                            <div class="icon"><img src="/var/facebook-box.png"/></div>
                        </a>
                        <a target="_blank" href="https://twitter.com/intent/tweet?url={{historical_url}}&text={{short_title}}">
                            <div class="icon"><img src="/var/twitter-box.png"/></div>
                        </a>
                         <a target="_blank" href="{{link_url}}">
                            <div class="icon"><img src="/var/link.png"/></div>
                        </a>
                   </div>
                </div>
            </div>
            {% endif %}
        """

    def harvestSync(self):
        # load from feed
        site = "https://hagenpreken.nl/preken/preek-van-de-week/"
        xpath = "//h2"
        harvest = getHtml(site, xpath)
        data = {
            'name': "Hagenpreken",
            'image': "/var/michel_hagen.jpg",
            'key': self._key
        }
        try:
            data['title'] = harvest['h2']['a']['title']
            data['url'] = harvest['h2']['a']['href']
            data['id'] = data['url']
        except (TypeError, KeyError, IndexError) as e:
            title = "Hagen: sync error"
            message = "No complete data found on %s (%s)" % (site, str(e))
            logging.error(title + " : " + message)
            report_error_by_mail(title, message)
            self._data = {}
        else:
            self._data.update(data)



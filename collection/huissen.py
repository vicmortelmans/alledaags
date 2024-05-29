from collection.data import *
from collection.source import Card

DATE_TIME_FORMAT = '%Y-%m-%d %H:%M:%S'


class Huissen(Card):
    def __init__(self):
        self._key = "huissen"
        self._category = "contemplation"
        self._type = "daily"
        self._data = {}
        self._template = """
            {% if data %}
            <div class="item">
                <div class="card contemplation">
                    <a target="_blank" href="{{data['url']}}" onclick="document.cookie='preken={{data['url']}}; expires=Fri, 31 Dec 9999 23:59:59 GMT;'">
                        <div class="filled-image">
                            <img src="{{data['image']}}"/>
                        </div>
                        <div class="title">{{data['name']}}</div>
                        <div class="text">{{data['title']}}</div>
                    </a>
                    <div class="actions">
                        {% set url = my_encode(data['url']) %}
                        {% set title = my_encode("Preken: " + data['title'] + ' via alledaags.gelovenleren.net') %}
                        {% set short_title = my_encode("Preken Dominicanen Huissen: " + data['title']) %}
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
            {% endif %}
        """

    def harvestSync(self):
        site = "https://huissen.dominicanen.nl/preekteksten.htm"
        xpath = "(//a)[last()]"
        harvest = getHtml(site, xpath)
        data = {
            'name': "Preken van de Dominicaanse gemeenschap Huissen",
            'image': "/static/huissen.png"
        }
        try:
            data['url'] = "https://huissen.dominicanen.nl/" + harvest['a']['href']
            data['title'] = harvest['a']['content']
        except (TypeError, KeyError, IndexError) as e:
            title = "Huissen: sync error"
            message = "No data found on %s (%s)" % (site, str(e))
            logging.error(title + " : " + message)
            report_error_by_mail(title, message)
            self._data = {}
        else:
            self._data.update(data)


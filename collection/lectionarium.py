from collection.data import *
from collection.source import Card
import datetime


class Lectionarium(Card):
    def __init__(self):
        self._key = "lectionarium"
        self._category = "lectionary"
        self._type = "daily"
        self._data = {}
        self._template = """
            <div class="item" id="lectionarium">
                <div class="card lectionary">
                    <a target="_blank" href="{{data['url']}}" onclick="document.cookie='lectionarium={{data['url']}}; expires=Fri, 31 Dec 9999 23:59:59 GMT;'">
                        {% if data['image'] %}
                        <div class="filled-image">
                            <img src="{{data['image']}}"/>
                        </div>
                        {% endif %}
                        <div class="title">{{data['name']}}</div>
                        <div class="text">{{data['title']}}</div>
                    </a>
                    <div class="actions">
                        <a target="_blank" href="{{data['index']}}">
                            <div class="button">INHOUD</div>
                        </a>
                    </div>
                    <div class="actions">
                        {% set url = my_encode(data['url']) %}
                        {% set title = my_encode(data['title'] + ' via alledaags.gelovenleren.net') %}
                        {% set short_title = my_encode(data['title']) %}
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

    def harvestSync(self):
        today = datetime.date.today().strftime("%Y-%m-%d")
        site = "https://lectionarium.gelovenleren.net/" + today + ".html"
        xpath = "//a"
        harvest = getHtml(site, xpath)
        try:
            url2 = "https://lectionarium.gelovenleren.net/" + harvest['a']['href']
            xpath2 = "//h2"
            harvest2 = getHtml(url2, xpath2)
            data = {
                'index': "https://lectionarium.gelovenleren.net/toc.html",
                'name': "Lectionarium van de Tridentijnse Mis",
                'url': url2,
                'image': "https://lectionarium.gelovenleren.net/resources/missaal-eo-cover.png",
                'title': harvest2['h2']['content']
            }
        except (TypeError, KeyError, IndexError) as e:
            title = "Lectionarium van de Tridentijnse Mis: sync error"
            message = "No detailed data found on %s (%s)" % (site, str(e))
            logging.error(title + " : " + message)
            report_error_by_mail(title, message)
            return
        else:
            self._data.update(data)

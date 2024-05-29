from collection.data import *
from collection.source import Card


class Middelbaar(Card):
    def __init__(self):
        self._key = "middelbaar"
        self._category = "catechism"
        self._type = "sequence"
        self._data = {
            'index': "https://mechelse.gelovenleren.net/tafel.html",
        }
        self._template = """
            <div class="item" id="middelbaar">
                <div class="card catechism">
                    <a target="_blank" href="{{item['url']}}" onclick="document.cookie='middelbaar={{item['url']}}; expires=Fri, 31 Dec 9999 23:59:59 GMT;'">
                        {% if item['image'] %}
                        <div class="filled-image">
                            <img src="{{item['image']}}"/>
                        </div>
                        {% endif %}
                        <div class="title">{{item['name']}}</div>
                        <div class="text">{{item['title']}}</div>
                    </a>
                    <div class="actions">
                        <a target="_blank" onclick="load_card('middelbaar');">
                            <div class="action-button"></div>
                        </a>
                        <a target="_blank" href="{{data['index']}}">
                            <div class="button">INHOUD</div>
                        </a>
                    </div>
                    <div class="actions">
                        {% set url = my_encode(item['url']) %}
                        {% set title = my_encode(item['title'] + ' via alledaags.gelovenleren.net') %}
                        {% set short_title = my_encode(item['title']) %}
                        <a target="_blank" href="https://www.facebook.com/sharer/sharer.php?u={{historical_url}}&title={{title}}">
                            <div class="icon"><img src="/static/facebook-box.png"/></div>
                        </a>
                        <a target="_blank" href="https://twitter.com/intent/tweet?url={{historical_url}}&text={{short_title}}">
                            <div class="icon"><img src="/static/twitter-box.png"/></div>
                        </a>
                        <a target="_blank" href="https://pinterest.com/pin/create/bookmarklet/?media={{image}}&url={{url}}&is_video=false&description={{title}}">
                            <div class="icon"><img src="/static/pinterest.png"/></div>
                        </a>
                        <a target="_blank" href="{{link_url}}">
                            <div class="icon"><img src="/static/link.png"/></div>
                        </a>
                    </div>
                </div>
            </div>
        """

    def harvestInit(self):
        site = self._data['index']
        xpath = "//section/p/a"
        harvest = getHtml(site, xpath)
        try:
            items = []
            for theme in harvest['a']:
                les_url = "https://mechelse.gelovenleren.net/" + theme['href']
                les_xpath = "//h1"
                les_harvest = getHtml(les_url, les_xpath)
                for item in les_harvest['h1']:
                    if 'id' in item:
                        items.append({
                            'title': item['content'],
                            'name': "Mechelse Catechismus voor het middelbaar onderwijs",
                            'image': "/static/mc-cover.jpg",
                            'url': les_url + "#" + item['id'],
                        })
        except (TypeError, KeyError, IndexError) as e:
            title = "Middelbaar: init error"
            message = "No data found on %s (%s)" % (site, str(e))
            logging.error(title + " : " + message)
            report_error_by_mail(title, message)
            self._data['items'] = []
        else:
            self._data['items'] = items


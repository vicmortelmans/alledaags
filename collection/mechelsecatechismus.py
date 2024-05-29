from collection.data import *
from collection.source import Card


class MechelseCatechismus(Card):
    def __init__(self):
        self._key = "mechelsecatechismus"
        self._category = "catechism"
        self._type = "sequence"
        self._data = {
            'index': "https://www.hetkatholiekegeloof.nl/catechese/catechismus/"
        }
        self._template = """
            <div class="item" id="mechelsecatechismus">
                <div class="card catechism">
                    <a target="_blank" href="{{item['url']}}" onclick="document.cookie='mechelsecatechismus={{item['url']}}; expires=Fri, 31 Dec 9999 23:59:59 GMT;'">
                        <div class="padded-image">
                            <img src="{{item['image']}}"/>
                        </div>
                        <div class="title">{{item['name']}}</div>
                        <div class="text">{{item['title']}}</div>
                    </a>
                    <div class="actions">
                        <a target="_blank" onclick="load_card('mechelsecatechismus');">
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
                        <a target="_blank" href="{{link_url}}">
                            <div class="icon"><img src="/static/link.png"/></div>
                        </a>
                   </div>
                </div>
            </div>
        """

    def harvestInit(self):
        site = self._data['index']
        xpath = "//td/a"
        harvest = getHtml(site, xpath)
        try:
            self._data['items'] = [
                {
                    'title': a['content'],
                    'name': "Mechelse Catechismus",
                    'url': a['href'] if a['href'].startswith('http') else "https://www.hetkatholiekegeloof.nl" + a['href'],
                    'image': "/static/mechelsecatechismus.png"
                }
                for a in harvest['a']
                if a['content'][:1].isdigit()
            ]
        except (TypeError, KeyError) as e:
            title = "MechelseCatechismus: init error"
            message = "No data found on %s (%s)" % (site, str(e))
            logging.error(title + " : " + message)
            report_error_by_mail(title, message)

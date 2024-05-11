from collection.data import *
from collection.source import Card


class Positief(Card):
    def __init__(self):
        self._key = "positief"
        self._category = "catechism"
        self._type = "sequence"
        self._data = {
            'index': "https://thmore.weebly.com/overzicht.html",
        }
        self._template = """
            <div class="item" id="positief">
                <div class="card catechism">
                    <a target="_blank" href="{{item['url']}}" onclick="document.cookie='positief={{item['url']}}; expires=Fri, 31 Dec 9999 23:59:59 GMT;'">
                        {% if item['image'] %}
                        <div class="filled-image">
                            <img src="{{item['image']}}"/>
                        </div>
                        {% endif %}
                        <div class="title">{{item['name']}}</div>
                        <div class="text">{{item['title']}}</div>
                    </a>
                    <div class="actions">
                        <a target="_blank" onclick="load_card('positief');">
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
        """

    def harvestInit(self):
        site = self._data['index']
        xpath = "//div[@class='paragraph']//a"
        harvest = getHtml(site, xpath)
        try:
            items = []
            for item in harvest['a']:
                if 'font' in item:
                    items.append({
                        'title': item['font']['content'],
                        'name': "Positief",
                        'image': "/var/positief.png",
                        'url': "https://thmore.weebly.com" + item['href']
                        })
        except (TypeError, KeyError, IndexError) as e:
            title = "ABC: init error"
            message = "No data found on %s (%s)" % (site, str(e))
            logging.error(title + " : " + message)
            report_error_by_mail(title, message)
            self._data['items'] = []
        else:
            self._data['items'] = items


from collection.data import *
from collection.source import Card
import os


class ABC(Card):
    def __init__(self):
        self._key = "abc"
        self._category = "catechism"
        self._type = "sequence"
        self._data = {
            'index': "https://www.kuleuven.be/thomas/page/volwassenencatechese-abc/",
        }
        self._template = """
            <div class="item" id="abc">
                <div class="card catechism">
                    <a target="_blank" href="{{item['url']}}" onclick="document.cookie='abc={{item['url']}}; expires=Fri, 31 Dec 9999 23:59:59 GMT;'">
                        {% if item['image'] %}
                        <div class="filled-image">
                            <img src="{{item['image']}}"/>
                        </div>
                        {% endif %}
                        <div class="title">{{item['name']}}</div>
                        <div class="text">{{item['title']}}</div>
                    </a>
                    <div class="actions">
                        <a target="_blank" onclick="load_card('abc');">
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
        site = os.environ['SERVER'] + "/var/abc.html"  # GAE cannot download the index site, gives html timeout
        xpath = "//div[@id='abc']//p/a"
        harvest = getHtml(site, xpath, no_headers=True)
        try:
            items = []
            for item in harvest['a']:
                items.append({
                    'title': item['content'],
                    'name': "ABC van het christelijk geloof",
                    'image': "/var/thomas-godsdienstonderwijs-og.png",
                    'url': item['href'],
                    })
        except (TypeError, KeyError, IndexError) as e:
            title = "ABC: init error"
            message = "No data found on %s (%s)" % (site, str(e))
            logging.error(title + " : " + message)
            report_error_by_mail(title, message)
            self._data['items'] = []
        else:
            self._data['items'] = items


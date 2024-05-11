from collection.data import *
from collection.source import Card


class Adoration(Card):
    def __init__(self):
        self._key = "adoration"
        self._category = "prayer video"
        self._type = "sequence"
        self._data = {
            'index': "https://virtualadoration.home.blog/"
        }
        self._template = """
            <div class="item" id="{{item['key']}}">
                <div class="card prayer video">
                    <a target="_blank" href="{{item['url']}}" onclick="document.cookie='{{item['key']}}={{item['url']}}; expires=Fri, 31 Dec 9999 23:59:59 GMT;'">
                        <div class="filled-image">
                            <img src="{{item['image']}}"/>
                        </div>
                        <div class="title">{{item['name']}}</div>
                        <div class="text">{{item['title']}}</div>
                    </a>
                    <div class="actions">
                        <a target="_blank" onclick="load_card('adoration');">
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
        xpath = "//figure"
        harvest = getHtml(site, xpath)
        self._data['items'] = []
        for item in harvest['figure']:
            try:
                self._data['items'].append({
                        'title': item['figcaption']['a']['content'],
                        'url': item['figcaption']['a']['href'],
                        'name': "Online Aanbidding",
                        'image': item['img']['data-orig-file'],
                        'key': self._key
                })
            except (TypeError, KeyError) as e:
                title = "Adoration: init error"
                message = "No data found on %s (%s)" % (site, str(e))
                logging.error(title + " : " + message)
                report_error_by_mail(title, message)

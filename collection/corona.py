from collection.data import *
from collection.source import Card


class Corona(Card):
    def __init__(self):
        self._key = "corona"
        self._category = "prayer"
        self._type = "sequence"
        self._data = {
            'index': "https://biddenonderweg.org/artikel/bidden-tijdens-de-coronacrisis"
        }
        self._template = """
            <div class="item" id="corona">
                <div class="card prayer">
                    <a target="_blank" href="{{item['url']}}" onclick="document.cookie='corona={{item['url']}}; expires=Fri, 31 Dec 9999 23:59:59 GMT;'">
                        <div class="filled-image">
                            <img src="{{item['image']}}"/>
                        </div>
                        <div class="title">{{item['name']}}</div>
                        <div class="text">{{item['title']}}</div>
                    </a>
                    <div class="actions">
                        <a target="_blank" onclick="load_card('corona');">
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
        xpath = "//a[contains(@href,'speler')]"
        harvest = getHtml(site, xpath)
        try:
            self._data['items'] = [
                {
                    'title': a['content'],
                    'name': "Bidden tijdens de coronacrisis",
                    'url': "https://biddenonderweg.org/" + a['href'],
                    'image': "/var/corona.jpg"
                }
                for a in harvest['a']
            ]
        except (TypeError, KeyError) as e:
            title = "Corona: init error"
            message = "No data found on %s (%s)" % (site, str(e))
            logging.error(title + " : " + message)
            report_error_by_mail(title, message)

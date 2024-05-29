from collection.data import *
from collection.source import Card


class Meesters(Card):
    def __init__(self):
        self._key = "meesters"
        self._category = "prayer"
        self._type = "sequence"
        self._data = {
            'index': "https://leren.kerknet.be/meesters-2/index.html#/"
        }
        self._template = """
            <div class="item" id="meesters">
                <div class="card prayer">
                    <a target="_blank" href="{{item['url']}}" onclick="document.cookie='meesters={{item['url']}}; expires=Fri, 31 Dec 9999 23:59:59 GMT;'">
                        <div class="filled-image">
                            <img src="{{item['image']}}"/>
                        </div>
                        <div class="title">{{item['name']}}</div>
                        <div class="text">{{item['title']}}</div>
                    </a>
                    <div class="actions">
                        <a target="_blank" onclick="load_card('meesters');">
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
        try:
            self._data['items'] = [
                {
                    'title': a['content'],
                    'name': "Naar het hart van je leven",
                    'url': a['href'],
                    'image': "/static/meesters.png"
                }
                for a in [
                    {'content': "Ignatius van Loyola", 'href': "https://leren.kerknet.be/meesters-2/index.html#/lessons/AfebjQ1tS0KJ2NFV3J4mtU8E78I3n7LL"},
                    {'content': "Hildegard van Bingen", 'href': "https://leren.kerknet.be/meesters-2/index.html#/lessons/4RNhYW_vURnvEjRwAJytpcP2_8c3UoxQ"},
                    {'content': "Johannes van het Kruis", 'href': "https://leren.kerknet.be/meesters-2/index.html#/lessons/Bn1Tl0vYfGUJw64yByftRj_eCIP04mcq"},
                    {'content': "Edith Stein", 'href': "https://leren.kerknet.be/meesters-2/index.html#/lessons/bRlE3PqX0OmIP-FFDSY5v89sIjr9GcYO"},
                    {'content': "Benedictus van Nursia", 'href': "https://leren.kerknet.be/meesters-2/index.html#/lessons/Lo3UmsjyjmWCRYwNe2uRxgloG3IJ3x6a"},
                    {'content': "Nicolaas van Cusa", 'href': "https://leren.kerknet.be/meesters-2/index.html#/lessons/kfUzCs1AVfjpaeZi_HRPLZvWFgkSLraF"},
                    {'content': "Extraatje", 'href': "https://leren.kerknet.be/meesters-2/index.html#/lessons/wUPSw-ARtKsv9dMM-FoBT1X-JVyAe5Tt"}
                ]
            ]
        except (TypeError, KeyError) as e:
            title = "Corona: init error"
            logging.error(title)
            report_error_by_mail(title)

from collection.data import *
from collection.source import Card
import os


class DagelijkseVerbinding(Card):
    def __init__(self):
        self._key = "dagelijkseverbinding"
        self._category = "bible video"
        self._type = "sequence"
        self._data = {
            'index': "https://www.youtube.com/playlist?list=PLsTqv8iy6f_1nQPx21yCdmgPxofTNBkaJ"
        }
        self._template = """
            {% if data %}
            <div class="item" id="dagelijkseverbinding">
                <div class="card bible video">
                    <a target="_blank" href="{{item['url']}}" onclick="document.cookie='{{data['key']}}={{item['url']}}; expires=Fri, 31 Dec 9999 23:59:59 GMT;'">
                        <div class="filled-image">
                            <iframe width="304" height="171" src="https://www.youtube.com/embed/{{item['videoid']}}?autoplay=0&amp;rel=0&amp;controls=0&amp;showinfo=0" frameborder="0" allow="encrypted-media" allowfullscreen></iframe>
                        </div>
                        <div class="title">{{item['name']}}</div>
                        <div class="text">{{item['title']}}</div>
                        <div class="caption">{{item['dag']}}</div>
                        <div class="caption">{{item['bibleref']}}</div>
                    </a>
                    <div class="actions">
                        <a target="_blank" href="{{item['lectionarium']}}">
                            <div class="button">LECTIONARIUM</div>
                        </a>
                    </div>
                    <div class="actions">
                        <a target="_blank" onclick="load_card('dagelijkseverbinding');">
                            <div class="action-button"></div>
                        </a>
                        <a target="_blank" href="{{data['index']}}">
                            <div class="button">INHOUD</div>
                        </a>
                    </div>
                    <div class="actions">
                        {% set url = my_encode(item['url']) %}
                        {% set title = my_encode("Dagelijkse Verbinding: " + item['title'] + ' via alledaags.gelovenleren.net') %}
                        {% set short_title = my_encode("Dagelijkse Verbinding: " + item['title']) %}
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

    def harvestInit(self):
        # /!\ the file 'dagelijkse_verbinding.json' in 'collection' is generated from a spreadsheet:
        # https://docs.google.com/spreadsheets/d/17LcW9yPUyFnvZTFflbzhn98fonf3AiLSqpAqRYwAo5Q/edit?usp=sharing
        DATA_FILE = os.path.join(os.path.dirname(__file__), 'dagelijkse_verbinding.json')
        with open(DATA_FILE, 'r') as dataFile:
            structure = json.loads(dataFile.read())
        self._data['items'] = []
        for item_key in structure:
            item = structure[item_key]
            self._data['items'].append({
                'key': self._key,
                'name': "Dagelijkse Verbinding",
                'title': item['titel'],
                'dag': item['dag'],
                'lectionarium': item['lectionarium'],
                'url': item['url'],
                'bibleref': item['bibleref'],
                'videoid': item['videoid'],
                'image': "https://alledaags.gelovenleren.net/var/dagelijkseverbinding.png",
                })

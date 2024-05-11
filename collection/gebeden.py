from collection.data import *
from collection.source import Card
import os
import json


class Gebeden(Card):
    def __init__(self):
        self._key = "gebeden"
        self._category = "prayer"
        self._type = "sequence"
        self._data = {
            'index': "https://gebeden.gelovenleren.net/",  # the trailing / is important for YQL not to choke on a redirect!
        }
        self._template = """
            <div class="item" id="gebeden">
                <div class="card prayer">
                    <a target="_blank" href="{{item['url']}}" onclick="document.cookie='{{item['key']}}={{item['url']}}; expires=Fri, 31 Dec 9999 23:59:59 GMT;'">
                        <div class="filled-image">
                            <img src="{{item['image']}}"/>
                        </div>
                        <div class="title">{{item['name']}}</div>
                        <div class="text">{{item['title']}}</div>
                    </a>
                    <div class="actions">
                        <a target="_blank" onclick="load_card('gebeden');">
                            <div class="action-button"></div>
                        </a>
                        <a target="_blank" href="{{data['index']}}">
                            <div class="button">INHOUD</div>
                        </a>
                    </div>
                    <div class="actions">
                        {% set url = my_encode(item['url']) %}
                        {% set title = my_encode("{{item['name']}}: " + item['title'] + ' via alledaags.gelovenleren.net') %}
                        {% set short_title = my_encode("{{item['name']}}: " + item['title']) %}
                        {% set image = my_encode(item['image']) %}
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
        # /!\ the file 'structure.json' in 'collection' is copied from the project 'gebeden-ionic' and should be kept in sync
        DATA_FILE = os.path.join(os.path.dirname(__file__), 'structure.json')
        with open(DATA_FILE, 'r') as dataFile:
            structure = json.loads(dataFile.read())
        self._data['items'] = []
        for category in structure['categories']:
            for prayer in category['prayers']:
                self._data['items'].append({
                    'key': self._key,
                    'name': "Katholieke Gebeden",
                    'title': prayer['title'],
                    'url': "https://gebeden.gelovenleren.net?" + 'category=' + category['id'] + '&prayer=' + prayer['id'],
                    'image': "https://alledaags.gelovenleren.net/var/03.jpg",
                    })

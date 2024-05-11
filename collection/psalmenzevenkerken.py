from collection.data import *
from collection.source import Card
import os


class PsalmenZevenkerken(Card):
    def __init__(self):
        self._key = "psalmenzevenkerken"
        self._category = "bible video"
        self._type = "sequence"
        self._data = {
            'index': "https://www.bijbelhuiszevenkerken.be/blog/2010/01/01/waken-met-de-psalmen/"
        }
        self._template = """
            {% if data %}
            <div class="item" id="psalmenzevenkerken">
                <div class="card bible video">
                    <a target="_blank" href="{{item['url']}}" onclick="document.cookie='{{data['key']}}={{item['url']}}; expires=Fri, 31 Dec 9999 23:59:59 GMT;'">
                        <div class="filled-image">
                            <iframe width="304" height="171" src="{{item['url']}}?autoplay=0&amp;rel=0&amp;controls=0&amp;showinfo=0" frameborder="0" allow="encrypted-media" allowfullscreen></iframe>
                        </div>
                        <div class="title">{{item['name']}}</div>
                        <div class="text">{{item['title']}}</div>
                    </a>
                    <div class="actions">
                        <a target="_blank" onclick="load_card('psalmenzevenkerken');">
                            <div class="action-button"></div>
                        </a>
                        <a target="_blank" href="{{data['index']}}">
                            <div class="button">INHOUD</div>
                        </a>
                    </div>
                    <div class="actions">
                        {% set url = my_encode(item['url']) %}
                        {% set title = my_encode("Waken met de psalmen: " + item['title'] + ' via alledaags.gelovenleren.net') %}
                        {% set short_title = my_encode("Waken met de psalmen: " + item['title']) %}
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
        # /!\ the file 'psalmen_zevenkerken.json' in 'collection' is generated from a spreadsheet:
        # https://docs.google.com/spreadsheets/d/1mHtoZvfASI6FZ02y_yl1gv4ZssUQVoB7MQ4_QZeA7n8/edit?usp=sharing
        DATA_FILE = os.path.join(os.path.dirname(__file__), 'psalmen_zevenkerken.json')
        with open(DATA_FILE, 'r') as dataFile:
            structure = json.loads(dataFile.read())
        self._data['items'] = []
        for item_key in structure:
            item = structure[item_key]
            self._data['items'].append({
                'key': self._key,
                'name': "Waken met de psalmen",
                'title': item['titel'],
                'url': item['url'],
                'image': "https://alledaags.gelovenleren.net/var/psalmenboek.png",
                })

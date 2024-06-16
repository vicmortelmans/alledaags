from collection.data import *
from collection.source import Card
from slugify import slugify


class MechelseCatechismus2(Card):
    def __init__(self):
        self._key = "mechelsecatechismus2"
        self._category = "catechism"
        self._type = "sequence"
        self._data = {
            'index': "http://catechismus.gelovenleren.net/"
        }
        self._template = """
            <div class="item" id="mechelsecatechismus2">
                <div class="card catechism">
                    <a target="_blank" href="{{item['url']}}" onclick="document.cookie='mechelsecatechismus2={{item['url']}}; expires=Fri, 31 Dec 9999 23:59:59 GMT;'">
                        <div class="padded-image">
                            <img src="{{item['image']}}"/>
                        </div>
                        <div class="title">{{item['name']}}</div>
                        <div class="text">{{item['title']}}</div>
                    </a>
                    <div class="actions">
                        <a target="_blank" onclick="load_card('mechelsecatechismus2');">
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
        leerjaren = [
            "Eerste Leerjaar",
            "Tweede Leerjaar",
            "Derde Leerjaar",
            "Vierde Leerjaar",
            "Vijfde Leerjaar",
            "Zesde Leerjaar",
            "Zevende Leerjaar",
        ]
        self._data['items'] = [
            {
                'title': leerjaar,
                'name': "Mechelse Catechismus voor het basisonderwijs",
                'url': f"https://catechismus.gelovenleren.net/?set={slugify(leerjaar)}",
                'image': "/static/mechelsecatechismus.png"
            }
            for leerjaar in leerjaren
        ]

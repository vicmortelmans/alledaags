from collection.data import *
from collection.source import Card


class Adventskalender(Card):
    def __init__(self):
        self._key = "adventskalender"
        self._category = "prayer"
        self._type = "daily"
        self._data = { }
        self._template = """
            <div class="item">
                <div class="card prayer">
                    <a target="_blank" href="{{data['url']}}">
                        <div class="filled-image">
                            <img src="{{data['image']}}"/>
                        </div>
                        <div class="title">{{data['name']}}</div>
                        <div class="text">{{data['title']}}</div>
                    </a>
                    <div class="actions">
                        {% set url = my_encode(data['url']) %}
                        {% set title = my_encode(data['name'] + ' via alledaags.gelovenleren.net') %}
                        {% set short_title = my_encode(data['name']) %}
                        {% if 'image' in data %}
                        {% set image = my_encode(data['image']) %}
                        {% endif %}
                        <a target="_blank" href="https://www.facebook.com/sharer/sharer.php?u={{historical_url}}&title={{title}}">
                            <div class="icon"><img src="/static/facebook-box.png"/></div>
                        </a>
                        <a target="_blank" href="https://twitter.com/intent/tweet?url={{historical_url}}&text={{short_title}}">
                            <div class="icon"><img src="/static/twitter-box.png"/></div>
                        </a>
                        {% if 'image' in data %}
                        <a target="_blank" href="https://pinterest.com/pin/create/bookmarklet/?media={{image}}&url={{url}}&is_video=false&description={{title}}">
                            <div class="icon"><img src="/static/pinterest.png"/></div>
                        </a>
                        {% endif %}
                         <a target="_blank" href="{{link_url}}">
                            <div class="icon"><img src="/static/link.png"/></div>
                        </a>
                   </div>
                </div>
            </div>
        """

    def harvestInit(self):
        data = {
            'name': "Adventskalender",
            'title': "Kinderen bidden voor kinderen",
            'image': "https://www.rkactiviteiten.nl/kinderenbiddenvoorkinderen/adventskalender/base00.jpg",
            'url': "https://www.rkactiviteiten.nl/kinderenbiddenvoorkinderen/?p=adventskalender"
        }
        self._data.update(data)

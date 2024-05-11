from collection.data import *
from collection.source import Card
import os


class Lourdes(Card):
    def __init__(self):
        self._key = "lourdes"
        self._category = "prayer video"
        self._type = "daily"
        self._data = {}
        self._template = """
            {% if data %}
            <div class="item">
                <div class="card prayer video">
                    <a target="_blank" href="{{data['url']}}">
                        <div class="filled-image">
                            <iframe width="304" height="171" src="{{data['url']}}&amp;autoplay=0&amp;rel=0&amp;controls=0&amp;showinfo=0" frameborder="0" allow="encrypted-media" allowfullscreen></iframe>
                        </div>
                        <div class="title">{{data['name']}}</div>
                        <div class="text">{{data['title']}}</div>
                    </a>
                    <div class="actions">
                        {% set url = my_encode(data['url']) %}
                        {% set title = my_encode("Lourdes: " + data['title'] + ' via alledaags.gelovenleren.net') %}
                        {% set short_title = my_encode("Lourdes: " + data['title']) %}
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
        data = {
            'name': "Lourdes",
            'title': "Livestream",
            'image': os.environ['SERVER'] + "/var/dove1.png",
            'url' : "https://www.youtube.com/embed/live_stream?channel=UC7zlbnNCnuAPiC3goKcFgUg&amp;rel=0"
        }  # title and image are required for the sharing concept to work
        self._data.update(data)



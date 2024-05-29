from collection.data import *
from collection.source import Card
import os
from datetime import datetime
from babel.dates import format_date


class Gebedenboek(Card):
    def __init__(self):
        self._key = "gebedenboek"
        self._category = "prayer"
        self._type = "daily"
        self._data = { }
        self._template = """
            {% if data %}
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
                        {% set title = my_encode("Gebedenboek: " + data['title'] + ' via alledaags.gelovenleren.net') %}
                        {% set short_title = my_encode("Gebedenboek: " + data['title']) %}
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
            {% endif %}
        """

    def harvestSync(self):
        # not working... for some reason all calls from GAE servers are timing out
        # load from web
        site = "https://www.kuleuven.be/thomas/page/gebedenboek/"
        now = datetime.now()
        data = {
            'name': "Thomas Gebedenboek",
            'image': os.environ['SERVER'] + "/static/gebedenboek.jpg",
            'title': format_date(now, format='full', locale='nl'),
            'url': site
        }
        self._data.update(data)



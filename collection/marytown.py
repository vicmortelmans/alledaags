from collection.source import Card
import os


class Marytown(Card):
    def __init__(self):
        self._key = "marytown"
        self._category = "prayer video"
        self._type = "daily"
        self._data = {}
        self._template = """
            {% if data %}
            <div class="item">
                <div class="card prayer video">
                    <a target="_blank" href="{{data['url']}}">
                        <div class="filled-image">
                            <iframe id="ls_embed_1513460540" src="{{data['url']}}" width="304" height="171" frameborder="0" scrolling="no" allowfullscreen> </iframe>
                        </div>
                        <div class="title">{{data['name']}}</div>
                        <div class="text">{{data['title']}}</div>
                    </a>
                    <div class="actions">
                        {% set url = my_encode(data['url']) %}
                        {% set title = my_encode("Marytown: " + data['title'] + ' via alledaags.gelovenleren.net') %}
                        {% set short_title = my_encode("Marytown: " + data['title']) %}
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
            'name': "Marytown",
            'title': "Online aanbidding",
            'image': os.environ['SERVER'] + "/var/marytown-online-adoration-chapel.jpg",
            'url' : "https://livestream.com/accounts/15529184/events/4408765/player?width=640&height=360&enableInfoAndActivity=true&defaultDrawer=&autoPlay=true&mute=true"
        }  # title and image are required for the sharing concept to work
        self._data.update(data)



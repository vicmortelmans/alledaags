from collection.source import Card
import os


class Livemass(Card):
    def __init__(self):
        self._key = "livemass"
        self._category = "prayer video"
        self._type = "daily"
        self._data = {}
        self._template = """
            {% if data %}
            <div class="item">
                <div class="card prayer video">
                    <div class="filled-image" id="livemass-player">
                        <script src="https://content.jwplatform.com/libraries/9KOdgUzC.js"></script>
                        <div id='myElement'>Loading the player...</div>
                        <script type='text/javascript'>
                        jwplayer("myElement").setup({
                            "responsive": true,
                            "width": "100%",
                            "title":"Live",
                            "autostart": true,
                            "sources": [{
                              "file": "https://34.232.8.78:1935/live/live/playlist.m3u8",
                          
                          }]

                        }); 
                        </script>
                    </div>
                    <a target="_blank" href="{{data['url']}}">
                        <div class="title">{{data['name']}}</div>
                        <div class="text">{{data['title']}}</div>
                    </a>
                    <div class="actions">
                        <a target="_blank" href="{{data['url']}}">
                            <div class="button">INHOUD</div>
                        </a>
                    </div>
                    <div class="actions">
                        {% set url = my_encode(data['url']) %}
                        {% set title = my_encode("LiveMass: " + data['title'] + ' via alledaags.gelovenleren.net') %}
                        {% set short_title = my_encode("LiveMass: " + data['title']) %}
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

    def harvestInit(self):
        data = {
            'name': "Livemass",
            'title': "FSSP - Live uitzending van de tridentijnse mis over de ganse wereld",
            'image': os.environ['SERVER'] + "/static/dove1.png",
            'url' : "http://www.livemass.net/"
        }  # title and image are required for the sharing concept to work
        self._data.update(data)



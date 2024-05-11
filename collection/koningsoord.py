from collection.data import *
from collection.source import Card
import os


class Koningsoord(Card):
    def __init__(self):
        self._key = "koningsoord"
        self._category = "prayer mp3"
        self._type = "daily"
        self._data = {}
        self._template = """
            {% if data %}
            <div class="item" id="item-koningsoord">
                <!-- there's a call to add the 'oldnews' class to this card in grid.html
                     only when showing the full grid (so not for historical view) -->
                <div class="card prayer mp3">
                    <a target="_blank" href="{{data['url']}}">
                        <div class="filled-image">
                            <img src="{{data['image']}}"/>
                        </div>
                        <div class="title">{{data['name']}}</div>
                        <div class="text" id="title-koningsoord">{{data['title']}}</div>
                    </a>
                    <div class="actions">
                        <a target="_blank" id="play-{{data['key']}}" onclick="document.cookie='{{data['key']}}={{data['url']}}; expires=fri, 31 dec 9999 23:59:59 gmt;'">
                            <div class="button play-button">BELUISTEREN</div>
                        </a>
                        <script>
                        $(function(){
                            var audio = playRadio('{{data['key']}}', '{{data['mp3']}}', false, 'alledaags');
                            var xpath = "//h1/text()";
                            var url = "https://klanten.connectingmedia.nl/koningsoord/stream-embed.php";
                            var statusurl = "/yql/html?url=$url&xpath=$xpath";
                            statusurl = statusurl.replace("$url", encodeURIComponent(url));
                            statusurl = statusurl.replace("$xpath", encodeURIComponent(xpath));
                            var statusladen = $.getJSON(statusurl);
                            statusladen.done(function(d){
                                var status = d;
                                $('#title-koningsoord').text(status);
                                if (!status.match(/Er zijn geen uitzendingen|Aanvang/)) {
                                    $('#item-koningsoord').show();
                                } else {
                                    $('#item-koningsoord').hide();
                                }
                                $('#container').masonry('layout');
                            });
                        });
                        //@ sourceURL={{data['key']}}.js
                        </script>
                        <div class="status" id="status-{{data['key']}}"></div>
                    </div>
                    <div class="actions">
                        {% set url = my_encode(data['url']) %}
                        {% set title = my_encode("koningsoord: " + data['title'] + ' via alledaags.gelovenleren.net') %}
                        {% set short_title = my_encode("koningsoord: " + data['title']) %}
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
            'name': "Abdij Koningsoord",
            'title': "Live getijden",
            'image': os.environ['SERVER'] + "/var/koningsoord.jpg",
            'image-width': '304',
            'image-height': '152',
            'url': "https://abdijkoningsoord.org/ons-gebed/getijden/",
            'mp3': "https://darkice.mx10.nl:8443/abdijkoningsoord",
            'key': self._key
        }
        self._data.update(data)



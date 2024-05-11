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
                    <link href="https://unpkg.com/video.js/dist/video-js.css" rel="stylesheet">
                    <script src="https://unpkg.com/video.js/dist/video.js"></script>
                    <script src="https://unpkg.com/videojs-contrib-hls/dist/videojs-contrib-hls.js"></script>
                    <div class="filled-image" id="livemass-player">
                        <video id="livemass" class="video-js vjs-fluid vjs-default-skin" controls preload="auto" data-setup='{}'>
                            <source src="http://34.232.8.78:1935/live/live/playlist.m3u8" type="application/x-mpegURL">
                        </video>
                        <script>
                            var player = videojs('livemass');
                            player.play();
                        </script>
                    </div>
                    <a target="_blank" href="{{data['url']}}">
                        <div class="title">{{data['name']}}</div>
                        <div class="text">{{data['title']}}</div>
                        <div class="caption" id="livemass-caption"></div>
                        <script>
                        $(function(){
                            var statusurl = "http://34.232.8.78:1935/live/live/playlist.m3u8";
                            var statusladen = $.get(statusurl);
                            statusladen.fail(function(){
                                $('#livemass-caption').text("Geen uitzending");
                                $('#livemass-player').hide();
                                $('#container').masonry('layout');
                            });
                        });
                        //@ sourceURL={{data['key']}}.js
                        </script>
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
            'name': "Livemass",
            'title': "FSSP - Live uitzending van de tridentijnse mis over de ganse wereld",
            'image': os.environ['SERVER'] + "/var/dove1.png",
            'url' : "http://www.livemass.net/"
        }  # title and image are required for the sharing concept to work
        self._data.update(data)



from collection.data import *
from collection.source import Card


class Navolging(Card):
    def __init__(self):
        self._key = "navolging"
        self._category = "contemplation mp3"
        self._type = "sequence"
        self._data = {
            'index': "https://storage.googleapis.com/geloven-leren/navolging-articles-list-20210824.xml"
        }
        self._template = """
            <div class="item" id="{{item['key']}}">
                <div class="card contemplation mp3">
                    <a target="_blank" href="{{item['url']}}" onclick="document.cookie='{{item['key']}}={{item['url']}}; expires=Fri, 31 Dec 9999 23:59:59 GMT;'">
                        <div class="filled-image">
                            <img src="{{item['image']}}"/>
                        </div>
                        <div class="title">{{item['name']}}</div>
                        <div class="text">{{item['title']}}</div>
                        <div class="caption">{{item['teaser']}}</div>
                    </a>
                    <div class="actions">
                        <a target="_blank" id="play-{{item['key']}}" onclick="document.cookie='{{item['key']}}={{item['url']}}; expires=Fri, 31 Dec 9999 23:59:59 GMT;'">
                            <div class="button play-button">BELUISTEREN</div>
                        </a>
                        <script>
                        $(function(){
                            var audio = playRadio('{{item['key']}}', '{{item['mp3']}}', false, 'alledaags');
                        });
                        //@ sourceURL={{item['key']}}.js
                        </script>
                        <div class="status" id="status-{{item['key']}}"></div>
                    </div>
                    <div class="actions">
                        <a target="_blank" onclick="load_card('navolging');">
                            <div class="action-button"></div>
                        </a>
                        {% set url = my_encode(item['url']) %}
                        {% set title = my_encode(item['title'] + ' via alledaags.gelovenleren.net') %}
                        {% set short_title = my_encode(item['title']) %}
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
        site = self._data['index']
        xpath = "//item"
        harvest = getXml(site, xpath)
        try:
            self._data['items'] = [
                {
                    'title': item['title'],
                    'url': item['link'],
                    'teaser': item['teaser'],
                    'mp3': item['audio'],
                    'name': "De Navolging van Christus",
                    'image': "https://alledaags.gelovenleren.net/var/navolging-cover2.png",
                    'key': self._key
                }
                for item in harvest['item']
            ]
        except (TypeError, KeyError) as e:
            title = "Navolging: init error"
            message = "No complete data found on %s (%s)" % (site, str(e))
            logging.error(title + " : " + message)
            report_error_by_mail(title, message)

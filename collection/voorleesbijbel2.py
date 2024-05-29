from collection.data import *
from collection.source import Card
import os


class VoorleesBijbel(Card):
    def __init__(self):
        self._key = "voorleesbijbel2"
        self._category = "bible mp3"
        self._type = "sequence"
        self._data = {
            'index': "https://storage.googleapis.com/voorleesbijbel-audio/Downloadbijbel-Luisterbijbel-Voorleesbijbel-inhoud%20-%20Blad1.json"
        }
        self._template = """
            <div class="item" id="{{item['key']}}">
                <div class="card bible mp3">
                    <a target="_blank" href="{{item['url']}}" onclick="document.cookie='{{item['key']}}={{item['url']}}; expires=Fri, 31 Dec 9999 23:59:59 GMT;'">
                        <div class="padded-image">
                            <img src="{{item['image']}}"/>
                        </div>
                        <div class="title">{{item['name']}}</div>
                        <div class="text">{{item['title']}}</div>
                        <div class="caption">{{item['book']}}</div>
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
                        <a target="_blank" onclick="load_card('voorleesbijbel2');">
                            <div class="action-button"></div>
                        </a>
                        {% set url = my_encode(item['url']) %}
                        {% set title = my_encode("{{item['name']}}: " + item['title'] + ' via alledaags.gelovenleren.net') %}
                        {% set short_title = my_encode("{{item['name']}}: " + item['title']) %}
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
        site = self._data['index']
        harvest = getJSON(site)
        try:
            self._data['items'] = [
                {
                    'key': self._key,
                    'name': "Voorleesbijbel",
                    'title': item['title'],
                    'book': item['book'],
                    'url': "https://www.debijbel.nl/bijbel/NBV/" + item['bookshort'] + "-" + item['verses'],
                    'mp3': item['mp3'],
                    'image': os.environ['SERVER'] + "/static/logo-nederlands-bijbelgenootschap.png"
                }
                for item in harvest['Blad1']
            ]
        except (TypeError, KeyError, IndexError) as e:
            title = "VoorleesBijbel: init error"
            message = "No complete data found on %s (%s)" % (site, str(e))
            logging.error(title + " : " + message)
            report_error_by_mail(title, message)



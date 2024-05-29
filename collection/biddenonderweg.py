from collection.data import *
from collection.source import Card
from datetime import date, datetime, time, timedelta
from babel.dates import format_date, format_datetime, format_time
import os

DATE_TIME_FORMAT = '%Y-%m-%d %H:%M:%S'


class BiddenOnderweg(Card):
    def __init__(self):
        self._key = "biddenonderweg"
        self._category = "prayer mp3"
        self._type = "daily"
        self._data = {}
        self._template = """
            {% if data %}
            <div class="item">
                <div class="card prayer mp3">
                    <a target="_blank" href="{{data['url']}}">
                        <div class="padded-image">
                            <img src="{{data['image']}}"/>
                        </div>
                        <div class="title">{{data['name']}}</div>
                        <div class="text">{{data['title']}}</div>
                        {% if 'title2' in data and data['title2'] %}
                        <div class="caption">{{data['title2']}}</div>
                        {% endif %}
                    </a>
                    <div class="actions">
                        <a target="_blank" id="play-{{data['key']}}" onclick="document.cookie='{{data['key']}}={{data['url']}}; expires=Fri, 31 Dec 9999 23:59:59 GMT;'">
                            <div class="button play-button">BELUISTEREN</div>
                        </a>
                        <script>
                        $(function(){
                            var audio = playRadio('{{data['key']}}', '{{data['mp3']}}', false, 'alledaags');
                        });
                        //@ sourceURL={{data['key']}}.js
                        </script>
                        <div class="status" id="status-{{data['key']}}"></div>
                    </div>
                    <div class="actions">
                        {% set url = my_encode(data['url']) %}
                        {% set title = my_encode("Bidden Onderweg: " + data['title'] + ' via alledaags.gelovenleren.net') %}
                        {% set short_title = my_encode("Bidden Onderweg: " + data['title']) %}
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
        now = datetime.now()
        site = "https://biddenonderweg.org/speler/%s" % now.strftime("%Y-%m-%d")
        xpath1 = "(//h3)[1]"
        xpath2 = "//audio/source/@src"
        harvest1 = getHtml(site, xpath1)
        harvest2 = getHtml(site, xpath2)
        data = {
            'name': "Bidden Onderweg",
            'image': os.environ['SERVER'] + "/static/biddenonderweg.png",
            'key': self._key
        }
        try:
            if harvest1['h3'] == '':
                now = now + timedelta(days=1)
                xpath1 = "(//h3)[1]"
                site = "https://biddenonderweg.org/speler/%s" % now.strftime("%Y-%m-%d")
                harvest1 = getHtml(site, xpath1)
            data['title2'] = harvest1['h3']
            data['title'] = format_date(now, format='full', locale='nl')
            data['url'] = site
            data['mp3'] = harvest2
        except (TypeError, KeyError, IndexError) as e:
            title = "BiddenOnderweg: sync error"
            message = "No complete data found on %s (%s)" % (site, str(e))
            logging.error(title + " : " + message)
            report_error_by_mail(title, message)
            self._data = {}
        else:
            self._data.update(data)


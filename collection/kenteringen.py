from collection.data import *
from collection.source import Card
import re


class Kenteringen(Card):
    def __init__(self):
        self._key = "kenteringen"
        self._category = "saints"
        self._type = "daily"
        self._data = { }
        self._template = """
            {% if data %}
            <div class="item">
                <div class="card saints">
                    <a target="_blank" href="{{data['url']}}">
                        <div class="filled-image">
                            <img src="{{data['image']}}"/>
                        </div>
                        <div class="title">{{data['name']}}</div>
                        <div class="text">{{data['title']}}</div>
                    </a>
                    <div class="actions">
                        {% set url = my_encode(data['url']) %}
                        {% set title = my_encode("Kenteringen: " + data['title'] + ' via alledaags.gelovenleren.net') %}
                        {% set short_title = my_encode("Kenteringen: " + data['title']) %}
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
        # load from Pinterest RSS feed https://www.pinterest.com/heiligenvandaag/heilige-van-de-dag.rss/
        feed = "https://www.pinterest.com/heiligenvandaag/heilige-van-de-dag.rss/"
        harvest = getRSS(feed)
        data = {
            'name': "Kenteringen",
            'image': "https://i2.wp.com/www.kenteringen.nl/wp-content/uploads/2017/06/Profiel-Heiligenvandaag.jpg?resize=236%2C300&ssl=1",
            'key': self._key
        }
        try:
            item = harvest['item'][0]
            data['title'] = item['title']
            data['url'] = item['link']
            description = item['description']
            url = re.search(r'img src="(https:[^"]+)"', description).group(1)
            data['image'] = url.replace('\\', '')
        except (TypeError, KeyError, IndexError) as e:
            title = "Kenteringen: sync error"
            message = "No complete data found on %s (%s)" % (feed, str(e))
            logging.error(title + " : " + message)
            report_error_by_mail(title, message)
            self._data = {}
        else:
            self._data.update(data)


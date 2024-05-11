from collection.data import *
from collection.source import Card


class KatholiekLeven(Card):
    def __init__(self):
        self._key = "katholiekleven"
        self._category = "contemplation video"
        self._type = "blog"
        self._data = {}
        self._template = """
            {% if data %}
            <div class="item{% if oldNews %} oldNews{% endif %}">
                <div class="card contemplation video">
                    <a target="_blank" href="{{data['url']}}" onclick="document.cookie='{{data['key']}}={{data['url']}}; expires=Fri, 31 Dec 9999 23:59:59 GMT;'">
                        <div class="filled-image">
                            <iframe width="304" height="171" src="https://www.youtube.com/embed/{{data['videoid']}}?autoplay=0&amp;rel=0&amp;controls=0&amp;showinfo=0" frameborder="0" allow="encrypted-media" allowfullscreen></iframe>
                        </div>
                        <div class="title">{{data['name']}}</div>
                        <div class="text">{{data['title']}}</div>
                    </a>
                    <div class="actions">
                        <a target="_blank" href="{{data['channel']}}">
                            <div class="button">HISTORIEK</div>
                        </a>
                    </div>
                    <div class="actions">
                        {% set url = my_encode(data['url']) %}
                        {% set title = my_encode(data['name'] + ": " + data['title'] + ' via alledaags.gelovenleren.net') %}
                        {% set short_title = my_encode(data['name'] + ": " + data['title']) %}
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

    def harvestSync(self):
        # load from feed
        feed = "https://www.youtube.com/feeds/videos.xml?channel_id=UCekKSj_tdihyinEHJHugpSg"
        harvest = getAtom(feed)
        data = {
            'name': "Katholiek Leven",
            'key': self._key
        }
        try:
            item = harvest['entry'][0]
            data['title'] = item['title']
            data['url'] = item['link']['href']
            data['videoid'] = item['videoId']
            data['id'] = data['url']
            data['image'] = item['group']['thumbnail']['url']
            data['channel'] = item['author']['uri']
            data['description'] = item['group']['description']
        except (TypeError, KeyError, IndexError) as e:
            title = "KatholiekLeven: sync error"
            message = "No complete data found on %s (%s)" % (feed, str(e))
            logging.error(title + " : " + message)
            report_error_by_mail(title, message)
            self._data = {}
        else:
            self._data.update(data)



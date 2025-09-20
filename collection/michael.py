from collection.data import *
from collection.source import Card


class Michael(Card):
    def __init__(self):
        self._key = "michael"
        self._category = "contemplation"
        self._type = "blog"
        self._data = {}
        self._template = """
            {% if data %}
            <div class="item{% if oldNews %} oldNews{% endif %}">
                <div class="card contemplation">
                    <a target="_blank" href="{{data['url']}}" onclick="document.cookie='{{data['key']}}={{data['url']}}; expires=Fri, 31 Dec 9999 23:59:59 GMT;'">
                        <div class="filled-image">
                            <img src="{{data['image']}}"/>
                        </div>
                        <div class="title">{{data['name']}}</div>
                        <div class="text">{{data['title']}}</div>
                    </a>
                    <div class="actions">
                        {% set url = my_encode(data['url']) %}
                        {% set title = my_encode(data['name'] + ": " + data['title'] + ' via alledaags.gelovenleren.net') %}
                        {% set short_title = my_encode(data['name'] + ": " + data['title']) %}
                        <a target="_blank" href="https://www.facebook.com/sharer/sharer.php?u={{historical_url}}&title={{title}}">
                            <div class="icon"><img src="/static/facebook-box.png"/></div>
                        </a>
                        <a target="_blank" href="https://twitter.com/intent/tweet?url={{historical_url}}&text={{short_title}}">
                            <div class="icon"><img src="/static/twitter-box.png"/></div>
                        </a>
                        <a target="_blank" href="https://pinterest.com/pin/create/bookmarklet/?media={{image}}&url={{url}}&is_video=false&description={{title}}">
                            <div class="icon"><img src="/static/pinterest.png"/></div>
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
        # load from feed
        feed = "http://www.heilige-michael.nl/?feed=rss2"
        harvest = getRSS(feed, headers=True)
        data = {
            'name': "H. Aartsengel Michael",
            'key': self._key
        }
        try:
            item = harvest['item'][0]
            data['title'] = item['title']
            data['url'] = item['link']
            data['id'] = data['url']
            xpath="//div[contains(@class,'entry-image')]/img"
            harvest = getHtml(data['url'], xpath)
            data['image'] = harvest['img']['src']
        except (TypeError, KeyError, IndexError) as e:
            title = "Michael: sync error"
            message = "No complete data found on %s (%s)" % (feed, str(e))
            logging.error(title + " : " + message)
            report_error_by_mail(title, message)
            self._data = {}
        else:
            self._data.update(data)

from collection.data import *
from collection.source import Card


class DominicanenRadio(Card):
    def __init__(self):
        self._key = "dominicanenradio"
        self._category = "contemplation"
        self._type = "blog"
        self._data = {}
        self._template = """
            {% if data %}
            <div class="item{% if oldNews %} oldNews{% endif %}">
                <div class="card contemplation">
                    <a target="_blank" href="{{data['url']}}">
                        <div class="filled-image">
                            <iframe src="{{data['embed']}}" width="304" height="171" frameborder="0" scrolling="no" allowfullscreen> </iframe>
                        </div>
                        <div class="title">{{data['name']}}</div>
                        <div class="text">{{data['title']}}</div>
                    </a>
                    <div class="actions">
                        {% set url = my_encode(data['url']) %}
                        {% set title = my_encode(data['title'] + ' via alledaags.gelovenleren.net') %}
                        {% set short_title = my_encode(data['title']) %}
                        {% if 'image' in data %}
                        {% set image = my_encode(data['image']) %}
                        {% endif %}
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
        # load from web
        feed = "https://dominicanen.nl/category/inspiratie/radio/feed/"
        data = {
            'name': "Dominicanenradio",
            'image': "/static/dominicanennederland.png",
            'key': self._key
        }
        harvest = getRSS(feed)
        try:
            item = harvest['item'][0]
            data['title'] = item['title']
            data['url'] = item['link']
            data['id'] = item['link']
            data['url'] = item['link']
            site1 = data['url']
            xpath1 = "//iframe/@src"
            harvest1 = getHtml(site1, xpath1)
            if not harvest1:
                return  # some pages don't have embedded soundcloud --- ignoring those
        except (TypeError, KeyError, IndexError) as e:
            title = "DominicanenRadio: sync error"
            message = "No complete data found on %s (%s)" % (feed, str(e))
            logging.error(title + " : " + message)
            report_error_by_mail(title, message)
        else:
            try:
                data['embed'] = harvest1
            except (TypeError, KeyError, IndexError) as e:
                title = "DominicanenRadio: sync error"
                message = "No data found on %s (%s)" % (site1, str(e))
                logging.error(title + " : " + message)
                report_error_by_mail(title, message)
            else:
                self._data.update(data)



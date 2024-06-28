from collection.data import *
from collection.source import Card


class OtheoFranciscus(Card):
    def __init__(self):
        self._key = "otheo_franciscus"
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
                        {% set title = my_encode("Paus Franciscus: " + data['title'] + ' via alledaags.gelovenleren.net') %}
                        {% set short_title = my_encode("Paus Franciscus: " + data['title']) %}
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
        # load from feed
        site = "https://www.otheo.be/auteur/paus-franciscus"
        xpath = "//div[contains(@class,'node__content--article')][.//a[contains(text(),'[catechese]')]]"
        harvest = getHtml(site, xpath, tree_requested=True)
        data = {
            'name': "Paus Franciscus",
            'key': self._key
        }
        try:
            item = harvest[0]
            data['title'] = ''.join(item.find('.//h3').itertext())
            data['url'] = "https://www.otheo.be" + item.find('.//a').get('href')
            data['id'] = data['url']
            data['image'] = "https://www.otheo.be" + item.find('.//noscript/img').get('src')
        except (TypeError, KeyError, IndexError) as e:
            title = "Otheo Franciscus: sync error"
            message = "No complete data found on %s (%s)" % (site, str(e))
            logging.error(title + " : " + message)
            report_error_by_mail(title, message)
            self._data = {}
        else:
            self._data.update(data)



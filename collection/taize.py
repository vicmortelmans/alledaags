from collection.data import *
from collection.source import Card
import os


class Taize(Card):
    def __init__(self):
        self._key = "taize"
        self._category = "prayer"
        self._type = "daily"
        self._data = { }
        self._template = """
            {% if data %}
            <div class="item">
                <div class="card prayer">
                    <a target="_blank" href="{{data['url']}}">
                        <div class="padded-image">
                            <img src="{{data['image']}}"/>
                        </div>
                        <div class="title">{{data['name']}}</div>
                        <div class="text">{{data['title']}}</div>
                    </a>
                    <div class="actions">
                        {% set url = my_encode(data['url']) %}
                        {% set title = my_encode("Taize: " + data['title'] + ' via alledaags.gelovenleren.net') %}
                        {% set short_title = my_encode("Taize: " + data['title']) %}
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
        site = "https://www.taize.fr/nl_article1208.html"
        xpath = "//h3[@class = 'spip']|//select[@name = 'prayers']/option"
        harvest = getHtml(site, xpath)
        data = {
            'name': "Taize",
            'image': os.environ['SERVER'] + "/static/taize-kruis-3.jpg",
        }
        try:
            url = site
            title = harvest['h3']['content']
            for option in harvest['option']:
                if option['content'] == title:
                    url = "https://www.taize.fr/" + option['value']
            data['url'] = url
            data['title'] = title
        except (TypeError, KeyError, IndexError) as e:
            title = "Taize: sync error"
            message = "No data found on %s (%s)" % (site, str(e))
            logging.error(title + " : " + message)
            report_error_by_mail(title, message)
            self._data = {}
        else:
            self._data.update(data)



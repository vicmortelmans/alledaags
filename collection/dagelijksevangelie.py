from collection.data import *
from collection.source import Card
import os


class DagelijksEvangelie(Card):
    def __init__(self):
        self._key = "dagelijksevangelie"
        self._category = "lectionary"
        self._type = "daily"
        self._data = { }
        self._template = """
            {% if data %}
            <div class="item">
                <div class="card lectionary">
                    <a target="_blank" href="{{data['url']}}">
                        <div class="padded-image">
                            <img src="{{data['image']}}"/>
                        </div>
                        <div class="title">{{data['name']}}</div>
                        <div class="text">{{data['title']}}</div>
                        <div class="caption">{{data['quote']}}</div>
                    </a>
                    <div class="actions">
                        {% set url = my_encode(data['url']) %}
                        {% set title = my_encode("Dagelijks Evangelie: " + data['title'] + ' via alledaags.gelovenleren.net') %}
                        {% set short_title = my_encode("Dagelijks Evangelie: " + data['title']) %}
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
        data = {
            'name': "Dagelijks Evangelie",
            'image': os.environ['SERVER'] + "/static/evangelizo.png"
        }
        site = "https://publication.evangelizo.ws/NL/days/%s" % time.strftime("%Y-%m-%d")
        harvest = getJSON(site)
        try:
            data['url'] = "https://dagelijksevangelie.org/NL/gospel/%s" % time.strftime("%Y-%m-%d")
            data['title'] = harvest['data']['liturgic_title']
            data['quote'] = harvest['data']['commentary']['title']
        except (TypeError, KeyError, IndexError) as e:
            title = "DagelijksEvangelie: sync error"
            message = "No data found on %s (%s)" % (site, str(e))
            logging.error(title + " : " + message)
            report_error_by_mail(title, message)
            self._data = {}
        else:
            self._data.update(data)



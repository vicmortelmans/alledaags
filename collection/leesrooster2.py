from collection.data import *
from collection.source import Card
import os


DATE_TIME_FORMAT = '%Y-%m-%d %H:%M:%S'


class Leesrooster2(Card):
    def __init__(self):
        self._key = "leesrooster2"
        self._category = "bible"
        self._type = "daily"
        self._data = {}
        self._template = """
            {% if data %}
            <div class="item">
                <div class="card bible">
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
                        {% set url = my_encode(data['url']) %}
                        {% set title = my_encode("Leesrooster: " + data['title'] + ' via alledaags.gelovenleren.net') %}
                        {% set short_title = my_encode("Leesrooster: " + data['title']) %}
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
        # /!\ this is not working on localhost, with error "Invalid and/or missing SSL certificate for URL"
        site = "https://rkbijbel.nl/cms/webservice.php?mode=bijbelleesrooster"
        harvest = getJSON(site)
        data = {
            'name': "KBS Leesrooster",
            'image': os.environ['SERVER'] + "/var/kbs.png"
        }
        try:
            if harvest['stitel']:
                data['title'] = harvest['stitel'] + ' (' + harvest['sbijbelverwijzing'] + ')'
            else:
                data['title'] = harvest['sbijbelverwijzing']
            data['url'] = "https://rkbijbel.nl"
            data['title2'] = harvest['ddatum']
        except (TypeError, KeyError, IndexError) as e:
            title = "Leesrooster2: sync error"
            message = "No complete data found on %s (%s)" % (site, str(e))
            logging.error(title + " : " + message)
            report_error_by_mail(title, message)
            self._data = {}
        else:
            self._data.update(data)


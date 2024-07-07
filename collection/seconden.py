from collection.data import *
from collection.source import Card
import os
import lxml
import re
import datetime


class Seconden(Card):
    def __init__(self):
        self._key = "seconden"
        self._category = "lectionary"
        self._type = "daily"
        self._data = {}
        self._template = """
            {% if data %}
            <div class="item">
                <div class="card lectionary">
                    <a target="_blank" href="{{data['url']}}">
                        <div class="filled-image">
                            <img src="{{data['image']}}"/>
                        </div>
                        <div class="title">{{data['name']}}</div>
                        <div class="text">{{data['title']}}</div>
                        <div class="caption">{{data['date']}}</div>
                    </a>
                    <div class="actions">
                        {% set url = my_encode(data['url']) %}
                        {% set title = my_encode("Seconden: " + data['title'] + ' via alledaags.gelovenleren.net') %}
                        {% set short_title = my_encode("Seconden: " + data['title']) %}
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
        site = "https://bijbelin1000seconden.be/menu/tiki-index.php"
        xpath = "//p[strong]"
        harvest = getHtml(site, xpath, tree_requested=True)
        data = {
            'name': "Bijbel in 1000 seconden",
            'image': os.environ['SERVER'] + "/static/seconden.png",
        }
        try:
            data['url'] = "https://bijbelin1000seconden.be/menu/" + harvest[0].find('a').get('href')
            data['title'] = ''.join(harvest[0].find('a').itertext())
            data['date'] = harvest[0].find('strong').text
            # now see if we can fetch an image
            site = data['url']
            xpath = "(//div[@id = 'page-data']//img)[1]"
            harvest = getHtml(site, xpath)
            if 'img' in harvest:
                data['image'] = "https://bijbelin1000seconden.be/menu/" + harvest['img']['src']
        except (TypeError, KeyError, IndexError) as e:
            title = "Seconden: sync error"
            message = "No data found on %s (%s)" % (site, str(e))
            logging.error(title + " : " + message)
            report_error_by_mail(title, message)
            self._data = {}
        else:
            self._data.update(data)
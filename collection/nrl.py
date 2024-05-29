from collection.data import *
from collection.source import Card
import datetime
import os
import random

class Nrl(Card):
    def __init__(self):
        self._key = "nrl"
        self._category = "lectionary"
        self._type = "blog"
        self._data = { }
        self._template = """
            {% if data %}
            <div class="item{% if oldNews %} oldNews{% endif %}">
                <div class="card lectionary">
                    <a target="_blank" href="{{data['url']}}" onclick="document.cookie='nrl={{data['url']}}; expires=Fri, 31 Dec 9999 23:59:59 GMT;'">
                        {% if 'image' in data and data['image'] %}
                        <div class="padded-image">
                            <img src="{{data['image']}}"/>
                        </div>
                        {% endif %}
                        <div class="title">{{data['name']}}</div>
                        <div class="text">{{data['title']}}</div>
                        <div class="caption">{{data['date']}}</div>
                    </a>
                    <div class="actions">
                        <a target="_blank" href="{{data['url_bonus_1']}}">
                            <div class="button">{{data['title_bonus_1']}}</div>
                        </a>
                    </div>
                    <div class="actions">
                        <a target="_blank" href="{{data['url_bonus_2']}}">
                            <div class="button">{{data['title_bonus_2']}}</div>
                        </a>
                    </div>
                    <div class="actions">
                        {% set url = my_encode(data['url']) %}
                        {% set title = my_encode("NRL: " + data['title'] + ' via alledaags.gelovenleren.net') %}
                        {% set short_title = my_encode("NRL: " + data['title']) %}
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
        current_date_time = datetime.datetime.now()
        # find a match for date of today or first of next 10 days
        for i in range(10):
            current_date_str = current_date_time.date().strftime("%d/%m/%Y")
            site = "https://rkliturgie.nl/liturgie/liturgische-catechese"
            xpath = "//div[span/span/span[contains(@class, 'date-display-single')][contains(., '%s')]]" % current_date_str
            harvest = getHtml(site, xpath)
            if harvest:
                break
            current_date_time += datetime.timedelta(days=1)
        data = {
            'name': "Liturgische Catechese",
            'index': "https://rkliturgie.nl/liturgie/liturgische-catechese",
            'image': os.environ['SERVER'] + "/static/nrl.png",
        }
        # bonus material from gebeden
        site_bonus_1 = "https://rkliturgie.nl/liturgische-catechese/algemene-of-dagelijkse-gebeden-en-oefeningen"
        xpath_bonus_1 = "//section[@id = 'block-views-children-titels']//a"
        harvest_bonus_1 = getHtml(site_bonus_1, xpath_bonus_1)
        # bonus material from formules
        site_bonus_2 = "https://rkliturgie.nl/liturgische-catechese/formules-van-de-katholieke-leer"
        xpath_bonus_2 = "//section[@id = 'block-views-children-titels']//a"
        harvest_bonus_2 = getHtml(site_bonus_2, xpath_bonus_2)
        try:
            if type(harvest['div']) is list:
                div = random.choice(harvest['div'])
            else:
                div = harvest['div']
            data['title'] = div['span'][1]['span']['a']['content']
            data['url'] = "https://rkliturgie.nl" + div['span'][1]['span']['a']['href']
            data['date'] = current_date_str
            data['id'] = data['url']
            bonus_1 = random.choice(harvest_bonus_1['a'])
            bonus_2 = random.choice(harvest_bonus_2['a'])
            data['title_bonus_1'] = bonus_1['content']
            data['url_bonus_1'] = "https://rkliturgie.nl" + bonus_1['href']
            data['title_bonus_2'] = bonus_2['content']
            data['url_bonus_2'] = "https://rkliturgie.nl" + bonus_2['href']
        except (TypeError, KeyError, IndexError) as e:
            title = "Nrl: sync error"
            message = "No complete data found on %s (%s)" % (site, str(e))
            logging.error(title + " : " + message)
            report_error_by_mail(title, message)
            self._data = {}
        else:
            self._data.update(data)



import API_keys
import datetime
import json
import requests
from collection.data import *
from collection.source import Card


class PopeLeo(Card):
    def __init__(self):
        self._key = "popeleo"
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
                        {% set title = my_encode("Paus Leo XIV: " + data['title'] + ' via alledaags.gelovenleren.net') %}
                        {% set short_title = my_encode("Paus Leo XIV: " + data['title']) %}
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

    def translate(self, english):
        API_KEY = API_keys.YOUTUBE
        url = "https://translation.googleapis.com/language/translate/v2"

        params = {
            "q": english,
            "target": "nl",
            "source": "en",
            "format": "text",
            "key": API_KEY
        }

        response = requests.post(url, data=params)

        if response.status_code == 200:
            result = response.json()
            translated_text = result["data"]["translations"][0]["translatedText"]
            return(translated_text)
        else:
            logging.error(f"translation failed")
            return(english)


    def harvestSync(self):
        # load from feed
        year = datetime.datetime.now().year
        site = f"https://www.vatican.va/content/leo-xiv/en/audiences/{year}.index.html"
        xpath = "(//h1)[2]"
        harvest = getHtml(site, xpath, tree_requested=True)
        data = {
            'name': "Paus Leo XIV",
            'key': self._key
        }
        try:
            item = harvest[0]
            data['title'] = self.translate(''.join(item.find('a').itertext()))
            data['url'] = "https://translate.google.com/translate?js=n&sl=en&tl=nl&u=https://www.vatican.va" + item.find('a').get('href')
            data['id'] = data['url']
            data['image'] = '/static/leo-xiv.jpg'
        except (TypeError, KeyError, IndexError) as e:
            title = "Pope Leo: sync error"
            message = "No complete data found on %s (%s)" % (site, str(e))
            logging.error(title + " : " + message)
            report_error_by_mail(title, message)
            self._data = {}
        else:
            self._data.update(data)
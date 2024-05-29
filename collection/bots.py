from collection.data import *
from collection.source import Card
import os
import re

TAG_RE = re.compile(r'<[^>]+>')



class Bots(Card):
    def __init__(self):
        self._key = "bots"
        self._category = "prayer"
        self._type = "daily"
        self._data = { }
        self._template = """
            {% if data %}
            <div class="item">
                <div class="card prayer mp3">
                    <a target="_blank" href="{{data['url']}}">
                        <div class="filled-image">
                            <img src="{{data['image']}}"/>
                        </div>
                        <div class="title">{{data['name']}}</div>
                        <div class="text">{{data['title']}}</div>
                        <div class="caption">{{data['caption']}}</div>
                        <div class="caption">{{data['preview']}}</div>
                    </a>
                    <div class="actions">
                        {% set url = my_encode(data['url']) %}
                        {% set title = my_encode("Luistert naar Hem: " + data['title'] + ' via alledaags.gelovenleren.net') %}
                        {% set short_title = my_encode("Luistert naar Hem: " + data['title']) %}
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
        date = time.strftime("%Y-%m-%d")
        site = "https://api.luistertnaarhem.nl/?mode=meditatieVoorDatum"
        harvest = getJsonPathPOST(site, json.dumps({"datum": date, "taal": 1, "appVersion": "4"}).encode('ascii'), None, None, headers={"Content-Type": "application/json"})
        # without 'json.dumps' and headers, the code works on development server but not on GAE;
        # here's where this fix was disclosed: https://github.com/eve-val/evelink/issues/203#issuecomment-276102726
        data = {
            'name': "Luistert naar Hem",
            'image': os.environ['SERVER'] + "/static/luistert-naar-hem-bots.png",
            'key': self._key
        }
        try:
            data['url'] = "https://app.luistertnaarhem.nl"
            if harvest['meditatie']:
                data['title'] = harvest['meditatie']['titel']
                data['caption'] = harvest['meditatie']["lezing"]
                if harvest['meditatie']['openingstekst']:
                    data['preview'] = TAG_RE.sub('', harvest['meditatie']["openingstekst"])
                else:
                    data['preview'] = ""
            else:  # harvest['heilige'] assumed
                data['title'] = harvest['heilige']['naam']
                data['caption'] = harvest['heilige']["lezing"]
                if harvest['heilige']['openingstekst']:
                    data['preview'] = TAG_RE.sub('', harvest['heilige']["openingstekst"])
                else:
                    data['preview'] = ""
        except (TypeError, KeyError, IndexError) as e:
            title = "Bots: sync error"
            message = "No data found on %s (%s)" % (site, str(e))
            logging.error(title + " : " + message)
            report_error_by_mail(title, message)
            self._data = {}
        else:
            self._data.update(data)



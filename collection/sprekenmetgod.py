from collection.data import *
from collection.source import Card


class SprekenMetGod(Card):
    def __init__(self):
        self._key = "sprekenmetgod"
        self._category = "contemplation"
        self._type = "daily"
        self._data = {}
        self._template = """
            {% if data %}
            <div class="item">
                <div class="card contemplation">
                    <a target="_blank" href="{{data['url']}}">
                        <div class="filled-image">
                            <img src="{{data['image']}}"/>
                        </div>
                        <div class="title">{{data['name']}}</div>
                        <div class="text">{{data['title']}}</div>
                    </a>
                    <div class="actions">
                        {% set url = my_encode(data['url']) %}
                        {% set title = my_encode("Spreken met God: " + data['title'] + ' via alledaags.gelovenleren.net') %}
                        {% set short_title = my_encode("Spreken met God: " + data['title']) %}
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
        site = "https://deboog-uitgeverij.nl/"
        xpath = "//div[h1[contains(.,'Spreken met God')]]"
        harvest = getHtml(site, xpath)
        data = {
            'name': "Spreken met God",
            'image': "/static/spreken-met-god.jpg"
        }
        try:
            data['title'] = harvest['div']['table']['tr'][1]['td']['a']['content']
            data['url'] = "https://deboog-uitgeverij.nl/" + harvest['div']['table']['tr'][1]['td']['a']['href']
        except (TypeError, KeyError, IndexError) as e:
            title = "SprekenMetGod: sync error"
            message = "No data found on %s (%s)" % (site, str(e))
            logging.error(title + " : " + message)
            report_error_by_mail(title, message)
            self._data = {}
        else:
            self._data.update(data)



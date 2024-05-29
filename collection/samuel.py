from collection.data import *
from collection.source import Card


class Samuel(Card):
    def __init__(self):
        self._key = "samuel"
        self._category = "lectionary"
        self._type = "blog"
        self._data = { }
        self._template = """
            {% if data %}
            <div class="item{% if oldNews %} oldNews{% endif %}">
                <div class="card lectionary">
                    <a target="_blank" href="{{data['url']}}" onclick="document.cookie='{{data['key']}}={{data['url']}}; expires=Fri, 31 Dec 9999 23:59:59 GMT;'">
                        <div class="filled-image">
                            <img src="{{data['image']}}"/>
                        </div>
                        <div class="title">{{data['name']}}</div>
                        <div class="text">{{data['title']}}</div>
                    </a>
                    <div class="actions">
                        <a target="_blank" href="{{data['index']}}">
                            <div class="button">VOLGENDE WEKEN</div>
                        </a>
                    </div>
                    <div class="actions">
                        {% set url = my_encode(data['url']) %}
                        {% set title = my_encode(data['name'] + ": " + data['title'] + ' via alledaags.gelovenleren.net') %}
                        {% set short_title = my_encode(data['name'] + ": " + data['title']) %}
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
        site = "https://www.samueladvies.nl/advies-materiaal/komende-zondagen/"
        xpath = "(//div[contains(@class,'zondag-grid-item')])[1]"
        harvest = getHtml(site, xpath)
        data = {
            'name': "Samuel Advies",
            'index': "https://www.samueladvies.nl/advies-materiaal/komende-zondagen/"
        }
        try:
            data['title'] = harvest['div']['h3']['a']['content']
            data['image'] = harvest['div']['div']['a']['img']['src']
            data['url'] = harvest['div']['h3']['a']['href']
            data['id'] = data['url']
        except (TypeError, KeyError, IndexError) as e:
            title = "Samuel: sync error"
            message = "No complete data found on %s (%s)" % (site, str(e))
            logging.error(title + " : " + message)
            report_error_by_mail(title, message)
            self._data = {}
        else:
            self._data.update(data)



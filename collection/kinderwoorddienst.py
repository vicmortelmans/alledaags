from collection.data import *
from collection.source import Card


class Kinderwoorddienst(Card):
    def __init__(self):
        self._key = "kinderwoorddienst"
        self._category = "lectionary"
        self._type = "daily"
        self._data = { }
        self._template = """
            {% if data %}
            <div class="item">
                <div class="card lectionary">
                    <a target="_blank" href="{{data['url']}}">
                        <div class="filled-image">
                            <img src="{{data['image']}}"/>
                        </div>
                        <div class="title">{{data['name']}}</div>
                        <div class="text">{{data['date']}}</div>
                        <div class="caption">{{data['day']}}</div>
                        <div class="caption">{{data['title']}}</div>
                    </a>
                    <div class="actions">
                        {% set url = my_encode(data['url']) %}
                        {% set title = my_encode("Kinderwoorddienst: " + data['title'] + ' via alledaags.gelovenleren.net') %}
                        {% set short_title = my_encode("Kinderwoorddienst: " + data['title']) %}
                        <a target="_blank" href="https://www.facebook.com/sharer/sharer.php?u={{historical_url}}&title={{title}}">
                            <div class="icon"><img src="/static/facebook-box.png"/></div>
                        </a>
                        <a target="_blank" href="https://twitter.com/intent/tweet?url={{historical_url}}&text={{short_title}}">
                            <div class="icon"><img src="/static/twitter-box.png"/></div>
                        </a>
                        <a target="_blank" href="https://pinterest.com/pin/create/bookmarklet/?media={{image}}&url={{url}}&is_video=false&description={{title}}">
                            <div class="icon"><img src="/static/pinterest.png"/></div>
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
        site = "https://www.kinderwoorddienst.nl"
        xpath = "//div[contains(@class,'item-page')]/div[contains(@class,'thema-container')]"
        harvest = getHtml(site, xpath)
        xpath2 = "(//div[contains(@class,'thema-content')]//img)[1]"
        harvest2 = getHtml(site, xpath2)
        if not harvest2:
            xpath2 = "(//div[contains(@class,'rubriek-row')]//img)[1]"
            harvest2 = getHtml(site, xpath2)
        data = {
            'name': "Kinderwoorddienst"
        }
        try:
            data['url'] = "https://www.kinderwoorddienst.nl" + harvest['div']['div'][2]['ul']['li'][1]['a']['href']
            data['day'] = harvest['div']['h1']['content']
            data['title'] = harvest['div']['div'][0]['h2']['content']
            data['date'] = harvest['div']['div'][1]['h3']['content']
            data['image'] = "https://www.kinderwoorddienst.nl" + harvest2['img']['src']
        except (TypeError, KeyError, IndexError) as e:
            title = "Kinderwoorddienst: sync error"
            message = "No complete data found on %s (%s)" % (site, str(e))
            logging.error(title + " : " + message)
            report_error_by_mail(title, message)
            self._data = {}
        else:
            self._data.update(data)



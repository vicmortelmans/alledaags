from collection.data import *
from collection.source import Card


class MissaleEO(Card):
    def __init__(self):
        self._key = "missaleeo"
        self._category = "lectionary"
        self._type = "blog"
        self._data = {}
        self._template = """
            {% if data %}
            <div class="item{% if oldNews %} oldNews{% endif %}">
                <div class="card lectionary">
                    <a target="_blank" href="{{data['url']}}" onclick="document.cookie='missaleeo={{data['id']}}; expires=Fri, 31 Dec 9999 23:59:59 GMT;'">
                        <div class="filled-image">
                            <img src="{{data['image']}}"/>
                        </div>
                        <div class="title">{{data['name']}}</div>
                        <div class="subtitle">Buitengewone vorm</div>
                        <div class="text">{{data['title']}}</div>
                        <div class="caption">({{data['bibleref']}}) {{' '.join(data['text'].split()[:10])}}...</div>
                    </a>
                    <div class="actions">
                        {% set url = my_encode(data['url']) %}
                        {% set title = my_encode(data['title'] + ' via alledaags.gelovenleren.net') %}
                        {% set short_title = my_encode(data['title']) %}
                        {% set image = my_encode(data['image']) %}
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
        site = "https://www.missale.net/eo/nl"
        xpath = "//article"
        harvest = getHtml(site, xpath)
        xpath = "//h1"
        harvestTitle = getHtml(site, xpath)
        data = {
            'name': "Missale"
        }
        try:
            data['title'] = harvestTitle['h1']['content']
            data['image'] = "https://missale.net" + harvest['article']['div'][0]['img']['src']
            data['id'] = data['image']  # = stored in cookie to check if the item has been read
            data['text'] = harvest['article']['div'][1]['p']
            data['bibleref'] = harvest['article']['div'][1]['div']['content']
            data['url'] = site
        except (TypeError, KeyError, IndexError) as e:
            title = "MissaleEO: sync error"
            message = "No complete data found on %s (%s)" % (site, str(e))
            logging.error(title + " : " + message)
            report_error_by_mail(title, message)
        else:
            self._data.update(data)


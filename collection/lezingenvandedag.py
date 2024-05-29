from collection.data import *
from collection.source import Card


class BeeldMeditatie(Card):
    def __init__(self):
        self._key = "lezingenvandedag"
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
                        {% set title = my_encode("Lezingen van de dag: " + data['title'] + ' via alledaags.gelovenleren.net') %}
                        {% set short_title = my_encode("Lezingen van de dag: " + data['title']) %}
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
        site = "https://bijbelcitaat.be/"
        xpath = "(//a[h2])[2]"
        harvest = getHtml(site, xpath)
        data = {
            'name': "Lezingen van de dag"
        }
        try:
            data['url'] = harvest['a']['href']
            data['date'] = harvest['a']['p']
        except (TypeError, KeyError, IndexError) as e:
            title = "Lezingen van de dag: sync error"
            message = "No data found on %s (%s)" % (site, str(e))
            logging.error(title + " : " + message)
            report_error_by_mail(title, message)
            return
        xpath3 = "//figure//img"
        harvest3 = getHtml(data['url'], xpath3)
        try:
            data['image'] = harvest3['img']['src']
        except (TypeError, KeyError, IndexError) as e:
            title = "Lezingen van de dag: no image found"
            message = "No image found on %s (%s)" % (site, str(e))
            logging.warning(title + " : " + message)
            data['image'] = '/static/lezingvandedag.png'
        xpath4 = "(//h1)[1]"
        harvest4 = getHtml(data['url'], xpath4)
        try:
            data['title'] = harvest4['h1']['content']
        except (TypeError, KeyError, IndexError) as e:
            title = "Lezingen van de dag: sync error"
            message = "No detailed data found on %s (%s)" % (site, str(e))
            logging.error(title + " : " + message)
            report_error_by_mail(title, message)
            return
        else:
            self._data.update(data)




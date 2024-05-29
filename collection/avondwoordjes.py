from collection.data import *
from collection.source import Card


class Avondwoordjes(Card):
    def __init__(self):
        self._key = "avondwoordjes"
        self._category = "contemplation"
        self._type = "daily"
        self._data = {}
        self._template = """
            {% if data %}
            <div class="item">
                <div class="card contemplation {% if 'video' in data %}video{% endif %}">
                    <a target="_blank" href="{{data['url']}}">
                        <div class="filled-image">
                            {% if 'video' in data %}
                            <iframe width="304" height="171" src="{{data['video']}}?autoplay=0&amp;rel=0&amp;controls=0&amp;showinfo=0" frameborder="0" allow="encrypted-media" allowfullscreen></iframe>
                            {% else %}
                            <img src="{{data['image']}}"/>
                            {% endif %}
                        </div>
                        <div class="title">{{data['name']}}</div>
                        <div class="text">{{data['title']}}</div>
                    </a>
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
                        {% if 'video' not in data %}
                        <a target="_blank" href="https://pinterest.com/pin/create/bookmarklet/?media={{image}}&url={{url}}&is_video=false&description={{title}}">
                            <div class="icon"><img src="/static/pinterest.png"/></div>
                        </a>
                        {% endif %}
                        <a target="_blank" href="{{link_url}}">
                            <div class="icon"><img src="/static/link.png"/></div>
                        </a>
                   </div>
                </div>
            </div>
            {% endif %}
        """

    def harvestSync(self):
        self._data = {}
        # load from web
        site = "https://www.jeugddienstdonbosco.be/zingeving/inspiratievooravondwoordjes"
        xpath = "//a[contains(text(), 'Verras me')]"
        harvest = getHtml(site, xpath)
        data = {
            'name': "Avondwoordjes",
            'image': "https://www.bijbelhuiszevenkerken.be/assets/img/logo-liggend.png"
        }
        try:
            data['url'] = "https://www.jeugddienstdonbosco.be" + harvest['a']['href']
        except (TypeError, KeyError, IndexError) as e:
            title = "Avondwoordjes: sync error"
            message = "No data found on %s (%s)" % (site, str(e))
            logging.error(title + " : " + message)
            report_error_by_mail(title, message)
            return
        site = data['url']
        xpath2 = "//h3[contains(@class, 'title')]"
        harvest2 = getHtml(site, xpath2)
        xpath3 = "//div[contains(@class, 'tz-about-image')]/img"
        xpath4 = "//iframe"
        try:
            data["title"] = harvest2['h3']['content']
            harvest4 = getHtml(site, xpath4)
            if 'iframe' in harvest4:
                data["video"] = harvest4['iframe']['src']
            else:
                harvest3 = getHtml(site, xpath3)
                data["image"] = harvest3['img']['src'].split('?')[0]
        except (TypeError, KeyError, IndexError) as e:
            title = "Avondwoordjes: sync error"
            message = "No detailed data found on %s (%s)" % (site, str(e))
            logging.error(title + " : " + message)
            report_error_by_mail(title, message)
        else:
            self._data.update(data)




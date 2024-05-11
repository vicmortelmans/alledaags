from collection.data import *
from collection.source import Card


class Gedichten(Card):
    def __init__(self):
        self._key = "gedichten"
        self._category = "contemplation"
        self._type = "daily"
        self._data = { }
        self._template = """
            {% if data %}
            <div class="item">
                <div class="card contemplation">
                    <a target="_blank" href="{{data['url']}}">
                        <div class="filled-image">
                            <img src="{{data['image']}}"/>
                        </div>
                        <div class="title">{{data['name']}}</div>
                        <div class="caption">{{data['title']}}</div>
                    </a>
                    <div class="actions">
                        {% set url = my_encode(data['url']) %}
                        {% set title = my_encode("Gedichten: " + data['title'] + ' via alledaags.gelovenleren.net') %}
                        {% set short_title = my_encode("Gedichten: " + data['title']) %}
                        <a target="_blank" href="https://www.facebook.com/sharer/sharer.php?u={{historical_url}}&title={{title}}">
                            <div class="icon"><img src="/var/facebook-box.png"/></div>
                        </a>
                        <a target="_blank" href="https://twitter.com/intent/tweet?url={{historical_url}}&text={{short_title}}">
                            <div class="icon"><img src="/var/twitter-box.png"/></div>
                        </a>
                         <a target="_blank" href="{{link_url}}">
                            <div class="icon"><img src="/var/link.png"/></div>
                        </a>
                   </div>
                </div>
            </div>
            {% endif %}
        """

    def harvestSync(self):
        # load from web
        site = "https://www.gedichtensite.nl/"
        xpath = "(//div[contains(@class,'firstarticletitle152')]/a)[1]"
        harvest = getHtml(site, xpath)
        data = {
            'name': "Christelijke gedichten",
            'image': "https://www.gedichtensite.nl/images/headers/IMG_7269.jpeg"
        }
        try:
            data['url'] = "https://www.gedichtensite.nl" + harvest['a']['href']
            data["title"] = harvest['a']['content']
        except (TypeError, KeyError, IndexError) as e:
            title = "Gedichten: sync error"
            message = "No detailed data found on %s (%s)" % (site, str(e))
            logging.error(title + " : " + message)
            report_error_by_mail(title, message)
        else:
            self._data.update(data)



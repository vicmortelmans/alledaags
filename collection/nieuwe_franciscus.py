from collection.data import *
from collection.source import Card


class NieuweFranciscus(Card):
    def __init__(self):
        self._key = "nieuwe-franciscus"
        self._category = "contemplation"
        self._type = "blog"
        self._data = { }
        self._template = """
            {% if data %}
            <div class="item{% if oldNews %} oldNews{% endif %}">
                <div class="card contemplation">
                    <a target="_blank" href="{{data['url']}}" onclick="document.cookie='nieuwe-franciscus={{data['url']}}; expires=Fri, 31 Dec 9999 23:59:59 GMT;'">
                        <div class="filled-image">
                            <img src="{{data['image']}}"/>
                        </div>
                        <div class="title">{{data['name']}}</div>
                        <div class="text">{{data['title']}}</div>
                    </a>
                    <div class="actions">
                        <a target="_blank" href="{{data['index']}}">
                            <div class="button">HISTORIEK</div>
                        </a>
                    </div>
                    <div class="actions">
                        {% set url = my_encode(data['url']) %}
                        {% set title = my_encode("Paus Franciscus: " + data['title'] + ' via alledaags.gelovenleren.net') %}
                        {% set short_title = my_encode("Paus Franciscus: " + data['title']) %}
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
        site = "https://www.kerknet.be/auteur/paus-franciscus"
        xpath_title = "(//div[@class='inner'][contains(.//a/@href,'/blog/')])[1]//h2/text()"
        xpath_image = "(//div[@class='inner'][contains(.//a/@href,'/blog/')])[1]//img/@src"
        xpath_url = "(//div[@class='inner'][contains(.//a/@href,'/blog/')])[1]//a/@href"
        harvest_title = getHtml(site, xpath_title)
        harvest_image = getHtml(site, xpath_image)
        harvest_url = getHtml(site, xpath_url)
        data = {
            'name': "Paus Franciscus",
            'index': "https://www.kerknet.be/auteur/paus-franciscus"
        }
        try:
            data['title'] = harvest_title
            data['image'] = harvest_image
            data['url'] = "https://www.kerknet.be" + harvest_url
            data['id'] = data['url']
        except (TypeError, KeyError, IndexError) as e:
            title = "NieuweFranciscus: sync error"
            message = "No complete data found on %s (%s)" % (site, str(e))
            logging.error(title + " : " + message)
            report_error_by_mail(title, message)
            self._data = {}
        else:
            self._data.update(data)



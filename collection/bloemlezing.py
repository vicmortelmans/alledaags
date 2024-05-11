from collection.data import *
from collection.source import Card


class Bloemlezing(Card):
    def __init__(self):
        self._key = "bloemlezing"
        self._category = "catechism"
        self._type = "sequence"
        self._data = {
            'index': "https://www.kerkvaders.be/bloemlezing",
        }
        self._template = """
            <div class="item" id="bloemlezing">
                <div class="card catechism">
                    <a target="_blank" href="{{item['url']}}" onclick="document.cookie='bloemlezing={{item['url']}}; expires=Fri, 31 Dec 9999 23:59:59 GMT;'">
                        {% if item['image'] %}
                        <div class="filled-image">
                            <img src="{{item['image']}}"/>
                        </div>
                        {% endif %}
                        <div class="title">{{item['name']}}</div>
                        {% if item['part'] %}<div class="caption">{{item['part']}}</div>{% endif %}
                        <div class="text">{{item['title']}}</div>
                    </a>
                    <div class="actions">
                        <a target="_blank" onclick="load_card('bloemlezing');">
                            <div class="action-button"></div>
                        </a>
                        <a target="_blank" href="{{data['index']}}">
                            <div class="button">INHOUD</div>
                        </a>
                    </div>
                    <div class="actions">
                        {% set url = my_encode(item['url']) %}
                        {% set title = my_encode(item['title'] + ' via alledaags.gelovenleren.net') %}
                        {% set short_title = my_encode(item['title']) %}
                        <a target="_blank" href="https://www.facebook.com/sharer/sharer.php?u={{historical_url}}&title={{title}}">
                            <div class="icon"><img src="/var/facebook-box.png"/></div>
                        </a>
                        <a target="_blank" href="https://twitter.com/intent/tweet?url={{historical_url}}&text={{short_title}}">
                            <div class="icon"><img src="/var/twitter-box.png"/></div>
                        </a>
                        <a target="_blank" href="https://pinterest.com/pin/create/bookmarklet/?media={{image}}&url={{url}}&is_video=false&description={{title}}">
                            <div class="icon"><img src="/var/pinterest.png"/></div>
                        </a>
                        <a target="_blank" href="{{link_url}}">
                            <div class="icon"><img src="/var/link.png"/></div>
                        </a>
                    </div>
                </div>
            </div>
        """

    def harvestInit(self):
        site = self._data['index']
        xpath = "//div[@id='content']/ul/li/a"
        harvest = getHtml(site, xpath)
        try:
            items = []
            for theme in harvest['a']:
                theme_url = "https://kerkvaders.be/" + theme['href']
                item_xpath = "//div[@id='content']/ol/li/a"
                item_harvest = getHtml(theme_url, item_xpath)
                img_xpath = "//img[@id='hoofding_foto']"
                img_harvest = getHtml(theme_url, img_xpath)
                if 'a' in item_harvest:
                    for item in item_harvest['a']:
                        items.append({
                            'title': item['content'],
                            'name': "Bloemlezing Kerkvaders",
                            'url': theme_url + item['href'],
                            'image': "https://kerkvaders.be/" + img_harvest['img']['src'],
                            'part': theme['content']
                        })
        except (TypeError, KeyError, IndexError) as e:
            title = "Bloemlezing: init error"
            message = "No data found on %s (%s)" % (site, str(e))
            logging.error(title + " : " + message)
            report_error_by_mail(title, message)
            self._data['items'] = []
        else:
            self._data['items'] = items


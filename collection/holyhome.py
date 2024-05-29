from collection.data import *
from collection.source import Card


class Holyhome(Card):
    def __init__(self):
        self._key = "holyhome"
        self._category = "bible"
        self._type = "sequence"
        self._data = {}
        self._template = """
            <div class="item" id="holyhome">
                <div class="card bible">
                    <a target="_blank" href="{{item['url']}}" onclick="document.cookie='holyhome={{item['url']}}; expires=Fri, 31 Dec 9999 23:59:59 GMT;'">
                        <div class="filled-image">
                            <img src="{{item['image']}}"/>
                        </div>
                        <div class="title">{{item['name']}}</div>
                        <div class="text">{{item['title']}}</div>
                    </a>
                    <div class="actions">
                        <a target="_blank" onclick="load_card('holyhome');">
                            <div class="action-button"></div>
                        </a>
                        <a target="_blank" href="{{item['index']}}">
                            <div class="button">INHOUD</div>
                        </a>
                    </div>
                    <div class="actions">
                        {% set url = my_encode(item['url']) %}
                        {% set title = my_encode("Holy Home: " + item['title'] + ' via alledaags.gelovenleren.net') %}
                        {% set short_title = my_encode("Holy Home: " + item['title']) %}
                        {% set image = my_encode(item['image']) %}
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
        """

    def harvestInit(self):
        self._data['items'] = []
        site1 = "https://www.holyhome.nl/missaal.html"
        xpath1 = "//div[contains(@class,'col1')]//a[contains(@href,'hwc')][not(contains(@href,'154'))]"
        harvest1 = getHtml(site1, xpath1)
        site2 = "https://www.holyhome.nl/lunenburg_start.html"
        xpath2 = "//div[contains(@class,'col1')]//td"
        harvest2 = getHtml(site2, xpath2)
        try:
            for a in harvest1['a']:
                site = a['href']
                xpath1b = "//big[img[contains(@src,'houtsnedes')]]"
                harvest1b = getHtml(site, xpath1b)
                self._data['items'] += [
                    {
                        'name': "Holyhome.nl",
                        'title': a['content'] if a['content'] else a['span']['content'],
                        'image': harvest1b['big']['img']['src'],
                        'url': site,
                        'index': site1
                    }
                ]
            for i, td in enumerate(harvest2['td']):
                if 'a' in td:
                    site = td['a']['href']
                    xpath = "//img[contains(@src,'Prentenboek-big')]"
                    harvest = getHtml(site, xpath)
                    self._data['items'] += [
                        {
                            'name': "Holyhome.nl",
                            'title': harvest2['td'][i+4]['content'],
                            'image': harvest['img']['src'],
                            'url': site,
                            'index': site2
                        }
                    ]
        except (TypeError, KeyError, IndexError) as e:
            title = "Holyhome: init error"
            message = "No data found on %s (%s)" % (site, str(e))
            logging.error(title + " : " + message)
            report_error_by_mail(title, message)

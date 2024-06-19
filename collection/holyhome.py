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
        xpath1 = "//table//a"
        harvest1 = getHtml(site1, xpath1, tree_requested=True)
        site2 = "https://www.holyhome.nl/lunenburg_start.html"
        xpath2 = "//table//a"
        harvest2 = getHtml(site2, xpath2, tree_requested=True)
        try:
            '''
            for a in harvest1:
                site = a.get('href')
                xpath1b = "(//big[img[contains(@src,'houtsnedes')]])[1]"
                harvest1b = getHtml(site, xpath1b)
                if harvest1b:
                    self._data['items'] += [
                        {
                            'name': "Holyhome.nl",
                            'title': ''.join(a.itertext()),
                            'image': harvest1b['big']['img']['src'],
                            'url': site,
                            'index': site1
                        }
                    ]
            '''
            for a in harvest2:
                site = a.get('href')
                if 'bpl' in site:
                    xpath2b = "(//div[contains(@class,'innertube')]/div/div/p/img)[1]"
                    harvest2b = getHtml(site, xpath2b)
                    xpath2c = "//h2[contains(.,'Prentenboek')]"
                    harvest2c = getHtml(site, xpath2c, tree_requested=True)
                    self._data['items'] += [
                        {
                            'name': "Holyhome.nl",
                            'title': harvest2c[0].text,
                            'image': harvest2b['img']['src'],
                            'url': site,
                            'index': site2
                        }
                    ]
        except (TypeError, KeyError, IndexError) as e:
            title = "Holyhome: init error"
            message = "No data found on %s (%s)" % (site1, str(e))
            logging.error(title + " : " + message)
            report_error_by_mail(title, message)

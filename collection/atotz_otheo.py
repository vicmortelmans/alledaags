from collection.data import *
from collection.source import Card


class AtotZ(Card):
    def __init__(self):
        self._key = "atotz_otheo"
        self._category = "catechism"
        self._type = "sequence"
        self._data = {
            'index': "https://www.otheo.be/artikel/bijbel-a-z-bekijk-hele-overzicht"
        }
        self._template = """
            <div class="item" id="atotz_otheo">
                <div class="card catechism">
                    <a target="_blank" href="{{item['url']}}" onclick="document.cookie='atotz_otheo={{item['url']}}; expires=Fri, 31 Dec 9999 23:59:59 GMT;'">
                        <div class="filled-image">
                            <img src="{{item['image']}}"/>
                        </div>
                        <div class="title">{{item['name']}}</div>
                        <div class="text">{{item['title']}}</div>
                    </a>
                    <div class="actions">
                        <a target="_blank" onclick="load_card('atotz_otheo');">
                            <div class="action-button"></div>
                        </a>
                        <a target="_blank" href="{{data['index']}}">
                            <div class="button">INHOUD</div>
                        </a>
                    </div>
                    <div class="actions">
                        {% set url = my_encode(item['url']) %}
                        {% set title = my_encode("Bijbel van A tot Z: " + item['title'] + ' via alledaags.gelovenleren.net') %}
                        {% set short_title = my_encode("Bijbel van A tot Z: " + item['title']) %}
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
        data = {
            'index': "https://www.otheo.be/artikel/bijbel-a-z-bekijk-hele-overzicht"
        }
        site = data['index']
        xpath = "//div[contains(@class,'block__content')]//p"
        harvest = getHtml(site, xpath, tree_requested=True)
        try:
            data['items'] = [
                {
                    'title': p.find('strong').text,
                    'name': "Bijbel van A tot Z",
                    'url': "https://www.otheo.be" + p.find('a').get('href'),
                    'image': "/static/atotz.jpg"
                }
                for p in harvest
            ]
            for item in data['items']:
                try:
                    site = item['url']
                    xpath = "//div[@class='content']//noscript//img" 
                    harvest = getHtml(site, xpath, tree_requested=True)
                    item['image'] = "https://www.otheo.be" + harvest[0].get('src')
                except (TypeError, KeyError, IndexError) as e:
                    title = "Otheo AtotZ: sync error fetching image"
                    message = "No complete data found on %s (%s)" % (site, str(e))
                    logging.error(title + " : " + message)
                    report_error_by_mail(title, message)
        except (TypeError, KeyError, IndexError) as e:
            title = "Otheo AtotZ: sync error"
            message = "No complete data found on %s (%s)" % (site, str(e))
            logging.error(title + " : " + message)
            report_error_by_mail(title, message)
            self._data = {}
        else:
            self._data.update(data)



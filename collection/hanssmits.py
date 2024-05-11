from collection.data import *
from collection.source import Card


class HansSmits(Card):
    def __init__(self):
        self._key = "hanssmits"
        self._category = "contemplation"
        self._type = "sequence"
        self._data = {
            'index': "https://www.hetkatholiekegeloof.nl/sub/-hans-smits-/",
        }
        self._template = """
            <div class="item" id="hanssmits">
                <div class="card contemplation">
                    <a target="_blank" href="{{item['url']}}" onclick="document.cookie='hanssmits={{item['url']}}; expires=Fri, 31 Dec 9999 23:59:59 GMT;'">
                        <div class="filled-image">
                            <img src="{{item['image']}}"/>
                        </div>
                        <div class="title">{{item['name']}}</div>
                        <div class="text">{{item['title']}}</div>
                    </a>
                    <div class="actions">
                        <a target="_blank" onclick="load_card('hanssmits');">
                            <div class="action-button"></div>
                        </a>
                        <a target="_blank" href="{{data['index']}}">
                            <div class="button">INHOUD</div>
                        </a>
                    </div>
                    <div class="actions">
                        {% set url = my_encode(item['url']) %}
                        {% set title = my_encode("Hans Smits: " + item['title'] + ' via alledaags.gelovenleren.net') %}
                        {% set short_title = my_encode("Hans Smits: " + item['title']) %}
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
        xpath = "//tbody//tbody"
        harvest = getHtml(site, xpath)
        try:
            items = []
            for article in harvest['tbody']['tr']:
                time.sleep(1)  # pause to be gentle on the server
                if not 'a' in article['td'][1]:
                    continue
                article_title = article['td'][1]['a']['content']
                article_url = article['td'][1]['a']['href']
                if not "http" in article_url:
                    article_url = "https://www.hetkatholiekegeloof.nl" + article_url
                xpath="//tbody//img"
                harvest = getHtml(article_url, xpath)
                article_image = ""
                if 'img' in harvest:
                    article_image = "https://www.hetkatholiekegeloof.nl" + harvest['img']['src']
                items.append({
                    'title': article_title,
                    'name': "Hans Smits",
                    'url': article_url,
                    'image': article_image,
                    'id': article_url
                })
        except (TypeError, KeyError, IndexError) as e:
            title = "HansSmits: init error"
            message = "No complete data found on %s (%s)" % (site, str(e))
            logging.error(title + " : " + message)
            report_error_by_mail(title, message)
            self._data['items'] = []
        else:
            self._data['items'] = items


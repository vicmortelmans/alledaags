from collection.data import *
from collection.source import Card


class EersteCommunie(Card):
    def __init__(self):
        self._key = "eerstecommunie"
        self._category = "catechism"
        self._type = "sequence"
        self._template = """
            <div class="item" id="eerstecommunie">
                <div class="card catechism">
                    <a target="_blank" href="{{item['url']}}" onclick="document.cookie='eerstecommunie={{item['url']}}; expires=Fri, 31 Dec 9999 23:59:59 GMT;'">
                        <div class="filled-image">
                            <img src="{{item['image']}}"/>
                        </div>
                        <div class="title">{{item['name']}}</div>
                        <div class="text">{{item['title']}}</div>
                    </a>
                    <div class="actions">
                        <a target="_blank" onclick="load_card('eerstecommunie');">
                            <div class="action-button"></div>
                        </a>
                        <a target="_blank" href="{{data['index']}}">
                            <div class="button">INHOUD</div>
                        </a>
                    </div>
                    <div class="actions">
                        {% set url = my_encode(item['url']) %}
                        {% set title = my_encode("Eerste Communie: " + item['title'] + ' via alledaags.gelovenleren.net') %}
                        {% set short_title = my_encode("Eerste Communie: " + item['title']) %}
                        {% set image = my_encode(item['image']) %}
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
        self._data = {
            'index': "https://eerstecommunie.gelovenleren.net"
        }
        site = self._data['index']
        xpath = "//div[contains(@class,'section')]"
        harvest = getHtml(site, xpath)
        self._data['items'] = []
        for div in harvest['div'][1:]:
            try:
                self._data['items'].append({
                    'name': "Eerste Communie",
                    'title': div['div'][0]['div']['div'][0]['h1'] + ': ' + div['div'][0]['div']['div'][0]['h2'],
                    'image': "https://eerstecommunie.gelovenleren.net/" + div['data-background'],
                    'url': "https://eerstecommunie.gelovenleren.net/#" + div['id'][2:].replace('-','')  # remove prefix 'a-' and inner dashes
                })
            except (TypeError, KeyError) as e:
                title = "EersteCommunie: init error"
                message = "Some item without data found on %s (%s)" % (site, str(e))
                logging.error(title + " : " + message)
                report_error_by_mail(title, message)

from collection.data import *
from collection.source import Card
from my_encrypting import my_encode_path_elements


class Youcat(Card):
    def __init__(self):
        self._key = "youcat"
        self._category = "catechism"
        self._type = "sequence"
        self._data = {
            'index': "https://www.hetkatholiekegeloof.nl/catechese/vragen-uit-de-catechismus/",
            'indices': [
                "https://www.hetkatholiekegeloof.nl/catechese/vragen-uit-de-catechismus/",
                "https://www.hetkatholiekegeloof.nl/catechese/vragen-uit-de-catechismus-2/",
                "https://www.hetkatholiekegeloof.nl/catechese/vragen-uit-de-catechismus-3/",
                "https://www.hetkatholiekegeloof.nl/catechese/vragen-uit-de-catechismus-4/"
            ]
        }
        self._template = """
            <div class="item" id="youcat">
                <div class="card catechism">
                    <a target="_blank" href="{{item['url']}}" onclick="document.cookie='youcat={{item['url']}}; expires=Fri, 31 Dec 9999 23:59:59 GMT;'">
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
                        <a target="_blank" onclick="load_card('youcat');">
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
        self._data['items'] = []
        for site in self._data['indices']:
            xpath = "//div/a"
            harvest = getHtml(site, xpath)
            xpath2 = "//h1"
            harvest2 = getHtml(site, xpath2)
            try:
                items = [
                    {
                        'title': a['content'],
                        'name': "YouCat",
                        'url': a['href'] if a['href'].startswith('http') else "https://www.hetkatholiekegeloof.nl/" + a['href'] ,
                        'part': normalize_whitespace(harvest2['h1'])
                    }
                    for a in harvest['a']
                ]
            except (TypeError, KeyError) as e:
                title = "Youcat: init error"
                message = "No data found on %s (%s)" % (site, str(e))
                logging.error(title + " : " + message)
                report_error_by_mail(title, message)
                raise
            else:
                self._data['items'].extend(items)
                time.sleep(1)  # be gently on the host
        for i in self._data['items']:
            site = i['url']
            xpath = "//table//img"
            sleep = 1
            for attempt in range(10):
                harvest = getHtml(site, xpath)
                item = {}
                try:
                    try:
                        item['image'] = "https://www.hetkatholiekegeloof.nl" + my_encode_path_elements(harvest['img']['src'])
                    except (TypeError, KeyError, IndexError):
                        logging.info("No image found on %s." % site)
                except (TypeError, KeyError, IndexError):
                    time.sleep(sleep)
                    logging.warning("Sleeping %d seconds because of error on %s." % (sleep, site))
                    sleep *= 2
                else:
                    i.update(item)
                    time.sleep(1)  # be gently on the host
                    break  # no error caught
            else:
                logging.critical("Retried 10 times reading data.")
                raise Exception("Retried 10 times reading data.") # attempts exhausted


def normalize_whitespace(s):
    return ' '.join(s.split())

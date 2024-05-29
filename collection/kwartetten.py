from collection.data import *
from collection.source import Card


class Kwartetten(Card):
    def __init__(self):
        self._key = "kwartetten"
        self._category = "catechism"
        self._type = "sequence"
        self._data = {
            'index': "https://kwartet.gelovenleren.net/#kwartetten"
        }
        self._template = """
            <div class="item" id="kwartetten">
                <div class="card catechism">
                    <a target="_blank" href="{{item['url']}}" onclick="document.cookie='kwartetten={{item['url']}}; expires=Fri, 31 Dec 9999 23:59:59 GMT;'">
                        <div class="title">{{item['name']}}</div>
                        {% if item['image'] %}
                        <div class="filled-image">
                            <img src="{{item['image']}}"/>
                        </div>
                        {% endif %}
                        {% if item['part'] %}<div class="caption">{{item['part']}}</div>{% endif %}
                        <div class="text">{{item['title']}}</div>
                    </a>
                    <div class="actions">
                        <a target="_blank" onclick="load_card('kwartetten');">
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
        site = self._data['index']
        xpath = "//div[@id='kwartetten']//ul[@data-role='listview']//a"
        harvest = getHtml(site, xpath)
        try:
            kwartetten = [
                {
                    'part': a['content'],
                    'url': "https://kwartet.gelovenleren.net" + a['href']
                }
                for a in harvest['a']
            ]
        except (TypeError, KeyError) as e:
            title = "Kwartetten: init error"
            message = "No data found on %s (%s)" % (site, str(e))
            logging.error(title + " : " + message)
            report_error_by_mail(title, message)
            raise
        self._data['items'] = []
        for kwartet in kwartetten:
            site = kwartet['url']
            xpath = "//area"
            harvest = getHtml(site, xpath)
            try:
                items = [kwartet] + [
                    {
                        'url': "https://kwartet.gelovenleren.net" + area['href'],
                        'part': kwartet['part']
                    }
                    for area in harvest['area']
                ]
            except (TypeError, KeyError) as e:
                title = "Kwartetten: init error"
                message = "No data found on %s (%s)" % (site, str(e))
                logging.error(title + " : " + message)
                report_error_by_mail(title, message)
                raise
            else:
                self._data['items'].extend(items)
                time.sleep(1)  # be gently on the host
        for i in self._data['items']:
            site = i['url']
            xpath = "//h1"
            xpath2 = "//img[@usemap]"
            sleep = 1
            for attempt in range(10):
                harvest = getHtml(site, xpath)
                harvest2 = getHtml(site, xpath2)
                item = {
                    'name': "Katholiek Kwartetten"
                }
                try:
                    try:
                        item['image'] = harvest2['img']['src']
                        item['title'] = harvest['h1'][0]
                    except (TypeError, KeyError, IndexError):
                        logging.info("No image or title found on %s." % site)
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

from collection.data import *
from collection.source import Card
import os
import re


class Compendium(Card):
    def __init__(self):
        self._key = "compendium"
        self._category = "catechism"
        self._type = "sequence"
        self._data = {
            'index': "https://rkdocumenten.nl/rkdocs/index.php?mi=680&nws=2606"
        }
        self._template = """
            <div class="item" id="compendium">
                <div class="card catechism">
                    <a target="_blank" href="{{item['url']}}" onclick="document.cookie='compendium={{item['url']}}; expires=Fri, 31 Dec 9999 23:59:59 GMT;'">
                        <div class="filled-image">
                            <img src="{{item['image']}}"/>
                        </div>
                        <div class="title">{{item['name']}}</div>
                        {% if item['part'] %}<div class="caption">{{item['part']}}</div>{% endif %}
                        {% if item['section'] %}<div class="caption">{{item['section']}}</div>{% endif %}
                        <div class="text">{{item['title']}}</div>
                    </a>
                    <div class="actions">
                        <a target="_blank" onclick="load_card('compendium');">
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
                         <a target="_blank" href="{{link_url}}">
                            <div class="icon"><img src="/static/link.png"/></div>
                        </a>
                   </div>
                </div>
            </div>
        """

    def harvestInit(self):
        site = self._data['index']
        xpath = "//ol/li"
        harvest = getHtml(site, xpath)
        try:
            self._data['items'] = [
                {
                    'title': li['span']['content'],
                    'name': "Compendium",
                    'snippet_url': f"https://rkdocumenten.nl/hans/progs2/services/serv_vraagCodeOpMt.php?codestring={li['span']['span']['content']}&host=rkdcloud&mettekst=&documenttaal=nl&index=alias_alle",
                    'image': os.environ['SERVER'] + "/static/rkdocumenten.png"
                }
                for li in harvest['li']
            ]
        except (TypeError, KeyError) as e:
            title = "Compendium: init error"
            message = "No data found on %s (%s)" % (site, str(e))
            logging.error(title + " : " + message)
            report_error_by_mail(title, message)
        else:
            for i in self._data['items']:
                site = i['snippet_url']
                sleep = 1
                clean = re.compile('<.*?>')
                for attempt in range(10):
                    harvest = getJSON(site)
                    harvest_data = next(iter(harvest.values()))  # there's only one item in harvest, but it has a variable key
                    item = {}
                    try:
                        item['part'] = re.sub(clean, '', harvest_data['alinea'][0])
                        try:
                            item['section'] = re.sub(clean, '', harvest_data['alinea'][1])
                            item['url'] = f"https://rkdocumenten.nl/toondocument/663-compendium-van-de-catechismus-van-de-katholieke-kerk-nl/?systeemnum={harvest_data['alinea_systeemnum']}"
                        except (TypeError, KeyError, IndexError) as e:
                            title = "Compendium: init error"
                            message = "Not all hierarchy tags found on %s (%s)" % (site, str(e))
                            logging.error(title + " : " + message)
                            report_error_by_mail(title, message)
                    except (TypeError, KeyError, IndexError):
                        time.sleep(sleep)
                        logging.warning("Sleeping %d seconds because of error on %s." % (sleep, site))
                        sleep *= 2
                    else:
                        i.update(item)
                        time.sleep(0.1)  # be gently on the host
                        break  # no error caught
                else:
                    logging.critical("Retried 10 times reading data.")
                    raise Exception("Retried 10 times reading data.") # attempts exhausted

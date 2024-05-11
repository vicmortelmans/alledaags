from collection.data import *
from collection.source import Card


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
                        {% if item['chapter'] %}<div class="caption">{{item['chapter']}}</div>{% endif %}
                        {% if item['article'] %}<div class="caption">{{item['article']}}</div>{% endif %}
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
        """

    def harvestInit(self):
        site = self._data['index']
        xpath = "//ol/li"
        harvest = getHtml(site, xpath)
        try:
            self._data['items'] = [
                {
                    'title': li['span']['title'],
                    'name': "Compendium",
                    'url': "https://rkdocumenten.nl/rkdocs/" + li['span']['a']['href'],
                    'image': "https://alledaags.gelovenleren.net/var/rkdocumenten.png"
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
                site = i['url']
                xpath = "//table[@class='document_kruimelpad']//tr//td[position()=2 or position()=4]"
                sleep = 1
                for attempt in range(10):
                    harvest = getHtml(site, xpath)
                    item = {}
                    try:
                        item['part'] = harvest['td'][0]['nobr']['a']['content'] + ' ' + harvest['td'][1]['a']['strong']
                        try:
                            item['section'] = harvest['td'][2]['nobr']['a']['content'] + ' ' + harvest['td'][3]['a']['content']
                            item['chapter'] = harvest['td'][4]['nobr']['a']['content'] + ' ' + harvest['td'][5]['a']['strong']
                            item['article'] = harvest['td'][6]['nobr']['a']['content'] + ' ' + harvest['td'][7]['a']['i']
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
                        time.sleep(1)  # be gently on the host
                        break  # no error caught
                else:
                    logging.critical("Retried 10 times reading data.")
                    raise Exception("Retried 10 times reading data.") # attempts exhausted

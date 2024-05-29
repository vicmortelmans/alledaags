from collection.data import *
from collection.source import Card
import os


class BeeldMeditatie(Card):
    def __init__(self):
        self._key = "beeldmeditatie"
        self._category = "contemplation"
        self._type = "daily"
        self._blob = "original_image"  # see data.py for code that stores the image in the datastore
        self._data = {}
        self._template = """
            {% if data %}
            <div class="item">
                <div class="card contemplation">
                    <a target="_blank" href="{{data['url']}}">
                        <div class="filled-image">
                            <img src="{{data['image']}}"/>
                        </div>
                        <div class="title">{{data['name']}}</div>
                        <div class="text">{{data['title']}}</div>
                    </a>
                    <div class="actions">
                        {% set url = my_encode(data['url']) %}
                        {% set title = my_encode("Beeldmeditatie: " + data['title'] + ' via alledaags.gelovenleren.net') %}
                        {% set short_title = my_encode("Beeldmeditatie: " + data['title']) %}
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
            {% endif %}
        """

    def harvestSync(self):
        # load from web
        site = "https://www.beeldmeditaties.nl/m_dag.php?YMD=%s" % time.strftime("%y%m%d")
        xpath = "(//a[img/@class='afbLi'])[1]"
        harvest = getHtml(site, xpath)
        data = {
            'name': "Beeldmeditatie"
        }
        try:
            data['url'] = "https://www.beeldmeditaties.nl/" + harvest['a']['href']
            data['title'] = harvest['a']['content']
        except (TypeError, KeyError, IndexError) as e:
            title = "BeeldMeditatie: sync error"
            message = "No complete data found on %s (%s)" % (site, str(e))
            logging.error(title + " : " + message)
            report_error_by_mail(title, message)
            return
        if data['title'].find('willekeurige') > 0:
            # if there's no meditation for this date, don't show a card
            return
        site = data['url']
        xpath = "(//div[@id='inhoud']//img)[1]"
        harvest = getHtml(site, xpath)
        try:
            data['original_image'] = "https://www.beeldmeditaties.nl/" + harvest['img']['src']
            data['image'] = os.environ['SERVER'] + "/image/beeldmeditatie"
        except (TypeError, KeyError, IndexError) as e:
            title = "BeeldMeditatie: sync error"
            message = "No image found on %s (%s)" % (site, str(e))
            logging.error(title + " : " + message)
            report_error_by_mail(title, message)
        else:
            self._data.update(data)

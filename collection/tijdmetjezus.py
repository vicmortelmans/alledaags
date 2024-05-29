from collection.data import *
from collection.source import Card
import os


class TijdMetJezus(Card):
    def __init__(self):
        self._key = "tijdmetjezus"
        self._category = "contemplation"
        self._type = "daily"
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
                        <div class="caption">{{data['passage']}}</div>
                    </a>
                </div>
            </div>
            {% endif %}
        """

    def harvestSync(self):
        # load from web
        site = "https://www.tijdmetjezus.nl/"
        xpath = "//div[@class='bijbelvindplaats']|//div[@class='bijbeltekst']"
        harvest = getHtml(site, xpath)
        data = {
            'name': "Tijd met Jezus",
            'image': os.environ['SERVER'] + "/static/tijd-met-jezus.png"
        }
        try:
            data['title'] = get_only_content_from_element(harvest['div'][1])
            data['passage'] = harvest['div'][0]['content']
            data['url'] = site
        except (TypeError, KeyError, IndexError) as e:
            title = "TijdMetJezus: sync error"
            message = "No data found on %s (%s)" % (site, str(e))
            logging.error(title + " : " + message)
            report_error_by_mail(title, message)
            self._data = {}
        else:
            self._data.update(data)



from collection.data import *
from collection.source import Card
import os

class DagelijksGebed(Card):
    def __init__(self):
        self._key = "dagelijksgebed"
        self._category = "prayer"
        self._type = "daily"
        self._data = { }
        self._template = """
            {% if data %}
            <div class="item">
                <div class="card prayer">
                    <a target="_blank" href="{{data['url']}}">
                        <div class="padded-image">
                            <img src="{{data['image']}}"/>
                        </div>
                        <div class="title">{{data['name']}}</div>
                        <div class="text">{{data['title']}}</div>
                    </a>
                </div>
            </div>
            {% endif %}
        """

    def harvestSync(self):
        # load from web
        site = "https://sacredspace.com/nl/daily-prayer/%s/" % time.strftime("%Y-%m-%d")
        xpath = "//div[contains(@class,'presence-header')]"
        harvest = getHtml(site, xpath, no_headers=False, tree_requested=True)
        data = {
            'name': "Dagelijks Gebed",
            'image': os.environ['SERVER'] + "/static/dagelijksgebed.png"
        }
        try:
            data['title'] = ''.join(harvest[0].find('p').itertext()).strip()
            data['url'] = site
        except (TypeError, KeyError, IndexError) as e:
            title = "DagelijksGebed: sync error"
            message = "No data found on %s (%s)" % (site, str(e))
            logging.error(title + " : " + message)
            report_error_by_mail(title, message)
            self._data = {}
        else:
            self._data.update(data)



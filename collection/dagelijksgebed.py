from collection.data import *
from collection.source import Card


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
        site = "https://www.gewijderuimte.org/daily-prayer/%s" % time.strftime("%Y-%m-%d")
        xpath = "//a[contains(@class,'active')]"
        harvest = getHtml(site, xpath, no_headers=True)
        data = {
            'name': "Dagelijks Gebed",
            'image': "https://www.sacredspace.ie/profiles/annerprofile/themes/sacredspacetheme/images/icon/logo.png"
        }
        try:
            data['title'] = harvest['a']['content']
            data['url'] = site
        except (TypeError, KeyError, IndexError) as e:
            title = "DagelijksGebed: sync error"
            message = "No data found on %s (%s)" % (site, str(e))
            logging.error(title + " : " + message)
            report_error_by_mail(title, message)
            self._data = {}
        else:
            self._data.update(data)



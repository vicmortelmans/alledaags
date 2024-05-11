from collection.data import *
from collection.source import Card


class InnerlijkLeven(Card):
    def __init__(self):
        self._key = "innerlijkleven"
        self._category = "contemplation"
        self._type = "daily"
        self._data = { }
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
                        <div class="caption">{{data['text']}}</div>
                    </a>
                    <div class="actions">
                        {% set url = my_encode(data['url']) %}
                        {% set title = my_encode("Innerlijk Leven: " + data['title'] + ' via alledaags.gelovenleren.net') %}
                        {% set short_title = my_encode("Innerlijk Leven: " + data['title']) %}
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
            {% endif %}
        """

    def harvestSync(self):
        # load from web
        site = "https://storage.googleapis.com/geloven-leren/calendar-alledaags-geloven-20210824.xml"
        xpath = "//day[date='%s']" % time.strftime("%Y-%m-%d")
        harvest = getXml(site, xpath)
        data = {
            'name': "Innerlijk Leven",
        }
        try:
            data['url'] = harvest['day']['url']
            data['title'] = harvest['day']['title']
            data['text'] = harvest['day']['text']
            data['image'] = harvest['day']['image']
        except (TypeError, KeyError, IndexError) as e:
            title = "InnerlijkLeven: sync error"
            message = "No data found on %s (%s)" % (site, str(e))
            logging.error(title + " : " + message)
            report_error_by_mail(title, message)
            self._data = {}
        else:
            self._data.update(data)



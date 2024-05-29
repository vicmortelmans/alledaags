from collection.data import *
from collection.source import Card


class Summa(Card):
    def __init__(self):
        self._key = "summa"
        self._category = "catechism"
        self._type = "sequence"
        self._data = {
            'index': "https://summa.gelovenleren.net/index.xml"
        }
        self._template = """
            <div class="item" id="{{item['key']}}">
                <div class="card catechism">
                    <a target="_blank" href="{{item['url']}}" onclick="document.cookie='{{item['key']}}={{item['url']}}; expires=Fri, 31 Dec 9999 23:59:59 GMT;'">
                        <div class="padded-image" id="summa-illustration">
                            <script src="https://summa.gelovenleren.net/scripts/shapes.js"></script>
                            <script>
                                var element = document.createElement("link");
                                element.setAttribute("rel", "stylesheet");
                                element.setAttribute("type", "text/css");
                                element.setAttribute("href", "https://summa.gelovenleren.net/styles/shapes.css");
                                document.getElementsByTagName("head")[0].appendChild(element);
                                document.getElementById("summa-illustration").innerHTML = newShape();
                            </script>
                            <!--img src="{{item['image']}}"/-->
                        </div>
                        <div class="title">{{item['name']}}</div>
                        <div class="text">{{item['title']}}</div>
                    </a>
                    <div class="actions">
                        <a target="_blank" onclick="load_card('summa');">
                            <div class="action-button"></div>
                        </a>
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
        xpath = "//articulus"
        harvest = getXml(site, xpath)
        try:
            self._data['items'] = [
                {
                    'title': item['title'],
                    'url': item['url'],
                    'name': "Summa Theologiae",
                    'image': item['image'],
                    'key': self._key
                }
                for item in harvest['articulus']
            ]
        except (TypeError, KeyError) as e:
            title = "Summa: init error"
            message = "No data found on %s (%s)" % (site, str(e))
            logging.error(title + " : " + message)
            report_error_by_mail(title, message)

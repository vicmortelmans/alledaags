from collection.source import Card
import os


class JozefMaria(Card):
    def __init__(self):
        self._key = "jozefmaria"
        self._category = "contemplation"
        self._type = "daily"
        self._data = { }
        self._template = """
            {% if data %}
            <div class="item">
                <div class="card contemplation">
                    <a target="_blank" href="{{data['url']}}">
                        <div class="padded-image">
                            <img src="{{data['image']}}"/>
                        </div>
                        <div class="title">{{data['name']}}</div>
                        <div class="text">{{data['title']}}</div>
                    </a>
                    <div class="actions">
                        {% set url = my_encode(data['url']) %}
                        {% set title = my_encode("Heilige Jozefmaria Escriva: " + data['title'] + ' via alledaags.gelovenleren.net') %}
                        {% set short_title = my_encode("Heilige Jozefmaria Escriva: " + data['title']) %}
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
        # no loading from web; site protected by cloudflare
        data = {
            'name': "Heilige Jozefmaria Escriva",
            'image':  os.environ['SERVER'] + "/var/jozefmaria.png",
            'url': "https://opusdei.org/nl-nl/page/zijn-boodschap/",
            'title': "Dagelijkse tekst"
        }
        self._data.update(data)



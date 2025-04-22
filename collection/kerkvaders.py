from collection.data import *
from collection.source import Card


class Kerkvaders(Card):
    def __init__(self):
        self._key = "kerkvaders"
        self._category = "catechism mp3"
        self._type = "sequence"
        self._data = { 
            'index': "https://www.radiomaria.be/de-kerk-vaders/heilige-ignatius-van-antiochie/",
        }
        self._template = """
            {% if data %}
            <div class="item{% if oldNews %} oldNews{% endif %}">
                <div class="card contemplation mp3">
                    <a target="_blank" href="{{item['url']}}" onclick="document.cookie='kerkvaders={{item['url']}}; expires=Fri, 31 Dec 9999 23:59:59 GMT;'">
                        <div class="filled-image">
                            <img src="{{item['image']}}"/>
                        </div>
                        <div class="title">{{item['name']}}</div>
                        <div class="text">{{item['title']}}</div>
                    </a>
                    <div class="actions">
                        <a target="_blank" id="play-{{data['key']}}" onclick="document.cookie='{{data['key']}}={{item['url']}}; expires=Fri, 31 Dec 9999 23:59:59 GMT;'">
                            <div class="button play-button">BELUISTEREN</div>
                        </a>
                        <script>
                        $(function(){
                            var audio = playRadio('{{data['key']}}', '{{item['mp3']}}', false, 'alledaags');
                        });
                        //@ sourceURL={{data['key']}}.js
                        </script>
                        <div class="status" id="status-{{data['key']}}"></div>
                    </div>
                    <div class="actions">
                        {% set url = my_encode(item['url']) %}
                        {% set title = my_encode("Kerkvaders: " + item['title'] + ' via alledaags.gelovenleren.net') %}
                        {% set short_title = my_encode("Kerkvaders: " + item['title']) %}
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

    def harvestInit(self):
        # load from web
        urls = [
            "https://www.radiomaria.be/de-kerk-vaders/heilige-ignatius-van-antiochie/",
            "https://www.radiomaria.be/de-kerk-vaders/heilige-johannes-chrysostomus/",
            "https://www.radiomaria.be/de-kerk-vaders/clemens-van-alexandrie/",
            "https://www.radiomaria.be/de-kerk-vaders/de-heilige-hieronymus/",
            "https://www.radiomaria.be/de-kerk-vaders/ireneus-van-lyon/",
            "https://www.radiomaria.be/de-kerk-vaders/athanasius/",
            "https://www.radiomaria.be/de-kerk-vaders/cyprianus-van-carthago/",
            "https://www.radiomaria.be/de-kerk-vaders/h-ambrosius-van-milaan/",
            "https://www.radiomaria.be/de-kerk-vaders/h-basilius-de-grote-een-lichtende-fakkel-van-de-kerk/",
            "https://www.radiomaria.be/de-kerk-vaders/gregorius-van-nyssa/",
            "https://www.radiomaria.be/de-kerk-vaders/cyrillus-van-jeruzalem/",
            "https://www.radiomaria.be/de-kerk-vaders/maximus-de-belijder/",
            "https://www.radiomaria.be/de-kerk-vaders/tertullianus/",
            "https://www.radiomaria.be/de-kerk-vaders/hilarius-van-poitiers/",
            "https://www.radiomaria.be/de-kerk-vaders/origenes/",
            "https://www.radiomaria.be/de-kerk-vaders/origenes-grondlegger-van-de-lectio-divina/",
            "https://www.radiomaria.be/de-kerk-vaders/gregorius-de-grote-kerkvader-en-paus/",
            "https://www.radiomaria.be/de-kerk-vaders/augustinus/"
        ]
        try:
            items = []
            for url in urls:
                xpath = "/html/body"
                harvest = getHtml(url, xpath, tree_requested=True)
                items.append({
                    'title': harvest[0].findtext('.//h2'),
                    'name': "De Kerkvaders",
                    'image': harvest[0].xpath('.//img[contains(@class,"attachment-ocean-thumb-ml")]')[0].get('src'),
                    'url': url,
                    'mp3': harvest[0].find('.//audio/source').get('src'),
                    'id': url
                    })
        except (TypeError, KeyError, IndexError) as e:
            title = "Kerkvaders: init error"
            message = "No data found on %s (%s)" % (url, str(e))
            logging.error(title + " : " + message)
            report_error_by_mail(title, message)
            self._data['items'] = []
        else:
            self._data['items'] = items
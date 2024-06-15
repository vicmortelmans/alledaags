from collection.data import *
from collection.source import Card


class Kerkvaders(Card):
    def __init__(self):
        self._key = "kerkvaders"
        self._category = "catechism mp3"
        self._type = "blog"
        self._data = { }
        self._template = """
            {% if data %}
            <div class="item{% if oldNews %} oldNews{% endif %}">
                <div class="card contemplation mp3">
                    <a target="_blank" href="{{data['url']}}" onclick="document.cookie='kerkvaders={{data['url']}}; expires=Fri, 31 Dec 9999 23:59:59 GMT;'">
                        <div class="filled-image">
                            <img src="{{data['image']}}"/>
                        </div>
                        <div class="title">{{data['name']}}</div>
                        <div class="text">{{data['title']}}</div>
                    </a>
                    <div class="actions">
                        <a target="_blank" id="play-{{data['key']}}" onclick="document.cookie='{{data['key']}}={{data['url']}}; expires=Fri, 31 Dec 9999 23:59:59 GMT;'">
                            <div class="button play-button">BELUISTEREN</div>
                        </a>
                        <script>
                        $(function(){
                            var audio = playRadio('{{data['key']}}', '{{data['mp3']}}', false, 'alledaags');
                        });
                        //@ sourceURL={{data['key']}}.js
                        </script>
                        <div class="status" id="status-{{data['key']}}"></div>
                    </div>
                    <div class="actions">
                        <a target="_blank" href="{{data['index']}}">
                            <div class="button">HISTORIEK</div>
                        </a>
                    </div>
                    <div class="actions">
                        {% set url = my_encode(data['url']) %}
                        {% set title = my_encode("Kerkvaders: " + data['title'] + ' via alledaags.gelovenleren.net') %}
                        {% set short_title = my_encode("Kerkvaders: " + data['title']) %}
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
        site = "http://www.radiomaria.be/de-kerkvaders/"
        xpath_title = "(//h3[contains(@class,'entry-title')]/a)[1]"
        harvest_title = getHtml(site, xpath_title)
        xpath_image = "(//a[contains(@class,'lae-post-link')]/img)[1]"
        harvest_image = getHtml(site, xpath_image)
        data = {
            'name': "Kerkvaders",
            'index': "http://www.radiomaria.be/de-kerkvaders/"
        }
        try:
            data['url'] = harvest_title['a']['href']
            data['title'] = harvest_title['a']['content']
            data['image'] = harvest_image['img']['src']
            site = data['url']
            xpath = "//audio/source/@src"
            harvest = getHtml(site, xpath)
            data['mp3'] = harvest
            data['id'] = site
        except (TypeError, KeyError, IndexError) as e:
            title = "Kerkvaders: sync error"
            message = "No complete data found on %s (%s)" % (site, str(e))
            logging.error(title + " : " + message)
            report_error_by_mail(title, message)
            self._data = {}
        else:
            self._data.update(data)



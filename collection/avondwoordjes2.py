from collection.data import *
from collection.source import Card


class Avondwoordjes2(Card):
    def __init__(self):
        self._key = "avondwoordjes2"
        self._category = "contemplation"
        self._type = "sequence"
        self._data = {
            'index': "https://www.jeugddienstdonbosco.be/don-bosco-als-inspirator/avondwoordjes"
        }
        self._template = """
            <div class="item" id="avondwoordjes2">
                <div class="card contemplation">
                    <a target="_blank" href="{{item['url']}}" onclick="document.cookie='avondwoordjes2={{item['url']}}; expires=Fri, 31 Dec 9999 23:59:59 GMT;'">
                        <div class="filled-image">
                            {% if item['image'] %}
                            <img src="{{item['image']}}"/>
                            {% endif %}
                            {% if item['videoid'] %}
                            <iframe width="304" height="171" src="https://www.youtube.com/embed/{{item['videoid']}}?autoplay=0&amp;rel=0&amp;controls=0&amp;showinfo=0" frameborder="0" allow="encrypted-media" allowfullscreen></iframe>
                            {% endif %}
                        </div>
                        <div class="title">{{item['name']}}</div>
                        <div class="text">{{item['title']}}</div>
                    </a>
                    <div class="actions">
                        <a target="_blank" onclick="load_card('avondwoordjes2');">
                            <div class="action-button"></div>
                        </a>
                        <a target="_blank" href="{{data['index']}}">
                            <div class="button">INHOUD</div>
                        </a>
                    </div>
                    <div class="actions">
                        {% set url = my_encode(item['url']) %}
                        {% set title = my_encode("Avondwoordjes: " + item['title'] + ' via alledaags.gelovenleren.net') %}
                        {% set short_title = my_encode("Avondwoordjes: " + item['title']) %}
                        <a target="_blank" href="https://www.facebook.com/sharer/sharer.php?u={{historical_url}}&title={{title}}">
                            <div class="icon"><img src="/var/facebook-box.png"/></div>
                        </a>
                        <a target="_blank" href="https://twitter.com/intent/tweet?url={{historical_url}}&text={{short_title}}">
                            <div class="icon"><img src="/var/twitter-box.png"/></div>
                        </a>
                        {% if item['image'] %}
                        {% set image = my_encode(item['image']) %}
                        <a target="_blank" href="https://pinterest.com/pin/create/bookmarklet/?media={{image}}&url={{url}}&is_video=false&description={{title}}">
                            <div class="icon"><img src="/var/pinterest.png"/></div>
                        </a>
                        {% endif %}
                         <a target="_blank" href="{{link_url}}">
                            <div class="icon"><img src="/var/link.png"/></div>
                        </a>
                   </div>
                </div>
            </div>
        """

    def harvestInit(self):
        # create a list of urls
        site = self._data['index']
        xpath_number = "//ul[contains(@class,'pagination')]/li[last()-1]/a/text()"
        harvest_number = getHtml(site, xpath_number)
        list = [site]
        for i in range(int(harvest_number)):
            list.append("https://www.jeugddienstdonbosco.be/don-bosco-als-inspirator/avondwoordjes?page=" + str(i+1))
        # obtain data from each url in the list
        items = []
        try:
            for url in list:
                xpath = "//div[contains(@class,'cards-container')]/div/div/a"
                harvest = getHtml(url, xpath)
                for a in harvest['a']:
                    item = {
                        'name': "Don Bosco Avondwoordjes",
                        'url': "https://www.jeugddienstdonbosco.be" + a['href'],
                    }
                    if 'img' in a:
                        item['image'] = a['img']['src']
                        item['title'] = a['div'][0]['h5']['content']
                    else:  # assume there's a video
                        video = a['div'][0]['div']['iframe']['src']
                        item['videoid'] = video.split("embed/",1)[1]  # substring-after pattern
                        item['title'] = a['div'][1]['h5']['content']
                    items.append(item)
        except (TypeError, KeyError, IndexError) as e:
            title = "Avondwoordjes2: init error"
            message = "No data found on %s (%s)" % (site, str(e))
            logging.error(title + " : " + message)
            report_error_by_mail(title, message)
            self._data['items'] = []
        else:
            self._data['items'] = items


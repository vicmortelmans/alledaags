from collection.data import *
from collection.source import Card


class LuistertNaarHem(Card):
    def __init__(self):
        self._key = "luistertnaarhem"
        self._category = "catechism"
        self._type = "sequence"
        self._data = {
            'index': "https://prentencatechismus.org/inhoud-luistert-naar-hem/"  # the trailing / is important for YQL not to choke on a redirect!
        }
        self._template = """
            <div class="item" id="luistertnaarhem">
                <div class="card catechism">
                    <a target="_blank" href="{{item['url']}}" onclick="document.cookie='luistertnaarhem={{item['url']}}; expires=Fri, 31 Dec 9999 23:59:59 GMT;'">
                        <div class="filled-image">
                            <img src="{{item['image']}}"/>
                        </div>
                        <div class="title">{{item['name']}}</div>
                        <div class="text">{{item['title']}}</div>
                    </a>
                    <div class="actions">
                        <a target="_blank" onclick="load_card('luistertnaarhem');">
                            <div class="action-button"></div>
                        </a>
                        <a target="_blank" href="{{data['index']}}">
                            <div class="button">INHOUD</div>
                        </a>
                    </div>
                    <div class="actions">
                        {% set url = my_encode(item['url']) %}
                        {% set title = my_encode("Luistert naar Hem: " + item['title'] + ' via alledaags.gelovenleren.net') %}
                        {% set short_title = my_encode("Luistert naar Hem: " + item['title']) %}
                        {% set image = my_encode(item['image']) %}
                        <a target="_blank" href="https://www.facebook.com/sharer/sharer.php?u={{historical_url}}&title={{title}}">
                            <div class="icon"><img src="/static/facebook-box.png"/></div>
                        </a>
                        <a target="_blank" href="https://twitter.com/intent/tweet?url={{historical_url}}&text={{short_title}}">
                            <div class="icon"><img src="/static/twitter-box.png"/></div>
                        </a>
                        <a target="_blank" href="https://pinterest.com/pin/create/bookmarklet/?media={{image}}&url={{url}}&is_video=false&description={{title}}">
                            <div class="icon"><img src="/static/pinterest.png"/></div>
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
        xpath = "//div[contains(@class,'entry-content')]//li/a"
        harvest = getHtml(site, xpath)
        try:
            self._data['items'] = [
                {
                    'title': a['content'],
                    'url': "https://prentencatechismus.org" + a['href']
                }
                for a in harvest['a']
            ]
        except (TypeError, KeyError, IndexError) as e:
            title = "LuistertNaarHem: init error"
            message = "No data found on %s (%s)" % (site, str(e))
            logging.error(title + " : " + message)
            report_error_by_mail(title, message)
        else:
            for item in self._data['items']:
                site = item['url']
                xpath = "//div[@class='prent']//img"
                harvest = getHtml(site, xpath)
                try:
                    item['name'] = "Luistert naar Hem"
                    item['image'] = "https://prentencatechismus.org" + harvest['img']['src']
                except (TypeError, KeyError, IndexError) as e:
                    title = "LuistertNaarHem: init error"
                    message = "No data found on %s (%s)" % (site, str(e))
                    logging.error(title + " : " + message)
                    report_error_by_mail(title, message)
                time.sleep(1)  # be gently on the host

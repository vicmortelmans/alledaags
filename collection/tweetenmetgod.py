from collection.data import *
from collection.source import Card


class TweetenMetGod(Card):
    def __init__(self):
        self._key = "tweetenmetgod"
        self._category = "catechism"
        self._type = "sequence"
        self._data = {
            'index': "https://www.tweetingwithgod.com/nl/tweets"
        }
        self._template = """
            <div class="item" id="tweetenmetgod">
                <div class="card catechism">
                    <a target="_blank" href="{{item['url']}}" onclick="document.cookie='tweetenmetgod={{item['url']}}; expires=Fri, 31 Dec 9999 23:59:59 GMT;'">
                        <div class="filled-image">
                            <img src="{{item['image']}}"/>
                        </div>
                        <div class="title">{{item['name']}}</div>
                        {% if item['title'] %}<div class="caption">{{item['section']}}</div>{% endif %}
                        <div class="text">{{item['title']}}</div>
                    </a>
                    <div class="actions">
                        <a target="_blank" onclick="load_card('tweetenmetgod');">
                            <div class="action-button"></div>
                        </a>
                        <a target="_blank" href="{{data['index']}}">
                            <div class="button">INHOUD</div>
                        </a>
                    </div>
                    <div class="actions">
                        {% set url = my_encode(item['url']) %}
                        {% set title = my_encode(item['title'] + ' via alledaags.gelovenleren.net') %}
                        {% set short_title = my_encode(item['title']) %}
                        {% set image = my_encode(item['image']) %}
                        <a target="_blank" href="https://www.facebook.com/sharer/sharer.php?u={{historical_url}}&title={{title}}">
                            <div class="icon"><img src="/var/facebook-box.png"/></div>
                        </a>
                        <a target="_blank" href="https://twitter.com/intent/tweet?url={{historical_url}}&text={{short_title}}">
                            <div class="icon"><img src="/var/twitter-box.png"/></div>
                        </a>
                        <a target="_blank" href="https://pinterest.com/pin/create/bookmarklet/?media={{image}}&url={{url}}&is_video=false&description={{title}}">
                            <div class="icon"><img src="/var/pinterest.png"/></div>
                        </a>
                         <a target="_blank" href="{{link_url}}">
                            <div class="icon"><img src="/var/link.png"/></div>
                        </a>
                   </div>
                </div>
            </div>
        """

    def harvestInit(self):
        site = self._data['index']
        xpath = "//div[@class='live-page-search']"
        harvest = getHtml(site, xpath)
        try:
            self._data['items'] = [
                {
                    'title': div['a']['content'],
                    'url': "https://www.tweetingwithgod.com" + div['a']['href']
                }
                for div in harvest['div']
                if div['a']['content'][:1].isdigit()
            ]
        except (TypeError, KeyError) as e:
            title = "TweetenMetGod: sync error"
            message = "No data found on %s (%s)" % (site, str(e))
            logging.error(title + " : " + message)
            report_error_by_mail(title, message)
        else:
            for i in self._data['items']:
                site = i['url']
                xpath = "//article"
                harvest = getHtml(site, xpath)
                item = {}
                try:
                    item['name'] = "Tweeting with God"
                    item['image'] = harvest['article'][0]['figure']['img']['src']
                    item['section'] = harvest['article'][0]['div']['content'].strip()
                except (TypeError, KeyError, IndexError) as e:
                    title = "TweetenMetGod: sync error"
                    message = "No data found on %s (%s)" % (site, str(e))
                    logging.error(title + " : " + message)
                    report_error_by_mail(title, message)
                else:
                    i.update(item)
                time.sleep(1)  # be gently on the host

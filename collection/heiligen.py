from collection.data import *
from collection.source import Card


class Heiligen(Card):
    def __init__(self):
        self._key = "heiligen"
        self._category = "saints"
        self._type = "daily"
        self._data = {}
        self._template = """
            {% if data %}
            <div class="item">
                <div class="card saints">
                    <a target="_blank" href="{{data['url']}}">
                        {% if 'image' in data %}
                        <div class="filled-image">
                            <img src="{{data['image']}}"/>
                        </div>
                        {% endif %}
                        <div class="title">{{data['name']}}</div>
                        <div class="text">{{data['title']}}</div>
                    </a>
                    <div class="actions">
                        <a target="_blank" href="{{data['index']}}">
                            <div class="button">DAGHEILIGEN</div>
                        </a>
                    </div>
                    <div class="actions">
                        {% set url = my_encode(data['url']) %}
                        {% set title = my_encode(data['title'] + ' via alledaags.gelovenleren.net') %}
                        {% set short_title = my_encode(data['title']) %}
                        {% if 'image' in data %}
                        {% set image = my_encode(data['image']) %}
                        {% endif %}
                        <a target="_blank" href="https://www.facebook.com/sharer/sharer.php?u={{historical_url}}&title={{title}}">
                            <div class="icon"><img src="/var/facebook-box.png"/></div>
                        </a>
                        <a target="_blank" href="https://twitter.com/intent/tweet?url={{historical_url}}&text={{short_title}}">
                            <div class="icon"><img src="/var/twitter-box.png"/></div>
                        </a>
                        {% if 'image' in data %}
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
            {% endif %}
        """

    def harvestSync(self):
        # load from web
        feed = "http://takes-long.katholiekkwartetten.appspot.com/heiligen-net.rss"
        harvest = getRSS(feed)
        try:
            # find the longest entry
            longestItemLength = 0
            for item in harvest['item']:
                if 'description' in item and len(item['description']) > longestItemLength:
                    longestItemLength = len(item['description'])
                    longestItem = item
            site = longestItem['link']
            xpath1 = "//div[contains(@id,'rompnaam')]"
            harvest1 = getHtml(site, xpath1)
            xpath2 = "//div[contains(@id,'inhoud')]//img"
            harvest2 = getHtml(site, xpath2)
            data = {
                'name': "Heiligen"
            }
        except (TypeError, KeyError, IndexError) as e:
            title = "Heiligen: sync error"
            message = "No complete data found on %s (%s)" % (feed, str(e))
            logging.error(title + " : " + message)
            report_error_by_mail(title, message)
        else:
            try:
                data['url'] = site
                data['index'] = "https://heiligen.net/heiligen_dag.php?MD=%s" % time.strftime("%m%d")
                data['title'] = harvest1['div']['content']
                try:
                    data['image'] = "https://heiligen.net" + harvest2['img'][1]['src']
                except (TypeError, KeyError, IndexError):
                    logging.warning("No image found on %s." % site)
                    data['image'] = "https://heiligen.net/images/allerh.jpg"
            except (TypeError, KeyError, IndexError):
                logging.error("No data found on %s." % site)
            else:
                self._data.update(data)



from collection.data import *
from collection.source import Card


class EWTNMutsaerts(Card):
    def __init__(self):
        self._key = "ewtn_mutsaerts"
        self._category = "contemplation mp3"
        self._type = "blog"
        self._data = {}
        self._template = """
            {% if data %}
            <div class="item{% if oldNews %} oldNews{% endif %}">
                <div class="card contemplation mp3">
                    <a target="_blank" href="{{data['url']}}" onclick="document.cookie='{{data['key']}}={{data['url']}}; expires=Fri, 31 Dec 9999 23:59:59 GMT;'">
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
                        {% set url = my_encode(data['url']) %}
                        {% set title = my_encode("Katholiek Leven Podcast: " + data['title'] + ' via alledaags.gelovenleren.net') %}
                        {% set short_title = my_encode("Katholiek Leven Podcast: " + data['title']) %}
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
        # load from feed
        feed = "https://feeds.buzzsprout.com/1698907.rss"
        harvest = getRSS(feed, headers=True)
        data = {
            'name': "EWTN Lage Landen - Mgr Rob Mutsaerts Vastentijd",
            'image': "https://alledaags.gelovenleren.net/var/mutsaerts.jpeg",
            'key': self._key
        }
        try:
            if type(harvest['item']) is list:
                item = harvest['item'][0]
            else:
                item = harvest['item']
            data['title'] = item['title'][0]  # duplicate title in rss
            data['url'] = 'https://podcasts.apple.com/nl/podcast/ewtn-lage-landen-mgr-rob-mutsaerts/id1553978203'
            data['mp3'] = item['enclosure']['url']
            data['id'] = data['mp3']
        except (TypeError, KeyError, IndexError) as e:
            title = "EWTNMutsaerts: sync error"
            message = "No complete data found on %s (%s)" % (feed, str(e))
            logging.error(title + " : " + message)
            report_error_by_mail(title, message)
            self._data = {}
        else:
            self._data.update(data)



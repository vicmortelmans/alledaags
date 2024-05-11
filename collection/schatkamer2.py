import API_keys
from collection.data import *
from collection.source import Card


class Schatkamer2(Card):
    def __init__(self):
        self._key = "schatkamer2"
        self._category = "contemplation video"
        self._type = "sequence"
        self._data = {}
        self._template = """
            {% if data %}
            <div class="item" id="schatkamer2">
                <div class="card contemplation video">
                    <a target="_blank" href="{{item['url']}}" onclick="document.cookie='{{data['key']}}={{item['url']}}; expires=Fri, 31 Dec 9999 23:59:59 GMT;'">
                        <div class="filled-image">
                            <iframe width="304" height="171" src="{{item['video']}}?autoplay=0&amp;rel=0&amp;controls=0&amp;showinfo=0" frameborder="0" allow="encrypted-media" allowfullscreen></iframe>
                        </div>
                        <div class="title">{{data['name']}}</div>
                        <div class="text">{{item['title']}}</div>
                    </a>
                    <div class="actions">
                        <a target="_blank" onclick="load_card('schatkamer2');">
                            <div class="action-button"></div>
                        </a>
                        <a target="_blank" href="{{data['index']}}">
                            <div class="button">INHOUD</div>
                        </a>
                    </div>
                    <div class="actions">
                        {% set url = my_encode(item['url']) %}
                        {% set title = my_encode("De Schatkamer: " + item['title'] + ' via alledaags.gelovenleren.net') %}
                        {% set short_title = my_encode("De Schatkamer: " + item['title']) %}
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

    def harvestInit(self):
        # load from feed
        site = "https://www.googleapis.com/youtube/v3/playlistItems?playlistId=PLsTqv8iy6f_2rXSsT3Hu3FzJ3EZpYHTu4&maxResults=25&part=snippet%2CcontentDetails&key=" + API_keys.YOUTUBE
        harvest = getJSON(site)
        self._data = {
            'index': "https://www.youtube.com/playlist?list=PLsTqv8iy6f_2rXSsT3Hu3FzJ3EZpYHTu4",
            'key': self._key
        }
        try:
            self._data['items'] = [
                {
                    'name': "De Schatkamer",
                    'image': "/var/schatkamer.jpg",
                    'title': item['snippet']['title'],
                    'video': "https://www.youtube.com/embed/" + item['contentDetails']['videoId'],
                    'url': "https://www.youtube.com/watch?v=" + item['contentDetails']['videoId']
                }
                for item in harvest['items']
            ]
            while 'nextPageToken' in harvest:
                site = "https://www.googleapis.com/youtube/v3/playlistItems?playlistId=PLsTqv8iy6f_2rXSsT3Hu3FzJ3EZpYHTu4&maxResults=25&part=snippet%2CcontentDetails&key=" + API_keys.YOUTUBE + "&pageToken=" + harvest['nextPageToken'] + "&key=" + API_keys.YOUTUBE
                harvest = getJSON(site)
                self._data['items'] += [
                    {
                        'name': "De Schatkamer",
                        'image': "/var/schatkamer.jpg",
                        'title': item['snippet']['title'],
                        'video': "https://www.youtube.com/embed/" + item['contentDetails']['videoId'],
                        'url': "https://www.youtube.com/watch?v=" + item['contentDetails']['videoId']
                    }
                    for item in harvest['items']
                ]

        except (TypeError, KeyError, IndexError) as e:
            title = "De Schatkamer: init error"
            message = "No complete data found on %s (%s)" % (site, str(e))
            logging.error(title + " : " + message)
            report_error_by_mail(title, message)



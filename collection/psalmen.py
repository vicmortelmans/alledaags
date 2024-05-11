from collection.data import *
from collection.source import Card


class Psalmen(Card):
    def __init__(self):
        self._key = "psalmen"
        self._category = "bible video"
        self._type = "sequence"
        self._data = {}
        self._template = """
            {% if data %}
            <div class="item" id="psalmen">
                <div class="card bible video">
                    <a target="_blank" href="{{item['url']}}" onclick="document.cookie='{{data['key']}}={{item['url']}}; expires=Fri, 31 Dec 9999 23:59:59 GMT;'">
                        <div class="filled-image">
                            <iframe width="304" height="171" src="{{item['video']}}?autoplay=0&amp;rel=0&amp;controls=0&amp;showinfo=0" frameborder="0" allow="encrypted-media" allowfullscreen></iframe>
                        </div>
                        <div class="title">{{data['name']}}</div>
                        <div class="text">{{item['title']}}</div>
                    </a>
                    <div class="actions">
                        <a target="_blank" onclick="load_card('psalmen');">
                            <div class="action-button"></div>
                        </a>
                        <a target="_blank" href="{{data['index']}}">
                            <div class="button">INHOUD</div>
                        </a>
                    </div>
                    <div class="actions">
                        {% set url = my_encode(item['url']) %}
                        {% set title = my_encode("Psalmen: " + item['title'] + ' via alledaags.gelovenleren.net') %}
                        {% set short_title = my_encode("Psalmen: " + item['title']) %}
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
        site = "https://www.googleapis.com/youtube/v3/playlistItems?playlistId=PL6452647DF97A3EDC&maxResults=25&part=snippet%2CcontentDetails&key=AIzaSyBClmJxCBMvWS1lyrrPAdruiefymwnb-04"
        harvest = getJSON(site)
        self._data = {
            'index': "https://www.youtube.com/playlist?list=PL6452647DF97A3EDC",
            'key': self._key
        }
        try:
            self._data['items'] = [
                {
                    'name': "Psalmen",
                    'image': "/var/psalmen.png",
                    'title': item['snippet']['title'],
                    'video': "https://www.youtube.com/embed/" + item['contentDetails']['videoId'],
                    'url': "https://www.youtube.com/watch?v=" + item['contentDetails']['videoId']
                }
                for item in harvest['items']
            ]
            while 'nextPageToken' in harvest:
                site = "https://www.googleapis.com/youtube/v3/playlistItems?playlistId=PL6452647DF97A3EDC&maxResults=25&part=snippet%2CcontentDetails&key=AIzaSyBClmJxCBMvWS1lyrrPAdruiefymwnb-04&pageToken=" + harvest['nextPageToken'] + "&key=AIzaSyDM32pGS7UnaYy1_7czui7eGa_HYb56R7s"
                harvest = getJSON(site)
                self._data['items'] += [
                    {
                        'name': "Psalmen",
                        'image': "/var/psalmen.png",
                        'title': item['snippet']['title'],
                        'video': "https://www.youtube.com/embed/" + item['contentDetails']['videoId'],
                        'url': "https://www.youtube.com/watch?v=" + item['contentDetails']['videoId']
                    }
                    for item in harvest['items']
                ]

        except (TypeError, KeyError, IndexError) as e:
            title = "Psalmen: init error"
            message = "No complete data found on %s (%s)" % (site, str(e))
            logging.error(title + " : " + message)
            report_error_by_mail(title, message)



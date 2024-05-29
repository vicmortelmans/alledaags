from collection.data import *
from collection.source import Card


class SterkeTijden(Card):
    def __init__(self):
        self._key = "sterketijden"
        self._category = "contemplation video"
        self._type = "blog"
        self._data = {}
        self._template = """
            {% if data %}
            <div class="item{% if oldNews %} oldNews{% endif %}" id="sterketijden">
                <div class="card contemplation video">
                    <a target="_blank" href="{{data['url']}}" onclick="document.cookie='{{data['key']}}={{data['url']}}; expires=Fri, 31 Dec 9999 23:59:59 GMT;'">
                        <div class="filled-image">
                            <img src="{{data['image']}}"/>
                        </div>
                        <div class="title">{{data['name']}}</div>
                        <div class="text">{{data['title']}}</div>
                    </a>
                    <div class="actions">
                        <a target="_blank" href="{{data['index']}}">
                            <div class="button">HISTORIEK</div>
                        </a>
                    </div>
                    <div class="actions">
                        {% set url = my_encode(data['url']) %}
                        {% set title = my_encode("Sterke tijden: " + data['title'] + ' via alledaags.gelovenleren.net') %}
                        {% set short_title = my_encode("Sterke tijden: " + data['title']) %}
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
        # load from feed
        site = "https://www.googleapis.com/youtube/v3/playlistItems?playlistId=PLLoFkqNgcwx9ThUCt1jZTgFO1e5bArXRO&maxResults=25&part=snippet%2CcontentDetails&key=AIzaSyBClmJxCBMvWS1lyrrPAdruiefymwnb-04"
        harvest = getJSON(site)
        self._data = {
            'index': "https://www.youtube.com/playlist?list=PLLoFkqNgcwx9ThUCt1jZTgFO1e5bArXRO",
            'key': self._key,
            'name': "Sterke tijden",
            'image': "/static/sterketijden.png"
        }
        try:
            items = [
                {
                    'title': item['snippet']['title'],
                    'video': "https://www.youtube.com/embed/" + item['snippet']['resourceId']['videoId'],
                    'url': "https://www.youtube.com/watch?v=" + item['snippet']['resourceId']['videoId'],
                    'publishedAt': item['snippet']['publishedAt']
                }
                for item in harvest['items']
            ]
            while 'nextPageToken' in harvest:
                site = "https://www.googleapis.com/youtube/v3/playlistItems?playlistId=PLLoFkqNgcwx9ThUCt1jZTgFO1e5bArXRO&maxResults=25&part=snippet%2CcontentDetails&key=AIzaSyBClmJxCBMvWS1lyrrPAdruiefymwnb-04&pageToken=" + harvest['nextPageToken']
                harvest = getJSON(site)
                items += [
                    {
                        'title': item['snippet']['title'],
                        'video': "https://www.youtube.com/embed/" + item['snippet']['resourceId']['videoId'],
                        'url': "https://www.youtube.com/watch?v=" + item['snippet']['resourceId']['videoId'],
                        'publishedAt': item['snippet']['publishedAt']
                    }
                    for item in harvest['items']
                ]

        except (TypeError, KeyError, IndexError) as e:
            title = "Sterke tijden: init error"
            message = "No complete data found on %s (%s)" % (site, str(e))
            logging.error(title + " : " + message)
            report_error_by_mail(title, message)

        newest_date = ""
        for item in items:
            if item['publishedAt'] > newest_date:
                newest_item = item

        self._data['title'] = newest_item['title']
        self._data['video'] = newest_item['video']
        self._data['url'] = newest_item['url']
        self._data['id'] = newest_item['url']




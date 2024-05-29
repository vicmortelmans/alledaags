import API_keys
from collection.data import *
from collection.source import Card
import datetime


class Hemelstraat(Card):
    def __init__(self):
        self._key = "hemelstraat"
        self._category = "contemplation video"
        self._type = "blog"
        self._data = {}
        self._template = """
            {% if data %}
            <div class="item{% if oldNews %} oldNews{% endif %}" id="hemelstraat">
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
                        {% set title = my_encode("FSSPX Antwerpen: " + data['title'] + ' via alledaags.gelovenleren.net') %}
                        {% set short_title = my_encode("FSSPX Antwerpen: " + data['title']) %}
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
        playlist = "https://www.googleapis.com/youtube/v3/playlistItems?playlistId=PLv4oPbaH3WTItrz73LNxoPsOzRO4SdgBm&maxResults=25&part=snippet%2CcontentDetails&key=" + API_keys.YOUTUBE
        harvest_playlist = getJSON(playlist)
        self._data = {
            'index': "https://www.youtube.com/playlist?list=PLv4oPbaH3WTItrz73LNxoPsOzRO4SdgBm",
            'key': self._key,
            'name': "FSSPX Antwerpen",
            'image': "/static/fsspx-antwerpen.png"
        }
        try:
            for item in harvest_playlist['items']:
                videoId = item['snippet']['resourceId']['videoId']
                video = "https://www.googleapis.com/youtube/v3/videos?id=" + videoId + "&maxResults=25&part=liveStreamingDetails&key=" + API_keys.YOUTUBE
                harvest_video = getJSON(video)
                if harvest_video['items'][0]['liveStreamingDetails']['scheduledStartTime'] < datetime.datetime.now().isoformat():
                    newest_item = {
                            'title': item['snippet']['title'],
                            'video': "https://www.youtube.com/embed/" + videoId,
                            'url': "https://www.youtube.com/watch?v=" + videoId,
                            'publishedAt': item['snippet']['publishedAt']
                        }
                    break
        except (TypeError, KeyError, IndexError) as e:
            title = "FSSPX Antwerpen: init error"
            message = "No complete data found on %s (%s)" % (playlist, str(e))
            logging.error(title + " : " + message)
            report_error_by_mail(title, message)

        self._data['title'] = newest_item['title']
        self._data['video'] = newest_item['video']
        self._data['url'] = newest_item['url']
        self._data['id'] = newest_item['url']


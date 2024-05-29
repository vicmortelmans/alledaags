from collection.data import *
from collection.source import Card


class ZingtJubilate(Card):
    def __init__(self):
        self._key = "zingtjubilate"
        self._category = "prayer video"
        self._type = "sequence"
        self._data = {}
        self._template = """
            {% if data %}
            <div class="item" id="zingtjubilate">
                <div class="card prayer video">
                    <a target="_blank" href="{{item['url']}}" onclick="document.cookie='{{data['key']}}={{item['url']}}; expires=Fri, 31 Dec 9999 23:59:59 GMT;'">
                        <div class="filled-image">
                            <iframe width="304" height="171" src="{{item['video']}}?autoplay=0&amp;rel=0&amp;controls=0&amp;showinfo=0" frameborder="0" allow="encrypted-media" allowfullscreen></iframe>
                        </div>
                        <div class="title">{{data['name']}}</div>
                        <div class="text">{{item['title']}}</div>
                    </a>
                    <div class="actions">
                        <a target="_blank" onclick="load_card('zingtjubilate');">
                            <div class="action-button"></div>
                        </a>
                        <a target="_blank" href="{{data['index']}}">
                            <div class="button">INHOUD</div>
                        </a>
                    </div>
                    <div class="actions">
                        {% set url = my_encode(item['url']) %}
                        {% set title = my_encode(item['name'] + ": " + item['title'] + ' via alledaags.gelovenleren.net') %}
                        {% set short_title = my_encode(item['name'] + ": " + item['title']) %}
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

    def harvestInit(self):
        site = "https://www.googleapis.com/youtube/v3/playlistItems?playlistId=PL6452647DF97A3EDC&maxResults=25&part=snippet%2CcontentDetails&key=AIzaSyBClmJxCBMvWS1lyrrPAdruiefymwnb-04"
        harvest = getJSON(site)

        #implementation abandoned; the code below doesn't work because of missing libraries; I have to use REST calls
        #like the above. But the content isn't that good, so I'm not doing the effort

        '''
        youtube = googleapiclient.discovery.build('youtube', 'v3', developerKey="AIzaSyBClmJxCBMvWS1lyrrPAdruiefymwnb-04")
        request = youtube.channels().list(part="contentDetails", id="UCVaShrYQcZLyJZIoSzSK6tw")
        response = request.execute()
        uploads = response['items'][0]['contentDetails']['relatedPlaylists']['uploads']
        request = youtube.playlistItems().list(part="snippet,contentDetails", playlistId=uploads)
        harvest = request.execute()
        self._data = {
            'index': "https://www.youtube.com/feeds/videos.xml?channel_id=UCVaShrYQcZLyJZIoSzSK6tw",
            'key': self._key
        }
        try:
            self._data['items'] = [
                {
                    'name': "Zingt Jubilate",
                    'image': item['group']['thumbnail']['url'],
                    'title': item['title'],
                    'video': "https://www.youtube.com/embed/" + item['videoId'],
                    'url': item['link']['href']
                }
                for item in harvest['items']
            ]

        except (TypeError, KeyError, IndexError) as e:
            title = "ZingtJubilate: init error"
            message = "No complete data found on %s (%s)" % (feed, str(e))
            logging.error(title + " : " + message)
            report_error_by_mail(title, message)

        '''

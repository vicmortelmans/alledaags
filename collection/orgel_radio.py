from collection.source import Radio
import os


class OrgelRadio(Radio):
    def __init__(self):
        self._key = "orgel-radio"
        self._category = "prayer"
        self._type = "daily"
        self._data = {}
        self._template = """
            {% if data %}
            <div class="item" id="item-{{data['key']}}">
                <div class="card prayer">
                    <div class="padded-image">
                        <img src="{{data['image']}}" width="{{data['image-width']}}" height="{{data['image-height']}}""/>
                    </div>
                    <div class="title">{{data['name']}}</div>
                    <div class="text" id="title-{{data['key']}}">{{data['title']}}</div>
                    <div class="actions">
                        <a target="_blank" id="play-{{data['key']}}" class="radio">
                            <div class="action-button play-button"></div>
                        </a>
                        <script>
                        $(function(){
                            var audio = playRadio('{{data['key']}}', '{{data['mp3']}}', true, 'radio');
                        });
                        //@ sourceURL={{data['key']}}.js
                        </script>
                        <div class="status" id="status-{{data['key']}}"></div>
                    </div>
                </div>
            </div>
            {% endif %}
        """

    def harvestInit(self):
        data = {
            'name': "Orgelradio",
            'title': "Organroxx Radio",
            'image': os.environ['SERVER'] + "/static/organroxx-logo.png",
            'image-width': '260',
            'image-height': '141',
            'url': "https://organroxx.com/",
            'mp3': "http://radio.organroxx.com:8000/organmusic.mp3",
            'key': self._key
        }
        self._data.update(data)



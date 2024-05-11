from collection.source import Radio
import os


class RadioMariaNederlandRadio(Radio):
    def __init__(self):
        self._key = "radiomarianederland-radio"
        self._category = "prayer"
        self._type = "daily"
        self._data = {}
        self._template = """
            {% if data %}
            <div class="item" id="item-{{data['key']}}">
                <div class="card prayer">
                    <div class="filled-image">
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
            'name': "Radio Maria Nederland",
            'title': "Live radio",
            'image': os.environ['SERVER'] + "/var/radiomarianederland.png",
            'image-width': '304',
            'image-height': '100',
            'url': "https://www.radiomaria.nl/",
            'mp3': "https://stream.radiomaria.nl/app",
            'key': self._key
        }
        self._data.update(data)



from collection.source import Radio
import collection.cards

DATE_TIME_FORMAT = '%Y-%m-%d %H:%M:%S'

class BiddenOnderwegRadio(Radio):
    def __init__(self):
        self._key = "biddenonderweg-radio"
        self._category = "prayer"
        self._type = "daily"
        self._data = {}
        self._template = """
            {% if data %}
            <div class="item" id="item-{{data['key']}}">
                <div class="card prayer">
                    <div class="padded-image">
                        <img src="{{data['image']}}"/>
                    </div>
                    <div class="title">{{data['name']}}</div>
                    <div class="text">{{data['title']}}</div>
                    {% if 'title2' in data and data['title2'] %}
                    <div class="caption">{{data['title2']}}</div>
                    {% endif %}
                    <div class="actions">
                        <a target="_blank" id="play-{{data['key']}}" class="radio">
                            <div class="action-button play-button"></div>
                        </a>
                        <script>
                        $(function(){
                            var audio = playRadio('{{data['key']}}', '{{data['mp3']}}', false, 'radio');
                        });
                        //@ sourceURL={{data['key']}}.js
                        </script>
                        <div class="status" id="status-{{data['key']}}"></div>
                    </div>
                </div>
            </div>
            {% endif %}
        """

    def harvestSync(self):
        self._data = cards.find_card("biddenonderweg").data
        if self._data:
            self._data['key'] = self._key


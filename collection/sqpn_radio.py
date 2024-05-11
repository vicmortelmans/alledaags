from collection.data import *
from collection.source import Radio


class SqpnRadio(Radio):
    def __init__(self):
        self._key = "sqpn-radio"
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
        data = {
            'name': "SQPN: Catholic Weekend",
            'image-width': '304',
            'image-height': '304',
            'key': self._key
        }
        # load from web
        feed = "https://sqpn.com/category/podcasts/cw/feed/"
        harvest = getRSS(feed)
        # find the first entry
        try:
            item = harvest['item'][0]
            data['mp3'] = item['enclosure']['url']
            data['title'] = item['title']
            data['image'] = item['image']['href']
        except (TypeError, KeyError, IndexError) as e:
            title = "SqpnRadio: sync error"
            message = "No data found on %s (%s)" % (feed, str(e))
            logging.error(title + " : " + message)
            report_error_by_mail(title, message)
        else:
            self._data.update(data)


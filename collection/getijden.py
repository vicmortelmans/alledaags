from collection.source import Card
from datetime import date, datetime, time
from babel.dates import format_date, format_datetime, format_time
import os


class Getijden(Card):
    def __init__(self):
        self._key = "getijden"
        self._category = "prayer"
        self._type = "daily"
        self._data = { }
        self._template = """
            <div class="item">
                <div class="card prayer">
                    <a target="_blank" href="{{data['url']}}">
                        <div class="padded-image">
                            <img src="{{data['image']}}"/>
                        </div>
                        <div class="title">{{data['name']}}</div>
                        <div class="text">{{data['title']}}</div>
                    </a>
                </div>
            </div>
        """

    def harvestSync(self):
        data = {
            'name': "Getijdengebed",
            'image': os.environ['SERVER'] + "/static/getijdengebed.png",
            'url': "https://www.tiltenberg.org/getijdengebed"
        }
        now = datetime.now()
        data['title'] = format_date(now, format='full', locale='nl')
        self._data.update(data)

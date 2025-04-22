from collection.data import *
from collection.source import Card
import datetime


class Seconden(Card):
    def __init__(self):
        self._key = "zingtjubilate2"
        self._category = "lectionary"
        self._type = "daily"
        self._data = {}
        self._template = """
            {% if data %}
            <div class="item">
                <div class="card lectionary">
                    <a target="_blank" href="{{data['url']}}">
                        <div class="filled-image">
                            <img src="{{data['image']}}"/>
                        </div>
                        <div class="title">{{data['name']}}</div>
                        <div class="text">{{data['title']}}</div>
                        <div class="caption">{{data['date']}}</div>
                    </a>
                    <div class="actions">
                        {% set url = my_encode(data['url']) %}
                        {% set title = my_encode("Zingt Jubilate: " + data['title'] + ' via alledaags.gelovenleren.net') %}
                        {% set short_title = my_encode("Zingt Jubilate: " + data['title']) %}
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
        # load from web
        current_date_time = datetime.datetime.now()
        # find a match for date of today or first of next 10 days
        for i in range(10):
            current_date_str = current_date_time.date().strftime("%Y-%m-%d")
            site = "https://www.zingtjubilate.be/LiedSuggesties/getMisByDate?date=" + current_date_str
            harvest = getJSON(site)
            if harvest != "NA":
                data = {
                    'name': "Zingt Jubilate",
                    'index': "https://www.zingtjubilate.be/Liedsuggesties",
                    'image': "https://www.zingtjubilate.be/Images/ZingtJubilate.jpg",
                    'url': "https://www.zingtjubilate.be/Archief/ViewMis/" + str(harvest['id']),
                    'title': harvest['titel'],
                    'date': harvest['tijdstip'][:10]
                }
                self._data.update(data)
                return
            current_date_time += datetime.timedelta(days=1)
        else:
            title = "Zingt Jubilate: sync error"
            message = "No date within 10 days from now found on %s" % site
            logging.error(title + " : " + message)
            report_error_by_mail(title, message)
            self._data = {}
            return
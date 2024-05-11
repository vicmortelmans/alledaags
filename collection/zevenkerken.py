from collection.data import *
from collection.source import Card
import os
from lxml import html, etree


class Zevenkerken(Card):
    def __init__(self):
        self._key = "zevenkerken"
        self._category = "lectionary video"
        self._type = "daily"
        self._data = {}
        self._template = """
            {% if data %}
            <div class="item">
                <div class="card lectionary video">
                    <a target="_blank" href="{{data['url']}}">
                        <div class="filled-image">
                            <iframe width="304" height="171" src="{{data['video']}}?autoplay=0&amp;rel=0&amp;controls=0&amp;showinfo=0" frameborder="0" allow="encrypted-media" allowfullscreen></iframe>
                        </div>
                        <div class="title">{{data['name']}}</div>
                        <div class="text">{{data['title']}}</div>
                    </a>
                    <div class="actions">
                        {% set url = my_encode(data['url']) %}
                        {% set title = my_encode(data['name'] + ": " + data['title'] + ' via alledaags.gelovenleren.net') %}
                        {% set short_title = my_encode(data['name'] + ": " + data['title']) %}
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

    def harvestSync(self):
        data = {
            'name': "Ingesproken Lezingen",
            'image': "/var/BIBLIA.jpg",
            'index': "https://www.kerknet.be/bijbeldienst-bisdom-brugge-vzw/artikel-inspiratie/lectionarium-voor-de-zondagen"
        }
        # load the json file that contains dates linked to the website url's
        # the json is generated offline and uses internal references to the *last* date to find the actual url
        # and to refer dates that have no page to the page that is upcoming in the next days
        DATA_FILE = os.path.join(os.path.dirname(__file__), 'zevenkerken-kalender.json')
        with open(DATA_FILE, 'r') as dataFile:
            kalender = json.loads(dataFile.read())

        # find the url for today
        reference_date = time.strftime("%Y-%m-%d")  # today
        for day in kalender["calendar"]:
            if day["date"] == reference_date:
                if "ref" in day:
                    reference_date = day["ref"]
                    continue
                else:
                    data["url"] = day["url"]
                    data["title"] = day["title"]
                    break

        try:
            # get the link to the soundcloud embed
            # for some reason, they've wrapped the iframe in a <script> tag !?
            xpath_video = "//script[@class='js-cookie-content-blocker-content']"
            harvest_video = getHtml(data['url'], xpath_video)
            hidden_code_block = harvest_video['script']['content']
            parser = etree.HTMLParser()
            tree = etree.HTML(hidden_code_block, parser=parser)
            result = tree.xpath("//iframe/@src")
            data["video"] = (result[0])
        except (TypeError, KeyError, IndexError) as e:
            title = "Zevenkerken: sync error"
            message = "No video link found on %s (%s)" % (data['index'], str(e))
            logging.error(title + " : " + message)
            report_error_by_mail(title, message)
        else:
            self._data.update(data)

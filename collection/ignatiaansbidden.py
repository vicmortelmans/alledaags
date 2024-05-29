from collection.data import *
from collection.source import Card


class IgnatiaansBidden(Card):
    def __init__(self):
        self._key = "ignatiaansbidden"
        self._category = "prayer"
        self._type = "daily"
        self._data = {}
        self._template = """
            {% if data %}
            <div class="item">
                <div class="card prayer">
                    <div class="filled-image">
                        <img src="{{data['image']}}"/>
                    </div>
                    <div class="title">Ignatiaans Bidden</div>
                    {% if 'podcast' in data %}
                    <div class="actions">
                        <a target="_blank" href="{{data['podcasturl']}}">
                            <div class="button">Podcast nr{{data['podcast']}}</div>
                        </a>
                    </div>
                    {% endif %}
                    <div class="actions">
                        <a target="_blank" href="{{data['GeloofsimpulsURL']}}">
                            <div class="button">{{data['Geloofsimpuls']}}</div>
                        </a>
                    </div>
                    <div class="actions">
                        <a target="_blank" href="{{data['CitaatURL']}}">
                            <div class="button">{{data['Citaat']}}</div>
                        </a>
                    </div>
                    <div class="actions">
                        <a target="_blank" href="{{data['GebedstipURL']}}">
                            <div class="button">{{data['Gebedstip']}}</div>
                        </a>
                    </div>
                    <div class="actions">
                        <a target="_blank" href="https://www.ignatiaansbidden.org">
                            <div class="button">AANMELDEN</div>
                        </a>
                    </div>
                    {% if 'podcast' in data %}
                    <div class="actions">
                        {% set url = my_encode("https://www.ignatiaansbidden.org/podcast-nr{{data['podcast']}}-podcast/") %}
                        {% set title = my_encode("40-dagenretraire podcast nr{{data['podcast']}}" + ' via alledaags.gelovenleren.net') %}
                        {% set short_title = my_encode("40-dagenretraire podcast nr{{data['podcast']}}") %}
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
                    {% endif %}
                </div>
            </div>
            {% endif %}
        """

    def harvestSync(self):
        # load from web
        # NOTE: add image and name before reactivating !!
        site = "https://www.ignatiaansbidden.org"
        data = {
            'image': "https://www.ignatiaansbidden.org/wp-content/themes/ib_theme_2021/images/IB_vasten2023_1.jpg"
        }
        xpath = "//div[@class='posts']/a"
        harvest = getHtml(site, xpath)
        try:
            for a in harvest['a']:
                title = a['div']['div']['h2']
                teaser = a['div']['div']['p']['content']
                type = title.split(' ',1)[0]
                data[type] = title + ": " + teaser
                data[type + "URL"] = a['href']
        except (TypeError, KeyError, IndexError) as e:
            title = "IgnatiaansBidden: sync error"
            message = "No data found on %s using '%s' (%s)" % (site, xpath, str(e))
            logging.error(title + " : " + message)
            report_error_by_mail(title, message)
            self._data = {}
        else:
            self._data.update(data)
        """
        today = date.today()
        tomorrow = today + datetime.timedelta(days=1)
        ashes = date(2015, 2, 18)
        nr = (today - ashes).days + 2
        sitePodCast = "https://www.ignatiaansbidden.org/podcast-nr%d-%s-%s/" % (nr, tomorrow.strftime("%d").lstrip('0'), month(tomorrow.strftime("%m")))
        xpathPodCast = "//h2"
        harvestPodCast = getHtml(sitePodCast, xpathPodCast)
        if harvestPodCast:
            self._data['podcast'] = nr
            self._data['podcasturl'] = sitePodCast
        else:
            nr -= 1
            sitePodCast = "https://www.ignatiaansbidden.org/podcast-nr%d-%s-%s/" % (nr, today.strftime("%d").lstrip('0'), month(today.strftime("%m")))
            xpathPodCast = "//h2"
            harvestPodCast = getHtml(sitePodCast, xpathPodCast)
            if harvestPodCast:
                self._data['podcast'] = nr
                self._data['podcasturl'] = sitePodCast
        """


def month(m):
    try:
        s = {
            '02': "februari",
            '03': "maart",
            '04': "april",
            '11': "november",
            '12': "december"
        }[m]
    except (KeyError):
        logging.error("This doesn't work in month %s" % m)
        s = "error"
    return s

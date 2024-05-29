from collection.data import *
from collection.source import Card
import os
import lxml
import re
import datetime


class Seconden(Card):
    def __init__(self):
        self._key = "seconden"
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
                        {% set title = my_encode("Seconden: " + data['title'] + ' via alledaags.gelovenleren.net') %}
                        {% set short_title = my_encode("Seconden: " + data['title']) %}
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

    def parse_date(self, text):
        date_match = re.search(r'\d{1,2} [a-zA-Z]+', text)
        if date_match:
            date_str = date_match.group().lower()
            month_name = re.search(r'[a-zA-Z]+', date_str).group()
            month_str_padded = str({
                'januari': 1,
                'februari': 2,
                'maart': 3,
                'april': 4,
                'mei': 5,
                'juni': 6,
                'juli': 7,
                'augustus': 8,
                'september': 9,
                'oktober': 10,
                'november': 11,
                'december': 12,
            }[month_name]).zfill(2)
            day_str_padded = re.search(r'\d{1,2}', date_str).group().zfill(2)
            current_date_time = datetime.datetime.now()
            current_year_str = current_date_time.date().strftime("%Y")
            current_month_str_padded = current_date_time.date().strftime("%m")
            if current_month_str_padded > '09' and month_str_padded < '03':
                year_str = str(int(current_year_str) + 1)
            elif current_month_str_padded < '03' and month_str_padded > '09':
                year_str = str(int(current_year_str) - 1)
            else:
                year_str = current_year_str
            return year_str + '-' + month_str_padded + '-' + day_str_padded, date_str
        else:
            return "", ""

    def parse_text(self, element):
        parsed_text = ""
        for node in element:
            text = ""
            if isinstance(node, lxml.etree._ElementStringResult):
                text = node.strip(' \n\t:')
            elif isinstance(node, lxml.etree._Element):
                text = self.parse_text(node)
            if text:
                parsed_text += text + ' '
        if element.text:
            parsed_text += element.text.strip(' \n\t:') + ' '  # for elements that only have text
        if element.tail:
            parsed_text += element.tail.strip(' \n\t:') + ' '  # for text inside mixed content elements
        return parsed_text

    def harvestSync(self):
        # load from web
        site = "https://bijbelin1000seconden.be/menu/tiki-index.php?page=Liturgische+kalender"
        xpath = "//div[@id = 'page-data']/p"
        harvest = getHtml(site, xpath, tree_requested=True)
        data = {
            'name': "Bijbel in 1000 seconden",
            'image': os.environ['SERVER'] + "/static/seconden.png",
        }
        try:
            # traverse the tree grouping elements in lines (split at <p> or <br>), recording
            # - full text of the line
            # - first link
            # - parsed date (if any present)
            lines = []
            for p in harvest:
                line = ""
                link = ""
                date = ""
                date_str = ""
                for node in p:
                    if isinstance(node, lxml.etree._ElementStringResult):
                        text = node.strip(' \n\t:')
                        if text:
                            line += text + ' '
                            parsed_date, parsed_date_str = self.parse_date(text)
                            if parsed_date:
                                date = parsed_date
                                date_str = parsed_date_str
                    elif isinstance(node, lxml.etree._Element):
                        if node.tag == 'br':
                            # line is finished
                            if line:
                                lines.append({
                                    'line': line,
                                    'link': link,
                                    'date': date,
                                    'date_str': date_str
                                })
                            line = ""
                            link = ""
                            date = ""
                            continue
                        if node.tag == 'a':
                            link = node.get('href')
                        text = self.parse_text(node)
                        if text:
                            line += text + ' '
                            parsed_date, parsed_date_str = self.parse_date(text)
                            if parsed_date:
                                date = parsed_date
                                date_str = parsed_date_str
                # end of <p> so line is finished
                if line:
                    lines.append({
                        'line': line,
                        'link': link,
                        'date': date,
                        'date_str': date_str
                    })
                line = ""
                link = ""
                date = ""
            # with today's date as key, find line with matching date or inbetween two dates
            current_date_time = datetime.datetime.now()
            current_date_str = current_date_time.date().strftime("%Y-%m-%d")
            candidate = lines[0]
            for line in lines:
                if 'date' in line:
                    if line['date'] == current_date_str:
                        candidate = line
                        break
                    elif line['date'] > current_date_str:
                        break
                    else:
                        candidate = line
                else:
                    candidate = line
            data['url'] = "https://bijbelin1000seconden.be/menu/" + candidate['link']
            data['title'] = candidate['line']
            data['date'] = candidate['date_str']
            # now see if we can fetch an image
            site = data['url']
            xpath = "(//div[@id = 'page-data']/img)[1]"
            harvest = getHtml(site, xpath)
            if 'img' in harvest:
                data['image'] = "https://bijbelin1000seconden.be/menu/" + harvest['img']['src']
        except (TypeError, KeyError, IndexError) as e:
            title = "Seconden: sync error"
            message = "No data found on %s (%s)" % (site, str(e))
            logging.error(title + " : " + message)
            report_error_by_mail(title, message)
            self._data = {}
        else:
            self._data.update(data)



from collection.data import *
from collection.source import Card


class AtotZ(Card):
    def __init__(self):
        self._key = "atotz"
        self._category = "catechism"
        self._type = "sequence"
        self._template = """
            <div class="item" id="atotz">
                <div class="card catechism">
                    <a target="_blank" href="{{item['url']}}" onclick="document.cookie='atotz={{item['url']}}; expires=Fri, 31 Dec 9999 23:59:59 GMT;'">
                        <div class="filled-image">
                            <img src="{{item['image']}}"/>
                        </div>
                        <div class="title">{{item['name']}}</div>
                        <div class="text">{{item['title']}}</div>
                    </a>
                    <div class="actions">
                        <a target="_blank" onclick="load_card('atotz');">
                            <div class="action-button"></div>
                        </a>
                        <a target="_blank" href="{{data['index']}}">
                            <div class="button">INHOUD</div>
                        </a>
                    </div>
                    <div class="actions">
                        {% set url = my_encode(item['url']) %}
                        {% set title = my_encode("Bijbel van A tot Z: " + item['title'] + ' via alledaags.gelovenleren.net') %}
                        {% set short_title = my_encode("Bijbel van A tot Z: " + item['title']) %}
                        {% set image = my_encode(item['image']) %}
                        <a target="_blank" href="https://www.facebook.com/sharer/sharer.php?u={{historical_url}}&title={{title}}">
                            <div class="icon"><img src="/var/facebook-box.png"/></div>
                        </a>
                        <a target="_blank" href="https://twitter.com/intent/tweet?url={{historical_url}}&text={{short_title}}">
                            <div class="icon"><img src="/var/twitter-box.png"/></div>
                        </a>
                        <a target="_blank" href="https://pinterest.com/pin/create/bookmarklet/?media={{image}}&url={{url}}&is_video=false&description={{title}}">
                            <div class="icon"><img src="/var/pinterest.png"/></div>
                        </a>
                         <a target="_blank" href="{{link_url}}">
                            <div class="icon"><img src="/var/link.png"/></div>
                        </a>
                   </div>
                </div>
            </div>
        """

    def harvestInit(self):
        self._data = {
            'index': "https://www.kerknet.be/biblia/artikel/bijbel-van-tot-z"
        }
        sites = [
            "https://www.kerknet.be/bijbeldienst-bisdom-brugge-vzw/blog/bijbel-van-tot-z-reeks-1-0",
            "https://www.kerknet.be/bijbeldienst-bisdom-brugge-vzw/inspiratie/bijbel-van-tot-z-overzicht-reeks-3",
            "https://www.kerknet.be/bijbeldienst-bisdom-brugge-vzw/inspiratie/bijbel-van-tot-z-reeks-4"
        ]
        self._data['items'] = []
        xpath = "//div[h3]//td"
        for site in sites:
            harvest = getHtml(site, xpath)
            odd_td = True
            for td in harvest['td']:
                if odd_td:
                    # odd td's have an image
                    item = {'name': "Bijbel van A tot Z"}
                    try:
                        item['image'] = td['div']['div']['div']['img']['src']
                    except (TypeError, KeyError) as e:
                        title = "AtotZ: init error"
                        message = "Some td without image found on %s (%s)" % (site, str(e))
                        logging.error(title + " : " + message)
                        item['image'] = '/var/atotz.jpg'
                else:
                    # even td's have a link
                    try:
                        if 'strong' in td:
                            item['title'] = td['strong']['a']['content']
                            item['url'] = td['strong']['a']['href']
                        else:
                            item['title'] = td['a']['content']
                            item['url'] = td['a']['href']
                    except (TypeError, KeyError) as e:
                        title = "AtotZ: init error"
                        message = "Some item without data found on %s (%s)" % (site, str(e))
                        logging.error(title + " : " + message)
                    else:
                        self._data['items'].append(item)
                odd_td = not odd_td
        # the page containing the second series has the table hidden in a script element
        site = "https://www.kerknet.be/bijbeldienst-bisdom-brugge-vzw/inspiratie/bijbel-van-tot-z-overzicht-reeks-2"
        xpath_video = "//script[@class='js-cookie-content-blocker-content']"
        harvest_video = getHtml(site, xpath_video)
        hidden_code_block = harvest_video['script']['content']
        parser = etree.HTMLParser()
        tree = etree.HTML(hidden_code_block, parser=parser)
        harvest = elements_list_to_json(tree.xpath("//td"))
        odd_td = True
        for td in harvest['td']:
            if odd_td:
                # odd td's have an image
                item = {'name': "Bijbel van A tot Z"}
                try:
                    if 'strong' in td:
                        item['image'] = td['strong']['img']['src']
                    else:
                        item['image'] = td['img']['src']
                except (TypeError, KeyError) as e:
                    title = "AtotZ: init error"
                    message = "Some td without image found on %s (%s)" % (site, str(e))
                    logging.error(title + " : " + message)
                    item['image'] = '/var/atotz.jpg'
            else:
                # even td's have a link
                try:
                    if 'strong' in td:
                        item['title'] = td['strong']['a']['content']
                        item['url'] = td['strong']['a']['href']
                    else:
                        item['title'] = td['a']['content']
                        item['url'] = td['a']['href']
                except (TypeError, KeyError) as e:
                    title = "AtotZ: init error"
                    message = "Some item without data found on %s (%s)" % (site, str(e))
                    logging.error(title + " : " + message)
                    odd_td = not odd_td
                    continue
                else:
                    self._data['items'].append(item)
            odd_td = not odd_td

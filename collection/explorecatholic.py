from collection.data import *
from collection.source import Card
import os
import json


class ExploreCatholic(Card):
    def __init__(self):
        self._key = "explorecatholic"
        self._category = "prayer"
        self._type = "sequence"
        self._data = {
            'index': "https://explorecatholic.nl/bidden/gebeden/",
        }
        self._template = """
            <div class="item" id="explorecatholic">
                <div class="card prayer">
                    <a target="_blank" href="{{item['url']}}" onclick="document.cookie='{{item['key']}}={{item['url']}}; expires=Fri, 31 Dec 9999 23:59:59 GMT;'">
                        <div class="filled-image">
                            <img src="{{item['image']}}"/>
                        </div>
                        <div class="title">{{item['name']}}</div>
                        <div class="text">{{item['title']}}</div>
                    </a>
                    <div class="actions">
                        <a target="_blank" onclick="load_card('explorecatholic');">
                            <div class="action-button"></div>
                        </a>
                        <a target="_blank" href="{{data['index']}}">
                            <div class="button">INHOUD</div>
                        </a>
                    </div>
                    <div class="actions">
                        <a target="_blank" href="{{item['instagram']}}">
                            <div class="button">INSTAGRAM</div>
                        </a>
                    </div>
                    <div class="actions">
                        {% set url = my_encode(item['url']) %}
                        {% set title = my_encode("{{item['name']}}: " + item['title'] + ' via alledaags.gelovenleren.net') %}
                        {% set short_title = my_encode("{{item['name']}}: " + item['title']) %}
                        {% set image = my_encode(item['image']) %}
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
        """

    def harvestInit(self):
        urls = ["https://explorecatholic.nl/portfolio/kruisweg/",
            "https://explorecatholic.nl/portfolio/lofzang-van-simeon-lc-229-32/",
            "https://explorecatholic.nl/portfolio/lofzang-van-maria-lc-146-55/",
            "https://explorecatholic.nl/portfolio/lofzang-van-zacharias-lc-168-79/",
            "https://explorecatholic.nl/portfolio/salve-regina/",
            "https://explorecatholic.nl/portfolio/angelus/",
            "https://explorecatholic.nl/portfolio/gebed-uit-berouw/",
            "https://explorecatholic.nl/portfolio/gebed-om-liefde/",
            "https://explorecatholic.nl/portfolio/gebed-om-hoop/",
            "https://explorecatholic.nl/portfolio/gebed-om-geloof/",
            "https://explorecatholic.nl/portfolio/schuldbelijdenis-confiteor/",
            "https://explorecatholic.nl/portfolio/geloofsbelijdenis-van-nicea/",
            "https://explorecatholic.nl/portfolio/de-apostolische-geloofsbelijdenis/",
            "https://explorecatholic.nl/portfolio/eer-aan-de-vader/",
            "https://explorecatholic.nl/portfolio/gloria-gloria-in-excelsis-deo/",
            "https://explorecatholic.nl/portfolio/wees-gegroet-maria-ave-maria/",
            "https://explorecatholic.nl/portfolio/onze-vader/",
            "https://explorecatholic.nl/portfolio/rozenkrans-van-de-goddelijke-barmhartigheid/",
            "https://explorecatholic.nl/portfolio/gebed-tot-de-heilige-anna/",
            "https://explorecatholic.nl/portfolio/noveen-aan-de-heilige-judas-thaddeus-voorspreker-in-hopeloze-zaken/",
            "https://explorecatholic.nl/portfolio/litanie-van-loreto/",
            "https://explorecatholic.nl/portfolio/lofzang-van-maria/",
            "https://explorecatholic.nl/portfolio/regina-coeli/",
            "https://explorecatholic.nl/portfolio/wees-gegroet-maria/",
            "https://explorecatholic.nl/portfolio/gebed-voor-de-heilige-vader/",
            "https://explorecatholic.nl/portfolio/gebed-voor-priesterroepingen/",
            "https://explorecatholic.nl/portfolio/gebed-tot-de-heilige-geest/",
            "https://explorecatholic.nl/portfolio/uw-liefde-is-groter/",
            "https://explorecatholic.nl/portfolio/instrument-van-uw-vrede/",
            "https://explorecatholic.nl/portfolio/zo-klein-en-toch-zo-machtig/",
            "https://explorecatholic.nl/portfolio/zijn-naam-is-jezus/",
            "https://explorecatholic.nl/portfolio/hier-ben-ik/",
            "https://explorecatholic.nl/portfolio/ware-grootheid/",
            "https://explorecatholic.nl/portfolio/vrede-gebed-op-het-kerstfeest/",
            "https://explorecatholic.nl/portfolio/zegenbede/",
            "https://explorecatholic.nl/portfolio/heb-goede-moed/",
            "https://explorecatholic.nl/portfolio/voorbede-om-hoop/",
            "https://explorecatholic.nl/portfolio/gebed-om-in-hoop-te-kunnen-leven/",
            "https://explorecatholic.nl/portfolio/gebed-op-kerstmis/",
            "https://explorecatholic.nl/portfolio/gebed-om-de-voorspraak-van-maria/",
            "https://explorecatholic.nl/portfolio/gebed-om-vertrouwen/",
            "https://explorecatholic.nl/portfolio/gebed-om-zegen-over-een-gemeenschap/",
            "https://explorecatholic.nl/portfolio/god-alleen-voldoet/",
            "https://explorecatholic.nl/portfolio/gebed-van-bernadette/",
            "https://explorecatholic.nl/portfolio/u-weet-van-mijn-tranen/",
            "https://explorecatholic.nl/portfolio/gij-hebt-ons-voor-u-en-elkaar-gemaakt/",
            "https://explorecatholic.nl/portfolio/niet-tevergeefs/"]
        titles = ["Kruisweg",
            "Lofzang van Simeon (Lc 2,29-32)",
            "Lofzang van Maria (Lc 1,46-55)",
            "Lofzang van Zacharias (Lc.1,68-79)",
            "Salve Regina",
            "Angelus",
            "Gebed uit berouw",
            "Gebed om Liefde",
            "Gebed om hoop",
            "Gebed om Geloof",
            "Schuldbelijdenis / Confiteor",
            "Geloofsbelijdenis van Nicea",
            "De apostolische geloofsbelijdenis",
            "Eer aan de Vader",
            "Gloria / Glória in excélsis Deo",
            "Wees gegroet Maria / Ave Maria",
            "Onze Vader",
            "Rozenkrans van de Goddelijke Barmhartigheid",
            "Gebed tot de heilige Anna",
            "Noveen aan de heilige Judas Thaddeüs, voorspreker in hopeloze zaken",
            "Litanie van Loreto",
            "Lofzang van Maria",
            "Regina coeli",
            "Wees gegroet Maria",
            "Gebed voor de Heilige Vader",
            "Gebed om priesterroepingen",
            "Gebed tot de Heilige Geest",
            "Uw liefde is groter",
            "Instrument van Uw vrede",
            "Zo klein en toch zo machtig",
            "Zijn naam is Jezus",
            "Hier ben ik",
            "Ware grootheid",
            "Vrede. Gebed op het kerstfeest",
            "Zegenbede",
            "Heb goede moed",
            "Voorbede om hoop",
            "Gebed om in hoop te kunnen leven",
            "Gebed op kerstmis",
            "Gebed om de voorspraak van Maria",
            "Gebed om vertrouwen",
            "Gebed om zegen over een gemeenschap",
            "God alleen voldoet",
            "Gebed van Bernadette",
            "U weet van mijn tranen",
            "Gij hebt ons voor U en elkaar gemaakt",
            "Niet tevergeefs"]
        self._data['items'] = []
        for url,title in zip(urls,titles):
            xpath = "/html/body"
            harvest = getHtml(url, xpath, tree_requested=True)
            self._data['items'].append({
                'key': self._key,
                'name': "Explore Catholic",
                'title': title,
                'url': url,
                'image': harvest[0].xpath('.//div[contains(@class,"media")]/img')[0].get('src'),
                'instagram': "https://www.instagram.com/xplorecatholic/"
            })
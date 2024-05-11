# -*- coding: utf-8 -*-
from collection.data import *
from collection.source import Card


class Sporen(Card):
    def __init__(self):
        self._key = "sporen"
        self._category = "contemplation mp3"
        self._type = "sequence"
        self._data = {
            'index': "https://sporenvangod.nl/Mystiek/Mystieke-citaten-audio/"
        }
        self._template = """
            <div class="item" id="{{item['key']}}">
                <div class="card contemplation mp3">
                    <a target="_blank" href="{{item['url']}}" onclick="document.cookie='{{item['key']}}={{item['url']}}; expires=Fri, 31 Dec 9999 23:59:59 GMT;'">
                        <div class="filled-image">
                            <iframe src="{{item['embed']}}" width="304" height="171" frameborder="0" scrolling="no" allowfullscreen> </iframe>
                        </div>
                        <div class="title">{{item['name']}}</div>
                        <div class="caption">{{item['title']}}</div>
                    </a>
                    <div class="actions">
                        <a target="_blank" onclick="load_card('sporen');">
                            <div class="action-button"></div>
                        </a>
                        <a target="_blank" href="{{data['index']}}">
                            <div class="button">INHOUD</div>
                        </a>
                    </div>
                    <div class="actions">
                        {% set url = my_encode(item['url']) %}
                        {% set title = my_encode(item['title'] + ' via alledaags.gelovenleren.net') %}
                        {% set short_title = my_encode(item['title']) %}
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
        """

    def harvestInit(self):
        sporen = [
            {
                "inleiding": "Een citaat uit 'Samenspraak', een boekje van Claesinne van Nieuwlant. Ophouden met je pogingen om dichterbij God te komen, want dat gaat niet lukken, zegt Claesinne. Maar wat dan wel? Ontbloot worden, zegt ze. Wat betekent dat? Hier hoor je er meer over:",
                "url": "https://soundcloud.com/user-687189612/podcast-claesinne-van-nieuwlant",
                "embedurl": "https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/1354136644&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true"
            },
            {
                "inleiding": "Een citaat van Suster Bertken, een gebed over de 'zoete naam van Jezus'. Waarom toch zo vaak mediteren over het lijden en de pijn van Jezus? Is dat niet een beetje luguber, of zelfs ziekelijk? Of kan het ons van onszelf bevrijden?",
                "url": "https://soundcloud.com/user-687189612/podcastbertken2",
                "embedurl": "https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/1340608609&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true"
            },
            {
                "inleiding": "Een citaat van de blinde mysticus Jean de Saint Samson, met toelichting. God werd mens om de mens goddelijk te maken. Maar hoe dan? Door het spel van de liefde.",
                "url": "https://soundcloud.com/user-687189612/podcast-jean-de-saint-samson",
                "embedurl": "https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/1209844333&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true"
            },
            {
                "inleiding": "Augustinus boek 1, hoe zit dat toch met God? Zit Hij ergens buiten, of ergens binnenin je?",
                "url": "https://soundcloud.com/user-687189612/augustinus-deel-1",
                "embedurl": "https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/1354331275&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true"
            },
            {
                "inleiding": "Augustinus boek 7, over een ontmoeting met God als het hoogste licht en wat hem dat doet",
                "url": "https://soundcloud.com/user-687189612/augustinusdeel2",
                "embedurl": "https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/1354794532&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true"
            },
            {
                "inleiding": "Augustinus boek 10, over het met huid en haar genieten van God",
                "url": "https://soundcloud.com/user-687189612/augustinusdeel3",
                "embedurl": "https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/1354794544&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true"
            },
            {
                "inleiding": "Een citaat van Etty Hillesum, uit haar dagboeken, over hoe het aanvaarden van de dood een verruiming van je leven betekent.",
                "url": "https://soundcloud.com/user-687189612/podcastetty2",
                "embedurl": "https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/987885760&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true"
            },
            {
                "inleiding": "Een citaat van de St. Exupéry, uit de Citadelle, over het grote geschenk van het niet-beantwoorde gebed.",
                "url": "https://soundcloud.com/user-687189612/podcastcitadelle2",
                "embedurl": "https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/987885775&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true"
            },
            {
                "inleiding": "Een citaat van Julian van Norwich, uit haar Visoenen, over waar je echt rust kunt vinden",
                "url": "https://soundcloud.com/user-687189612/podcastjulian",
                "embedurl": "https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/987885754&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true"
            },
            {
                "inleiding": "Een citaat van Dag Hammerskjold, uit Merkstenen, over de spirituele mogelijkheid van je dagelijkse plichten.",
                "url": "https://soundcloud.com/user-687189612/hammerskjold",
                "embedurl": "https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/1354916590&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true"
            },
            {
                "inleiding": "Citaat van Thomas a Kempis, uit de Navolging van Christus, over het eindeloze gebabbel van onze 'social talk'  en mogelijkheid van een écht gesprek.",
                "url": "https://soundcloud.com/user-687189612/podcastnavolging",
                "embedurl": "https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/987885718&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true"
            },
            {
                "inleiding": "Citaat uit de Wolk van niet-weten, over de beperking van het denken als het gaat over de omgang met God.",
                "url": "https://soundcloud.com/user-687189612/podcastwolk",
                "embedurl": "https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/987885697&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true"
            },
            {
                "inleiding": "Citaat uit Berg Karmel, (op een tekening) van Johannes van het Kruis, over hoe het 'niets' en 'alles' samenhangen op de spirituele weg.",
                "url": "https://soundcloud.com/user-687189612/podcastkarmel",
                "embedurl": "https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/987885748&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true"
            },
            {
                "inleiding": "Een citaat van Meester Eckhart, het slot van een preek van hem, over de eigenaardig soort eenheid met God.",
                "url": "https://soundcloud.com/user-687189612/podcasteckhart",
                "embedurl": "https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/987885772&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true"
            },
            {
                "inleiding": "Een citaat van Beatrijs van Nazareth, uit ' De zeven manieren van heilige Minne\", over de buitensporige hartstocht die gepaard kan gaan met de liefde van en tot God.",
                "url": "https://soundcloud.com/user-687189612/podcastbeatrijs",
                "embedurl": "https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/987885793&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true"
            },
            {
                "inleiding": "Een citaat van Martin Buber, uit 'Ik en Jij'. Je kunt over God alleen maar spreken als een  'JIJ' - iemand die jóu aanspreekt.",
                "url": "https://soundcloud.com/user-687189612/podcastbuber",
                "embedurl": "https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/987885778&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true"
            },
            {
                "inleiding": "Een citaat van Evelyn Underhill, uit Praktische mystiek voor nuchtere mensen. Mystiek gaat over de werkelijkheid - niet over al die beelden in je hoofd waarvan je dénkt dat het de werkelijkheid is.",
                "url": "https://soundcloud.com/user-687189612/podcastunderhill",
                "embedurl": "https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/987885709&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true"
            },
            {
                "inleiding": "Een citaat van Suster Bertken, een middeleeuwse kluizenares uit Utrecht, die minneliedjes over God schreef. Over het vonkje van je ziel.",
                "url": "https://soundcloud.com/user-687189612/podcastbertken",
                "embedurl": "https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/987885790&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true"
            },
            {
                "inleiding": "Een citaat van Willem de St. Thierry, uit zijn commentaar op het Hooglied, hoe de lichamelijke liefde de trekkracht van de geestelijke liefde in zich draagt.",
                "url": "https://soundcloud.com/user-687189612/podcaststthierry",
                "embedurl": "https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/987885715&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true"
            },
            {
                "inleiding": "Een citaat van Thérèse van Lisieux, uit haar autobiografie 'Geschiedenis van een ziel', over een 'lift naar God'.",
                "url": "https://soundcloud.com/user-687189612/podcastlisieux",
                "embedurl": "https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/987885739&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true"
            },
            {
                "inleiding": "Een citaat van Hein Blommestijn, uit een artikel in Speling (1993), over waarom een mens alleen van God moet houden.",
                "url": "https://soundcloud.com/user-687189612/podcastblommestijn",
                "embedurl": "https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/987885787&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true"
            },
            {
                "inleiding": "Een citaat van Mechtild van Hackenborg, uit haar biografie 'Boek van bijzondere genade', door Geertruid van Helfta, over het geheim van het hart van Jezus.",
                "url": "https://soundcloud.com/user-687189612/podcastmechtild",
                "embedurl": "https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/987885730&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true"
            }
        ]
        self._data['items'] = [
            {
                'title': item['inleiding'],
                'url': item['url'],
                'embed': item['embedurl'],
                'name': "Sporen van God",
                'image': "/var/sporenvangod.png",
                'key': self._key
            }
            for item in sporen
        ]

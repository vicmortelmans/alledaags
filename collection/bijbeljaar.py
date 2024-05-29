from collection.data import *
from collection.source import Card
from datetime import date, datetime, time, timedelta


class BijbelJaar(Card):
    def __init__(self):
        self._key = "bijbeljaar"
        self._category = "bible"
        self._type = "daily"
        self._data = {}
        self._template = """
            <div class="item" id="bijbeljaar">
                <div class="card bible">
                    <a target="_blank" href="{{data['url']}}" onclick="document.cookie='bijbeljaar={{data['url']}}; expires=Fri, 31 Dec 9999 23:59:59 GMT;'">
                        <div class="filled-image">
                            <img src="{{data['image']}}"/>
                        </div>
                        <div class="title">{{data['name']}}</div>
                        {% if data['section'] %}<div class="caption">{{data['section']}}</div>{% endif %}
                        <div class="text">{{data['title']}}</div>
                    </a>
                    <div class="actions">
                        <a target="_blank" href="{{data['index']}}">
                            <div class="button">INHOUD</div>
                        </a>
                    </div>
                    <div class="actions">
                        {% set url = my_encode(data['url']) %}
                        {% set title = my_encode("Bible in One Year: " + data['title'] + ' via alledaags.gelovenleren.net') %}
                        {% set short_title = my_encode("Bible in One Year: " + data['title']) %}
                        {% set image = my_encode(data['image']) %}
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

    def harvestSync(self):
        list = {
          "31/12": {
            "title": "Beginnen en eindigen",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=1728efbda81692282ba642aafd57be3a.611&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "30/12": {
            "title": "De bruid",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=8eefcfdf5990e441f0fb6f3fad709e21.610&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "29/12": {
            "title": "Jouw kroon komt eraan",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=4e4b5fbbbb602b6d35bea8460aa8f8e5.609&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "28/12": {
            "title": "Het verbond van liefde",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=58ae749f25eded36f486bc85feb3f0ab.608&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "27/12": {
            "title": "Halleluja",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=a9a6653e48976138166de32772b1bf40.607&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "26/12": {
            "title": "Met geld omgaan",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=3a0772443a0739141292a5429b952fe6.606&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "25/12": {
            "title": "Waarom Kerstmis?",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=1bb91f73e9d31ea2830a5e73ce3ed328.605&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "24/12": {
            "title": "Kijk omhoog",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=6e2713a6efee97bacb63e52c54f0ada0.604&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "23/12": {
            "title": "Jouw hoopvolle woorden voor iedereen",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=11b921ef080f7736089c757404650e40.603&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "22/12": {
            "title": "Zuiverheid en kracht",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=15de21c670ae7c3f6f3f1f37029303c9.602&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "21/12": {
            "title": "Gods hand rust op jou",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=5e388103a391daabe3de1d76a6739ccd.601&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "20/12": {
            "title": "Drie manieren om het kwaad te overwinnen",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=97e8527feaf77a97fc38f34216141515.591&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "19/12": {
            "title": "Je Koning",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=81448138f5f163ccdba4acc69819f280.590&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "18/12": {
            "title": "Zo eer je de Heer",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=7dcd340d84f762eba80aa538b0c527f7.589&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "17/12": {
            "title": "De Bijbel lezen en begrijpen",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=16c222aa19898e5058938167c8ab6c57.588&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "16/12": {
            "title": "Wie is de Heer van je leven?",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=9b72e31dac81715466cd580a448cf823.587&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "15/12": {
            "title": "Wat speelt zich af achter de schermen van de geschiedenis?",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=5737034557ef5b8c02c0e46513b98f90.586&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "14/12": {
            "title": "De leeuw en het lam",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=7bcdf75ad237b8e02e301f4091fb6bc8.585&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "13/12": {
            "title": "Feestvieren",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=5ea1649a31336092c05438df996a3e59.584&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "12/12": {
            "title": "De voordelen van terechtwijzingen",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=65658fde58ab3c2b6e5132a39fae7cb9.583&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "11/12": {
            "title": "Jij kunt van invloed zijn",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=33e8075e9970de0cfea955afd4644bb2.582&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "10/12": {
            "title": "Jezus vinden",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=c399862d3b9d6b76c8436e924a68c45b.581&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "09/12": {
            "title": "Onthullende openbaring",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=df877f3865752637daa540ea9cbc474f.580&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "08/12": {
            "title": "Smachten",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=298f95e1bf9136124592c8d4825a06fc.579&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "07/12": {
            "title": "Heeft God echt alles in de hand?",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=0fcbc61acd0479dc77e3cccc0f5ffca7.578&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "06/12": {
            "title": "Je evenwicht vinden",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=d64a340bcb633f536d56e51874281454.577&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "05/12": {
            "title": "Gods doel voor jou",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=37f0e884fbad9667e38940169d0a3c95.576&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "04/12": {
            "title": "Vier remedies tegen angst",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=f4be00279ee2e0a53eafdaa94a151e2c.575&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "03/12": {
            "title": "Heb vertrouwen",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=13f320e7b5ead1024ac95c3b208610db.574&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "02/12": {
            "title": "Van visie naar actie",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=2d6cc4b2d139a53512fb8cbb3086ae2e.552&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "01/12": {
            "title": "Zo voorkom je geestelijke besmetting",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=ff4d5fbbafdf976cfdc032e3bde78de5.551&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "30/11": {
            "title": "Intieme banden",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=e8c0653fea13f91bf3c48159f7c24f78.550&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "29/11": {
            "title": "Gods perfecte tijd",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=b337e84de8752b27eda3a12363109e80.549&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "28/11": {
            "title": "Laat je inspireren",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=285e19f20beded7d215102b49d5c09a0.548&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "27/11": {
            "title": "God bestaat en Hij is groot",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=b5b41fac0361d157d9673ecb926af5ae.547&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "26/11": {
            "title": "Gods grote goedheid en genade",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=5b69b9cb83065d403869739ae7f0995e.546&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "25/11": {
            "title": "Weten wanneer je moet knielen",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=cee631121c2ec9232f3a2f028ad5c89b.545&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "24/11": {
            "title": "Jouw voorbeeld",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=3cf166c6b73f030b4f67eeaeba301103.544&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "23/11": {
            "title": "Waar is God?",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=05f971b5ec196b8c65b75d2ef8267331.543&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "22/11": {
            "title": "Geestelijk volwassen worden",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=7380ad8a673226ae47fce7bff88e9c33.542&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "21/11": {
            "title": "Bidden met kracht",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=b534ba68236ba543ae44b22bd110a1d6.541&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "20/11": {
            "title": "Je kunt je verzetten tegen het kwaad",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=35051070e572e47d2c26c241ab88307f.540&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "19/11": {
            "title": "Goddelijke verbindingen",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=1be3bc32e6564055d5ca3e5a354acbef.539&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "18/11": {
            "title": "Hoe moeten we vandaag leven?",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=2f55707d4193dc27118a0f19a1985716.538&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "17/11": {
            "title": "Vijf elementen van het leven van een christen",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=55a7cf9c71f1c9c495413f934dd1a158.537&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "16/11": {
            "title": "Acht kenmerken van een christelijke gemeenschap",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=559cb990c9dffd8675f6bc2186971dc2.536&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "15/11": {
            "title": "God aanbidden: waarom en hoe",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=218a0aefd1d1a4be65601cc6ddc1520e.530&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "14/11": {
            "title": "De wedstrijd die voor je ligt",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=e1e32e235eee1f970470a3a6658dfdd5.528&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "13/11": {
            "title": "Drie keer geloof in de praktijk",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=f770b62bc8f42a0b66751fe636fc6eb0.527&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "12/11": {
            "title": "Wat is geloof?",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=9461cce28ebe3e76fb4b931c35a169b0.526&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "11/11": {
            "title": "Hou vol",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=6ea2ef7311b482724a9b7b0bc0dd85c6.525&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "10/11": {
            "title": "Jouw onweerstaanbare schoonheid",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=d18f655c3fce66ca401d5f38b48c89af.524&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "09/11": {
            "title": "Voor eens en altijd",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=cfee398643cbc3dc5eefc89334cacdc1.523&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "08/11": {
            "title": "Jouw bloeddonor",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=74071a673307ca7459bcf75fbd024e09.522&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "07/11": {
            "title": "De remedie voor eenzaamheid",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=598b3e71ec378bd83e0a727608b5db01.521&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "06/11": {
            "title": "Jij hebt toegang tot God",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=5ef0b4eba35ab2d6180b0bca7e46b6f9.520&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "05/11": {
            "title": "Gods beloften",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=25ddc0f8c9d3e22e03d3076f98d83cb2.519&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "04/11": {
            "title": "Waarschuwingen",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=2050e03ca119580f74cca14cc6e97462.518&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "03/11": {
            "title": "Naar God toe gaan",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=ef575e8837d065a1683c022d2077d342.517&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "02/11": {
            "title": "Beslissingen die je leven bepalen",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=8e6b42f1644ecb1327dc03ab345e618b.516&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "01/11": {
            "title": "Richt je aandacht",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=26337353b7962f533d78c762373b3318.515&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "31/10": {
            "title": "Het verrassende geheim van vrijheid",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=877a9ba7a98f75b90a9d49f53f15a858.513&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "30/10": {
            "title": "De sleutel tot het leven",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=ab817c9349cf9c4f6877e1894a1faa00.512&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "29/10": {
            "title": "Nieuwe kracht voor je geest, je hart en je ziel",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=e836d813fd184325132fca8edcdfb40e.511&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "28/10": {
            "title": "Goede dingen doen",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=68ce199ec2c5517597ce0a4d89620f55.510&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "27/10": {
            "title": "Uitdagende tegenstrijdigheden",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=f1b6f2857fb6d44dd73c7041e0aa0f19.509&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "26/10": {
            "title": "Als het nog niet goed is gekomen, is het nog niet het einde",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=428fca9bc1921c25c5121f9da7815cde.508&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "25/10": {
            "title": "Je kostbaarste bezit",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=51d92be1c60d1db1d2e5e7a07da55b26.507&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "24/10": {
            "title": "Zo spreekt God tegen je",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=0353ab4cbed5beae847a7ff6e220b5cf.506&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "23/10": {
            "title": "Vijfentwintig manieren om nuttig te zijn voor God",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=98b297950041a42470269d56260243a1.505&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "22/10": {
            "title": "Je belangrijkste taak",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=7fe1f8abaad094e0b5cb1b01d712f708.504&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "21/10": {
            "title": "Tevreden leven",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=15d4e891d784977cacbfcbb00c48f133.486&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "20/10": {
            "title": "Zware tijden",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=a8abb4bb284b5b27aa7cb790dc20f80b.485&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "19/10": {
            "title": "Woorden, het Woord van God en ‘woorden’",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=eed5af6add95a9a6f1252739b1ad8c24.484&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "18/10": {
            "title": "Het leven van een leider",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=1651cf0d2f737d7adeab84d339dbabd3.483&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "17/10": {
            "title": "Hoe moet je bidden?",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=fccb60fb512d13df5083790d64c4d5dd.482&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "16/10": {
            "title": "De belangrijkste beslissing van mijn leven",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=2421fcb1263b9530df88f7f002e78ea5.481&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "15/10": {
            "title": "Het goede doen",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=ddb30680a691d157187ee1cf9e896d03.480&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "14/10": {
            "title": "Niet in oude gewoonten vervallen",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=a49e9411d64ff53eccfdd09ad10a15b3.479&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "13/10": {
            "title": "Gods goede plannen voor jouw toekomst",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=019d385eb67632a7e958e23f24bd07d7.478&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "12/10": {
            "title": "Durf anders te zijn",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=f74909ace68e51891440e4da0b65a70c.475&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "11/10": {
            "title": "Meer",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=8d7d8ee069cb0cbbf816bbb65d56947e.473&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "10/10": {
            "title": "Verrast door vreugde",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=25b2822c2f5a3230abfadd476e8b04c9.470&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "09/10": {
            "title": "Woorden die levens veranderen",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=b6f0479ae87d244975439c6124592772.465&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "08/10": {
            "title": "De Heer verheerlijken als we verliezen",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=7eacb532570ff6858afd2723755ff790.464&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "07/10": {
            "title": "Nieuwe kleren",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=d1f255a373a3cef72e03aa9d980c7eca.463&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "06/10": {
            "title": "Kan een panter zijn vlekken veranderen?",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=41ae36ecb9b3eee609d05b90c14222fb.462&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "05/10": {
            "title": "Wat is de zin van het leven?",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=8fe0093bb30d6f8c31474bd0764e6ac0.461&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "04/10": {
            "title": "Een dankbare houding",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=42e7aaa88b48137a16a1acd04ed91125.460&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "03/10": {
            "title": "Zo word je een tevreden mens",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=66808e327dc79d135ba18e051673d906.459&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "02/10": {
            "title": "Goddelijke ambitie",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=0deb1c54814305ca9ad266f53bc82511.458&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "01/10": {
            "title": "Zo ben je een bron van zegen",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=0d0fd7c6e093f7b804fa0150b875b868.453&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "30/09": {
            "title": "Ere wie ere toekomt",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=f4f6dce2f3a0f9dada0c2b5b66452017.452&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "29/09": {
            "title": "Een leven dat het leven waard is",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=8cb22bdd0b7ba1ab13d742e22eed8da2.451&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "28/09": {
            "title": "Zeven gewoontes die je leven veranderen",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=bbcbff5c1f1ded46c25d28119a85c6c2.450&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "27/09": {
            "title": "Zeven manieren om de Heer blij te maken",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=4f4adcbf8c6f66dcfc8a3282ac2bf10a.449&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "26/09": {
            "title": "Zes factoren die goede relaties bevorderen",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=bbf94b34eb32268ada57a3be5062fe7d.448&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "25/09": {
            "title": "Leven in de kracht van de Geest",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=18d8042386b79e2c279fd162df0205c8.445&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "24/09": {
            "title": "Ontdek dit geheim",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=69cb3ea317a32c4e6143e665fdb20b14.447&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "23/09": {
            "title": "Wat heeft Jezus veranderd?",
            "url": "f=\"https://alphanl.activehosted.com/index.php?action=social&chash=352fe25daf686bdb4edca223c921acea.444&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "22/09": {
            "title": "Weet hoe waardevol je bent",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=b7b16ecf8ca53723593894116071700c.443&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "21/09": {
            "title": "Geef nooit op",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=f8c1f23d6a8d8d7904fc0ea8e066b3bb.441&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "20/09": {
            "title": "Omgaan met conflicten",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=1543843a4723ed2ab08e18053ae6dc5b.440&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "19/09": {
            "title": "Blijf niet gevangen in je verleden",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=28f0b864598a1291557bed248a998d4e.439&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "18/09": {
            "title": "God is aardig en Hij vindt jou aardig",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=70c639df5e30bdee440e4cdf599fec2b.438&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "17/09": {
            "title": "De beste manier om leiding te geven",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=f73b76ce8949fe29bf2a537cfa420e8f.437&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "16/09": {
            "title": "God houdt van mensen met tekortkomingen",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=5a4b25aaed25c2ee1b74de72dc03c14e.436&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "15/09": {
            "title": "Omgaan met onverwachte problemen",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=a01a0380ca3c61428c26a231f0e49a09.435&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "14/09": {
            "title": "Ben je gered?",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=c86a7ee3d8ef0b551ed58e354a836f2b.434&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "13/09": {
            "title": "Jezus Christus woont in jou",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=d9fc5b73a8d78fad3d6dffe419384e70.433&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "12/09": {
            "title": "Op Gods wegen blijven",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=8efb100a295c0c690931222ff4467bb8.432&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "11/09": {
            "title": "Je hebt niet meer nodig dan zijn genade",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=39461a19e9eddfb385ea76b26521ea48.431&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "10/09": {
            "title": "Vrede in donkere tijden",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=dc912a253d1e9ba40e2c597ed2376640.430&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "09/09": {
            "title": "Jezus kennen en liefhebben",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=0584ce565c824b7b7f50282d9a19945b.429&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "08/09": {
            "title": "De geestelijke strijd winnen",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=beed13602b9b0e6ecb5b568ff5058f07.428&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "07/09": {
            "title": "Tien redenen om gul te geven",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=4f6ffe13a5d75b2d6a3923922b3922e5.427&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "06/09": {
            "title": "Je Heer liefhebben",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=00ec53c4682d36f5c4359f4ae7bd7ba1.426&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "05/09": {
            "title": "Gods belofte aan gulle mensen",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=bca82e41ee7b0833588399b1fcd177c7.425&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "04/09": {
            "title": "Hoe kun jij nuttig zijn voor God?",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=a02ffd91ece5e7efeb46db8f10a74059.424&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "03/09": {
            "title": "Jouw leven kan vruchtbaar zijn",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=8bf1211fd4b7b94528899de0a43b9fb3.423&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "02/09": {
            "title": "Erken wie je bent",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=d34ab169b70c9dcd35e62896010cd9ff.422&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "01/09": {
            "title": "Jouw levensdoel",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=142949df56ea8ae0be8b5306971900a4.421&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "31/08": {
            "title": "Houd je blik gericht op de Onzichtbare",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=f61d6947467ccd3aa5af24db320235dd.420&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "30/08": {
            "title": "Een spirituele facelift",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=ad972f10e0800b49d76fed33a21f6698.419&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "29/08": {
            "title": "Als de Heilige Geest komt",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=05049e90fa4f5039a8cadc6acbb4b2cc.412&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "28/08": {
            "title": "Rechtvaardige liefde",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=9be40cee5b0eee1462c82c6964087ff9.410&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "27/08": {
            "title": "Door God gezalfd",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=bac9162b47c56fc8a4d2a519803d51b3.409&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "26/08": {
            "title": "Gods weldaden",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=00411460f7c92d2124a67ea0f4cb5f85.408&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "25/08": {
            "title": "Het gezin",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=c3e878e27f52e2a57ace4d9a76fd9acf.407&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "24/08": {
            "title": "Overwinning",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=52720e003547c70561bf5e03b95aa99f.406&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "23/08": {
            "title": "Vertrouw erop dat God het op zijn manier doet",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=e7b24b112a44fdd9ee93bdf998c6ca0e.405&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "22/08": {
            "title": "Volhouders",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=c058f544c737782deacefa532d9add4c.404&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "21/08": {
            "title": "Vrede vinden en bewaren",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=b2f627fff19fda463cb386442eac2b3d.644&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "20/08": {
            "title": "Luisteren naar de Heilige Geest",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=aa942ab2bfa6ebda4840e7360ce6e7ef.403&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "19/08": {
            "title": "Zestien kenmerken van de liefde",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=fb7b9ffa5462084c5f4e7e85a093e6d7.402&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "18/08": {
            "title": "Intieme relaties",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=6c524f9d5d7027454a783c841250ba71.401&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "17/08": {
            "title": "Genieten van God",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=7895fc13088ee37f511913bac71fa66f.1438&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "16/08": {
            "title": "Beter worden",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=8dd48d6a2e2cad213179a3992c0be53c.399&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "15/08": {
            "title": "Je best doen",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=138bb0696595b338afbab333c555292a.398&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "14/08": {
            "title": "Je invloed gebruiken ten goede",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=371bce7dc83817b7893bcdeed13799b5.397&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "13/08": {
            "title": "Wat je moet weten",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=efe937780e95574250dabe07151bdc23.396&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "12/08": {
            "title": "Genieten van het leven ondanks de moeilijkheden",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=b3967a0e938dc2a6340e258630febd5a.380&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "11/08": {
            "title": "Angst en rust",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=3ad7c2ebb96fcba7cda0cf54a2e802f5.379&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "10/08": {
            "title": "Gods oordeel en dat van ons",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=58238e9ae2dd305d79c2ebc8c1883422.378&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "09/08": {
            "title": "Echt succes",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=3dd48ab31d016ffcbf3314df2b3cb9ce.377&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "08/08": {
            "title": "Geld: zegen of vloek?",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=40008b9a5380fcacce3976bf7c08af5b.376&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "07/08": {
            "title": "Drie slechte houdingen tot verdeeldheid leiden",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=04025959b191f8f9de3f924f0940515f.375&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "06/08": {
            "title": "God is bij je",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=819f46e52c25763a55cc642422644317.374&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "05/08": {
            "title": "Hij geeft je kracht",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=357a6fdf7642bf815a88822c447d9dc4.373&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "04/08": {
            "title": "Eenheid",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=6855456e2fe46a9d49d3d3af4f57443d.372&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "03/08": {
            "title": "Werken zonder te verwelken",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=f9b902fc3289af4dd08de5d1de54f68f.371&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "02/08": {
            "title": "De Heer is bij je",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=2f2b265625d76a6704b08093c652fd79.370&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "01/08": {
            "title": "Mensen hoop geven",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=310dcbbf4cce62f762a2aaa148d556bd.369&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "31/07": {
            "title": "Een einde aan ruzies, meningsverschillen en strijd",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=c042f4db68f23406c6cecf84a7ebb0fe.368&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "30/07": {
            "title": "Goed burgerschap",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=6da37dd3139aa4d9aa55b8d237ec5d4a.367&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "29/07": {
            "title": "Vier offers die God een plezier doen",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=fe73f687e5bc5280214e0486b273a5f9.366&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "28/07": {
            "title": "Je roeping is onherroepelijk",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=6faa8040da20ef399b63a72d0e4ab575.365&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "27/07": {
            "title": "Je hebt het in je",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=cd00692c3bfe59267d5ecfac5310286c.364&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "26/07": {
            "title": "Je stamboom",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=b83aac23b9528732c23cc7352950e880.363&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "25/07": {
            "title": "Hoe zit het met mensen die niet geloven?",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=a666587afda6e89aec274a3657558a27.362&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "24/07": {
            "title": "Een kussen om ons moede hoofd te ruste te leggen",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=f2fc990265c712c49d51a18a32b39f0c.360&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "23/07": {
            "title": "Weet wie je bent",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=5737c6ec2e0716f3d8a7a5c4e0de0d9a.358&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "22/07": {
            "title": "Heer, help!",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=caf1a3dfb505ffed0d024130f58c5cfa.357&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "21/07": {
            "title": "De uitgang van de doolhof",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=320722549d1751cf3f247855f937b982.356&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "20/07": {
            "title": "Geniet van je nieuwe leven",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=8d3bba7425e7c98c50f52ca1b52d3735.355&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "19/07": {
            "title": "Alleen maar genade ",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=432aca3a1e345e339f35a30c8f65edce.354&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "18/07": {
            "title": "Zo voel je Gods liefde voor jou",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=5b8add2a5d98b1a652ea7fd72d942dac.353&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "17/07": {
            "title": "Alsof je nooit iets verkeerd hebt gedaan",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=3fe94a002317b5f9259f82690aeea4cd.352&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "16/07": {
            "title": "Gods antwoord dat alles verandert",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=ad13a2a07ca4b7642959dc0c4c740ab6.351&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "15/07": {
            "title": "Een zacht hart en harde voeten",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=758874998f5bd0c393da094e1967a72b.350&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "14/07": {
            "title": "God van de nieuwe kans",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=158f3069a435b314a80bdcb024f8e422.349&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "13/07": {
            "title": "Hoe aanbid je God",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=9dfcd5e558dfa04aaf37f137a1d9d3e5.347&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "12/07": {
            "title": "Je relaties herstellen",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=06eb61b839a0cefee4967c67ccb099dc.346&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "11/07": {
            "title": "Je woorden hebben kracht",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=eddea82ad2755b24c4e168c5fc2ebd40.345&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "10/07": {
            "title": "Onzichtbaar maar van onschatbare waarde",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=a8c88a0055f636e4a163a5e3d16adab7.344&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "09/07": {
            "title": "Vertrouw op de Heer",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=8e98d81f8217304975ccb23337bb5761.343&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "08/07": {
            "title": "Luister naar God",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=b2eb7349035754953b57a32e2841bda5.342&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "07/07": {
            "title": "Het gevaar van hoogmoed",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=496e05e1aea0a9c4655800e8a7b9ea28.341&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "06/07": {
            "title": "Omgaan met de uitdagingen van het leven",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=37bc2f75bf1bcfe8450a1a41c200364c.340&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "05/07": {
            "title": "Het licht van God schijnt op jou",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=11b9842e0a271ff252c1903e7132cd68.339&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "04/07": {
            "title": "God keert tegenslag ten goede",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=577bcc914f9e55d5e4e4f82f9f00e7d4.338&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "03/07": {
            "title": "Gods doelen voor jou",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=34ed066df378efacc9b924ec161e7639.337&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "02/07": {
            "title": "Transformeer je wereld",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=94f6d7e04a4d452035300f18b984988c.336&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "01/07": {
            "title": "Zeven kenmerken van de goede leiders",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=ef0d3930a7b6c95bd2b32ed45989c61f.335&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "30/06": {
            "title": "De krachtigste boodschap die er bestaat",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=26e359e83860db1d11b6acca57d8ea88.334&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "29/06": {
            "title": "Je leven plannen",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=9fd81843ad7f202f26c1a174c7357585.333&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "28/06": {
            "title": "Krachtmetingen",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=d296c101daa88a51f6ca8cfc1ac79b50.332&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "27/06": {
            "title": "De God die wonderen doet",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=6883966fd8f918a4aa29be29d2c386fb.330&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "26/06": {
            "title": "Drie dingen die God je wil geven",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=53c3bce66e43be4f209556518c2fcb54.329&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "25/06": {
            "title": "De kracht van gebed",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=1700002963a49da13542e0726b7bb758.328&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "24/06": {
            "title": "Geef het stokje door",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=9c838d2e45b2ad1094d42f4ef36764f6.327&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "23/06": {
            "title": "Drie dingen die onmisbaar zijn voor een goede vriendschap",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=f90f2aca5c640289d0a29417bcb63a37.326&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "22/06": {
            "title": "Het leven van een christen is niet makkelijk",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=839ab46820b524afda05122893c2fe8e.325&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "21/06": {
            "title": "God ziet je hart",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=48aedb8880cab8c45637abc7493ecddd.324&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "20/06": {
            "title": "Kom Heilige Geest",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=918317b57931b6b7a7d29490fe5ec9f9.323&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "19/06": {
            "title": "Onuitputtelijke schatten",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=16a5cdae362b8d27a1d8f8c7b78b4330.322&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "18/06": {
            "title": "Drie bekeringen die iedereen nodig heeft",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=82cec96096d4281b7c95cd7e74623496.400&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "17/06": {
            "title": "Bidden heeft zin",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=0e01938fc48a2cfb5f2217fbfb00722d.321&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "16/06": {
            "title": "God volgen en niet tegenwerken",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=46ba9f2a6976570b0353203ec4474217.320&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "15/06": {
            "title": "Als je God niet begrijpt",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=0f49c89d1e7298bb9930789c8ed59d48.319&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "14/06": {
            "title": "Ruimte",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=6a9aeddfc689c1d0e3b9ccc3ab651bc5.318&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "13/06": {
            "title": "De maatschappij kan veranderen",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=8c19f571e251e61cb8dd3612f26d5ecf.299&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "12/06": {
            "title": "Je kunt veranderen",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=36660e59856b4de58a219bcf4e27eba3.298&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "11/06": {
            "title": "God gebruikt zelfs je fouten",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=b1a59b315fc9a3002ce38bbe070ec3f5.297&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "10/06": {
            "title": "Zorgen hebben niet het laatste woord",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=cfa0860e83a4c3a763a7e62d825349f7.295&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "09/06": {
            "title": "Wees loyaal",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=502e4a16930e414107ee22b6198c578f.294&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "08/06": {
            "title": "Geen grijstinten",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=d96409bf894217686ba124d7356686c9.293&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "07/06": {
            "title": "Beproeving en verleiding",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=f718499c1c8cef6730f9fd03c8125cab.292&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "06/06": {
            "title": "Barmhartigheid",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=fe131d7f5a6b38b23cc967316c13dae2.291&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "05/06": {
            "title": "Hij geeft je kracht",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=c52f1bd66cc19d05628bd8bf27af3ad6.290&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "04/06": {
            "title": "Hemelse geluiden",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=c24cd76e1ce41366a4bbe8a49b02a028.289&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "03/06": {
            "title": "Zelfs je zwakheid wordt gezalfd",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=03c6b06952c750899bb03d998e631860.288&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "02/06": {
            "title": "Waanzinnige liefde",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=6c9882bbac1c7093bd25041881277658.286&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "01/06": {
            "title": "Wow!",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=077e29b11be80ab57e1a2ecabb7da330.285&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "31/05": {
            "title": "Jij hebt Gods energie",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=621bf66ddb7c962aa0d22ac97d69b793.284&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "30/05": {
            "title": "Beproeving wordt overwinning",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=3cec07e9ba5f5bb252d13f5f431e4bbb.283&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "29/05": {
            "title": "Vijf lasten die je niet hoeft te dragen",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=38db3aed920cf82ab059bfccbd02be6a.282&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "28/05": {
            "title": "Reageren op conflicten",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=0266e33d3f546cb5436a10798e657d97.281&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "27/05": {
            "title": "De kracht van eenheid",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=9188905e74c28e489b44e954ec0b9bca.280&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "26/05": {
            "title": "De naam van de Heer",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=cb70ab375662576bd1ac5aaf16b3fca4.279&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "25/05": {
            "title": "De strijd aanbinden met reuzen",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=e4a6222cdb5b34375400904f03d8e6a5.278&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "24/05": {
            "title": "Dingen tot een goed einde brengen",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=577ef1154f3240ad5b9b413aa7346a1e.269&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "23/05": {
            "title": "De liefde van je leven",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=e165421110ba03099a1c0393373c5b43.267&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "22/05": {
            "title": "Tijd voor een feestje",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=be83ab3ecd0db773eb2dc1b0a17836a1.266&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "21/05": {
            "title": "Goed bestuur?",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=9b04d152845ec0a378394003c96da594.265&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "20/05": {
            "title": "Hoe vind je rust bij tegenspoed?",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=6da9003b743b65f4c0ccd295cc484e57.264&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "19/05": {
            "title": "Je hoop in moeilijke tijden",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=57aeee35c98205091e18d1140e9f38cf.263&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "18/05": {
            "title": "Verzadig je ziel",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=74db120f0a8e5646ef5a30154e9f6deb.262&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "17/05": {
            "title": "God kennen als een vader",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=705f2172834666788607efbfca35afb3.261&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "16/05": {
            "title": "Jouw verhaal heeft kracht",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=3937230de3c8041e4da6ac3246a888e8.2111&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "15/05": {
            "title": "Alles wat Hij wil, ben jij",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=4ba3c163cd1efd4c14e3a415fa0a3010.2110&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "14/05": {
            "title": "Met God is het mogelijk",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=bdc4626aa1d1df8e14d80d345b2a442d.2109&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "13/05": {
            "title": "Omgaan met wanhopige situaties",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=51174add1c52758f33d414ceaf3fe6ba.2108&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "12/05": {
            "title": "De geweldige Heilige Geest",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=b2ab001909a8a6f04b51920306046ce5.2087&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "11/05": {
            "title": "Onuitputtelijke energie, grenzeloze kracht",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=801272ee79cfde7fa5960571fee36b9b.2086&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "10/05": {
            "title": "God verandert je zwakheid in kracht",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=0b1ec366924b26fc98fa7b71a9c249cf.2085&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "09/05": {
            "title": "Zo oogst je veel meer dan je zaait",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=26f5bd4aa64fdadf96152ca6e6408068.2084&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "08/05": {
            "title": "Leven in HD",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=bf424cb7b0dea050a42b9739eb261a3a.2083&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "07/05": {
            "title": "Twaalf manieren om nuttig te zijn voor God",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=d3a7f48c12e697d50c8a7ae7684644ef.2082&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "06/05": {
            "title": "Gebeden tot God",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=4d6b3e38b952600251ee92fe603170ff.2081&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "05/05": {
            "title": "Jezus verlost altijd",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=f80ff32e08a25270b5f252ce39522f72.2080&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "04/05": {
            "title": "Drie manieren om je wereld te transformeren",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=e0a209539d1e74ab9fe46b9e01a19a97.2079&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "03/05": {
            "title": "Goede keuzes maken",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=a088ea2078cd92b0b8a0e78a32c5c082.2078&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "02/05": {
            "title": "Omgaan met confrontaties",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=3e9e39fed3b8369ed940f52cf300cf88.2077&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "01/05": {
            "title": "God wil je verrassen",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=850af92f8d9903e7a4e0559a98ecc857.2076&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "30/04": {
            "title": "Het is al van jou",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=654ad60ebd1ae29cedc37da04b6b0672.2073&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "29/04": {
            "title": "De strijd van vandaag speelt zich af rondom Jezus",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=f410588e48dc83f2822a880a68f78923.2072&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "28/04": {
            "title": "Het is niet voorbij",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=819e3d6c1381eac87c17617e5165f38c.2071&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "27/04": {
            "title": "Leven in overwinning",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=6492d38d732122c58b44e3fdc3e9e9f3.2070&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "26/04": {
            "title": "Goede relaties",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=cbef46321026d8404bc3216d4774c8a9.2069&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "25/04": {
            "title": "U gaat vol liefde in onze plaats",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=1f4fe6a4411edc2ff625888b4093e917.2068&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "24/04": {
            "title": "Twee manieren van leven",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=4b86abe48d358ecf194c56c69108433e.2067&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "23/04": {
            "title": "Gods barmhartige hand",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=07cb5f86508f146774a2fac4373a8e50.2066&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "22/04": {
            "title": "Je woorden hebben veel kracht",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=fb2e203234df6dee15934e448ee88971.2065&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "21/04": {
            "title": "Hallo God!",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=6f4920ea25403ec77bee9efce43ea25e.2060&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "20/04": {
            "title": "Vijf manieren waarop God je leidt",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=0ae3f79a30234b6c45a6f7d298ba1310.2059&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "19/04": {
            "title": "Gods strategische plan",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=f8bf09f5fceaea80e1f864a1b48938bf.2058&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "18/04": {
            "title": "Het is nooit te laat",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=16ba72172e6a4f1de54d11ab6967e371.2057&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "17/04": {
            "title": "Zes stappen om God centraal te stellen in je leven",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=2d405b367158e3f12d7c1e31a96b3af3.2056&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "16/04": {
            "title": "Zijn aanwezigheid",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=52dbb0686f8bd0c0c757acf716e28ec0.2055&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "15/04": {
            "title": "Kiezen wat je onthoudt",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=f8c0c968632845cd133308b1a494967f.2054&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "14/04": {
            "title": "Maak niet dezelfde fout als de bouwers van de Titanic",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=06b1338ba02add2b5d2da67663b19ebe.2045&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "13/04": {
            "title": "Wie en hoe is God?",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=051928341be67dcba03f0e04104d9047.2044&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "12/04": {
            "title": "Jouw uitnodiging",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=a501bebf79d570651ff601788ea9d16d.2043&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "11/04": {
            "title": "Acht dingen die God echt belangrijk vindt",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=3875115bacc48cca24ac51ee4b0e7975.2042&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "10/04": {
            "title": "Zeven manieren om te groeien in wijsheid",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=0189caa552598b845b29b17a427692d1.2041&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "09/04": {
            "title": "Zie zijn goedheid",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=d8330f857a17c53d217014ee776bfd50.2040&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "08/04": {
            "title": "Stoppen met je zorgen maken",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=d79c6256b9bdac53a55801a066b70da3.2039&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "07/04": {
            "title": "Liefhebben van binnenuit",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=4c144c47ecba6f8318128703ca9e2601.2036&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "06/04": {
            "title": "Hou vol",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=a48564053b3c7b54800246348c7fa4a0.2035&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "05/04": {
            "title": "Er is maar één ding nodig",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=2557911c1bf75c2b643afb4ecbfc8ec2.2034&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "04/04": {
            "title": "Geen zegen zonder strijd",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=23d2e1578544b172cca332ff74bddf5f.2033&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "03/04": {
            "title": "Liefhebben",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=f48c04ffab49ff0e5d1176244fdfb65c.2032&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "02/04": {
            "title": "Het is allemaal voor jou",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=2b0f658cbffd284984fb11d90254081f.2031&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "01/04": {
            "title": "Volg Jezus",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=d198bd736a97e7cecfdf8f4f2027ef80.2030&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "31/03": {
            "title": "Zo kun je je angst overwinnen",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=2d579dc29360d8bbfbb4aa541de5afa9.2026&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "30/03": {
            "title": "Een honderdvoudige opbrengst",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=093b60fd0557804c8ba0cbf1453da22f.2025&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "29/03": {
            "title": "Zo word je wijs",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=d860edd1dd83b36f02ce52bde626c653.2024&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "28/03": {
            "title": "In tijden van nood",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=9f62b8625f914a002496335037e9ad97.2023&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "27/03": {
            "title": "Tien goede tips voor Gods boodschappers",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=312351bff07989769097660a56395065.2021&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "26/03": {
            "title": "De overvloed van de zegen",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=07811dc6c422334ce36a09ff5cd6fe71.2020&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "25/03": {
            "title": "Zeven namen van Jezus",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=5531a5834816222280f20d1ef9e95f69.2019&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "24/03": {
            "title": "God wil je versteld doen staan",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=8038da89e49ac5eabb489cfc6cea9fc1.2009&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "23/03": {
            "title": "Jouw hotline met God",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=253614bbac999b38b5b60cae531c4969.2008&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "22/03": {
            "title": "Wees altijd gul en ruimhartig",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=c8758b517083196f05ac29810b924aca.2007&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "21/03": {
            "title": "Verleiding weerstaan",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=d7a84628c025d30f7b2c52c958767e76.2006&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "20/03": {
            "title": "God is goed, altijd",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=f1981e4bd8a0d6d8462016d2fc6276b3.2005&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "19/03": {
            "title": "Zo ontwikkel je een vertrouwelijke band met God",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=ea5a486c712a91e48443cd802642223d.2002&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "18/03": {
            "title": "Redder",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=d47268e9db2e9aa3827bba3afb7ff94a.2001&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "17/03": {
            "title": "Als het gras groener lijkt, is het waarschijnlijk kunstgras",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=b8b4b727d6f5d1b61fff7be687f7970f.2000&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "16/03": {
            "title": "Wat God voor jou in petto heeft",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=a591024321c5e2bdbd23ed35f0574dde.1999&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "15/03": {
            "title": "Gods gunst rust op jou",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=8d8818c8e140c64c743113f563cf750f.2013&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "14/03": {
            "title": "De strijd van het leven",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=d0fb963ff976f9c37fc81fe03c21ea7b.1997&s=dddc2c42b0959d86bb19db3d3b2e1fa5\""
          },
          "13/03": {
            "title": "Liefdevolle grenzen",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=5ec829debe54b19a5f78d9a65b900a39.1995&s=dddc2c42b0959d86bb19db3d3b2e1fa5\""
          },
          "12/03": {
            "title": "Vertrouwen in je toekomst",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=c5b2cebf15b205503560c4e8e6d1ea78.1994&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "11/03": {
            "title": "Volledige vergeving",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=06964dce9addb1c5cb5d6e3d9838f733.1993&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "10/03": {
            "title": "Gekruisigd",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=dc513ea4fbdaa7a14786ffdebc4ef64e.1986&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "09/03": {
            "title": "Hoe zit het met je hart?",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=4a3e00961a08879c34f91ca0070ea2f5.1985&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "08/03": {
            "title": "MAAR…",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=9d7311ba459f9e45ed746755a32dcd11.1984&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "07/03": {
            "title": "God heeft mij gered",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=d68a18275455ae3eaa2c291eebb46e6d.1983&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "06/03": {
            "title": "Een ommekeer in je leven",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=8c249675aea6c3cbd91661bbae767ff1.1982&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "05/03": {
            "title": "Gezond blijven",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=1f36c15d6a3d18d52e8d493bc8187cb9.1981&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "04/03": {
            "title": "Je leven lang genieten van Gods liefde",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=1e4d36177d71bbb3558e43af9577d70e.1979&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "03/03": {
            "title": "Hoe kun je geestelijk gezag uitoefenen?",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=fb87582825f9d28a8d42c5e5e5e8b23d.1978&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "02/03": {
            "title": "Een liefdevolle, duurzame relatie",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=b3b4d2dbedc99fe843fd3dedb02f086f.1977&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "01/03": {
            "title": "Mijn ogen werden geopend",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=f80bf05527157a8c2a7bb63b22f49aaa.1976&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "29/02": {
            "title": "Schrikkeldag",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=378a063b8fdb1db941e34f4bde584c7d.1954&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "28/02": {
            "title": "Rijk aan genade",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=7f16109f1619fd7a733daf5a84c708c1.1959&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "27/02": {
            "title": "Zes kenmerken van een heilig leven",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=e4dd5528f7596dcdf871aa55cfccc53c.1958&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "26/02": {
            "title": "De juiste kijk op beroemdheid",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=d77f00766fd3be3f2189c843a6af3fb2.1957&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "25/02": {
            "title": "Je leven optimaal benutten",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=277a78fc05c8864a170e9a56ceeabc4c.1956&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "24/02": {
            "title": "God vermenigvuldigt wat jij Hem geeft ",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=e3408432c1a48a52fb6c74d926b38886.1955&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "23/02": {
            "title": "God horen ",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=5a7f963e5e0504740c3a6b10bb6d4fa5.1953&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "22/02": {
            "title": "Tijd met Jezus doorbrengen",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=a38b16173474ba8b1a95bcbc30d3b8a5.1952&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "21/02": {
            "title": "Samen is het beter",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=1113d7a76ffceca1bb350bfe145467c6.1951&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "20/02": {
            "title": "Hoe kunnen we God ontmoeten?",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=6a508a60aa3bf9510ea6acb021c94b48.1950&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "19/02": {
            "title": "God houdt van mij",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=03e7d2ebec1e820ac34d054df7e68f48.1949&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "18/02": {
            "title": "Jouw liefdesbrief",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=36ac8e558ac7690b6f44e2cb5ef93322.1948&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "17/02": {
            "title": "Je geweten slijpen",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=7af6266cc52234b5aa339b16695f7fc4.1940&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "16/02": {
            "title": "Wat het zwaarst is, moet het zwaarst wegen",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=7ca57a9f85a19a6e4b9a248c1daca185.1947&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "15/02": {
            "title": "De hoogte- en dieptepunten van het leven",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=8562ae5e286544710b2e7ebe9858833b.1933&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "14/02": {
            "title": "De allerbelangrijkste vraag van de wereld",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=1e913e1b06ead0b66e30b6867bf63549.1932&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "13/02": {
            "title": "God heeft jouw bestwil voor ogen",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=52d2752b150f9c35ccb6869cbf074e48.1931&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "12/02": {
            "title": "Hij heeft je gered",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=29530de21430b7540ec3f65135f7323c.1929&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "11/02": {
            "title": "Vrijheid",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=5103c3584b063c431bd1268e9b5e76fb.1925&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "10/02": {
            "title": "Levensveranderende woorden",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=0950ca92a4dcf426067cfd2246bb5ff3.1924&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "09/02": {
            "title": "Vijf uitvluchten",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=65fc52ed8f88c81323a418ca94cec2ed.1915&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "08/02": {
            "title": "Leven in een vijandige omgeving",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=b432f34c5a997c8e7c806a895ecc5e25.1914&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "07/02": {
            "title": "Gebruik je gaven",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=07a4e20a7bbeeb7a736682b26b16ebe8.1913&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "06/02": {
            "title": "De verborgen dingen",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=e74c0d42b4433905293aab661fcf8ddb.1917&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "05/02": {
            "title": "Je woorden ten goede gebruiken",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=ff7d0f525b3be596a51fb919492c099c.1911&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "04/02": {
            "title": "Zeven eigenschappen van een goede leider",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=04df4d434d481c5bb723be1b6df1ee65.1910&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "03/02": {
            "title": "Drie soorten overwinning in je leven",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=ab7314887865c4265e896c6e209d1cd6.1909&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "02/02": {
            "title": "Hechte vriendschap",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=e1314fc026da60d837353d20aefaf054.1881&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "01/02": {
            "title": "Je kunt vertrouwen op God",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=b4568df26077653eeadf29596708c94b.1880&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "31/01": {
            "title": "Leidinggeven zoals Jezus",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=3214a6d842cc69597f9edf26df552e43.1879&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "30/01": {
            "title": "Verhoort God al je gebeden?",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=fb8feff253bb6c834deb61ec76baa893.1870&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "29/01": {
            "title": "Je bent geliefd",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=d305281faf947ca7acade9ad5c8c818c.1869&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "28/01": {
            "title": "Bij God is alles mogelijk",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=68c694de94e6c110f42e587e8e48d852.1868&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "27/01": {
            "title": "Op koers blijven",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=c164bbc9d6c72a52c599bbb43d8db8e1.1867&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "26/01": {
            "title": "Waarom staat God het lijden toe?",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=a19acd7d2689207f9047f8cb01357370.1866&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "25/01": {
            "title": "God bedoelde het ten goede",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=67c6a1e7ce56d3d6fa748ab6d9af3fd7.59&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "24/01": {
            "title": "Luisteren naar God",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=d7fd118e6f226a71b5f1ffe10efd0a78.1857&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "23/01": {
            "title": "Jij hebt de sleutels",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=3c947bc2f7ff007b86a9428b74654de5.1855&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "22/01": {
            "title": "‘Hoelang nog, Heer?’",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=49ad23d1ec9fa4bd8d77d02681df5cfa.1853&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "21/01": {
            "title": "Wees eerlijk tegen God",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=7503cfacd12053d309b6bed5c89de212.1852&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "20/01": {
            "title": "Je weg zoeken door het leven",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=eb1e78328c46506b46a4ac4a1e378b91.1851&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "19/01": {
            "title": "Het kostbaarste ter wereld",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=aa2a77371374094fe9e0bc1de3f94ed9.1828&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "18/01": {
            "title": "Uw koninkrijk kome",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=4496bf24afe7fab6f046bf4923da8de6.1827&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "17/01": {
            "title": "Vijf manieren om tot volle bloei te komen",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=fface8385abbf94b4593a0ed53a0c70f.1826&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "16/01": {
            "title": "Waar het hart vol van is",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=f442d33fa06832082290ad8544a8da27.1825&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "15/01": {
            "title": "God is rechtvaardig en barmhartig",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=ed519dacc89b2bead3f453b0b05a4a8b.1824&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "14/01": {
            "title": "Maak je niet druk, laat God zijn werk maar doen",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=2647c1dba23bc0e0f9cdf75339e120d2.1823&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "13/01": {
            "title": "Goddelijke versnelling",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=14cfdb59b5bda1fc245aadae15b1984a.1822&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "12/01": {
            "title": "Geen angst",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=0e087ec55dcbe7b2d7992d6b69b519fb.1821&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "11/01": {
            "title": "‘Heer… geef me succes vandaag’",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=f5c3dd7514bf620a1b85450d2ae374b1.1817&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "10/01": {
            "title": "De stormen van het leven het hoofd bieden",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=f4a4da9aa7eadfd23c7bdb7cf57b3112.1816&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "09/01": {
            "title": "Vertrouw erop dat God de dingen rechtzet",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=faacbcd5bf1d018912c116bf2783e9a1.1815&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "08/01": {
            "title": "Niets is onmogelijk voor de Heer",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=f0bbac6fa079f1e00b2c14c1d3c6ccf0.1814&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "07/01": {
            "title": "Jouw dubbele zegen",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=155fa09596c7e18e50b58eb7e0c6ccb4.1813&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "06/01": {
            "title": "Richtlijnen voor het leven",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=5b6ba13f79129a74a3e819b78e36b922.1811&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "05/01": {
            "title": "God zal je goede dingen geven",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=09b15d48a1514d8209b192a8b8f34e48.1810&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "04/01": {
            "title": "Strijd en zegen",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=645098b086d2f9e1e0e939c27f9f2d6f.1808&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "03/01": {
            "title": "Praat tijdens het wandelen",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=39027dfad5138c9ca0c474d71db915c3.1807&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "02/01": {
            "title": "Je eerste vraag",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=1f1baa5b8edac74eb4eaa329f14a0361.1806&s=5a0b94903df7b4cf73dd58253fba58ef"
          },
          "01/01": {
            "title": "Goede voornemens",
            "url": "https://alphanl.activehosted.com/index.php?action=social&chash=9fe97fff97f089661135d0487843108e.1702&s=5a0b94903df7b4cf73dd58253fba58ef"
          }
        }
        now = datetime.now().strftime("%d/%m")
        data = {}
        data['index'] = "https://alphanederland.org/bible-in-one-year-gemist/"
        data['name'] = "Bible in One Year"
        data['section'] = now
        data['title'] = list[now]["title"]
        data['url'] = list[now]["url"]
        data['image'] = "https://alphanederland.org/wp-content/uploads/2023/12/130267.jpg"
        self._data.update(data)

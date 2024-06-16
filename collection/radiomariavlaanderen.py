from collection.data import *
from collection.source import Card


class RadioMariaVlaanderen(Card):
    def __init__(self):
        self._key = "radiomariavlaanderen"
        self._category = "prayer mp3"
        self._type = "daily"
        self._data = {}
        self._template = """
            {% if data %}
            <div class="item" id="item-radiomariavlaanderen">
                <!-- there's a call to add the 'oldnews' class to this card in grid.html
                     only when showing the full grid (so not for historical view) -->
                <div class="card prayer mp3">
                    <a target="_blank" href="{{data['url']}}">
                        <div class="filled-image">
                            <img src="{{data['image']}}"/>
                        </div>
                        <div class="title">{{data['name']}}</div>
                        <div class="text" id="title-radiomariavlaanderen">{{data['title']}}</div>
                    </a>
                    <div class="actions">
                        <a target="_blank" id="play-{{data['key']}}" onclick="document.cookie='{{data['key']}}={{data['url']}}; expires=Fri, 31 Dec 9999 23:59:59 GMT;'">
                            <div class="button play-button">BELUISTEREN</div>
                        </a>
                        <script>
                        $(function(){
                            var audio = playRadio('{{data['key']}}', '{{data['mp3']}}', false, 'alledaags');
                            //var xpath = "//h3/text()";
                            //var url = "http://www.radiomaria.be/audio-player-popup/";
                            //var statusurl = "/yql/html?url=$url&xpath=$xpath";
                            //statusurl = statusurl.replace("$url", encodeURIComponent(url));
                            //statusurl = statusurl.replace("$xpath", encodeURIComponent(xpath));
                            //var statusladen = $.getJSON(statusurl);
                            //statusladen.done(function(d){
                            //    var status = d;
                            //    $('#title-radiomariavlaanderen').text(status);
                            //    if (status.match(/Angelus|Uur van de Barmhartigheid|Rozenkrans|Lauden|Middaggebed|Bidden onderweg|Vespers|Completen|Eucharistie|Avondgebed/)) {
                            //        $('#item-radiomariavlaanderen').show();
                            //    } else {
                            //        $('#item-radiomariavlaanderen').hide();
                            //    }
                            //    $('#container').masonry('layout');
                            //});
                        });
                        //@ sourceURL={{data['key']}}.js
                        </script>
                        <div class="status" id="status-{{data['key']}}"></div>
                    </div>
                    <div class="actions">
                        {% set url = my_encode(data['url']) %}
                        {% set title = my_encode("Radio Maria: " + data['title'] + ' via alledaags.gelovenleren.net') %}
                        {% set short_title = my_encode("Radio Maria: " + data['title']) %}
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

    def harvestInit(self):
        data = {
            'name': "Radio Maria Vlaanderen",
            'title': "Live gebed",
            'image': "/static/radiomariavlaanderen.png",
            'url': "https://www.radiomaria.be/",
            'mp3': "http://stream.radiomaria.be:8000/RadioMaria-32",
            'key': self._key
        }
        self._data.update(data)



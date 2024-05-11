from collection.source import Radio
import os


class KoningsoordRadio(Radio):
    def __init__(self):
        self._key = "koningsoord-radio"
        self._category = "prayer"
        self._type = "daily"
        self._data = {}
        self._template = """
            {% if data %}
            <div class="item" id="item-{{data['key']}}">
                <div class="card prayer">
                    <div class="filled-image">
                        <img src="{{data['image']}}" width="{{data['image-width']}}" height="{{data['image-height']}}""/>
                    </div>
                    <div class="title">{{data['name']}}</div>
                    <div class="text" id="title-{{data['key']}}">{{data['title']}}</div>
                    <div class="actions">
                        <a target="_blank" id="play-{{data['key']}}" class="radio">
                            <div class="action-button play-button"></div>
                        </a>
                        <script>
                        $(function(){
                            var audio = playRadio('{{data['key']}}', '{{data['mp3']}}', true, 'radio');
                            // fetch the website status every 5 minutes
                            setInterval(function update() {
                                var xpath = "//h1/text()";
                                var url = "https://klanten.connectingmedia.nl/koningsoord/stream-embed.php";
                                var statusurl = "https://alledaags.gelovenleren.net/yql/html?url=$url&xpath=$xpath&callback=?";
                                statusurl = statusurl.replace("$url", encodeURIComponent(url));
                                statusurl = statusurl.replace("$xpath", encodeURIComponent(xpath));
                                var statusladen = $.getJSON(statusurl);
                                statusladen.done(function(d){
                                    var status = d;
                                    $('#title-{{data['key']}}').text(status);
                                    $('#container').masonry('layout');
                                });
                                return update; // part of a trick to run the first update immediately
                            }(), 300000);
                        });
                        //@ sourceURL={{data['key']}}.js
                        </script>
                        <div class="status" id="status-{{data['key']}}"></div>
                    </div>
                </div>
            </div>
            {% endif %}
        """

    def harvestInit(self):
        data = {
            'name': "Abdij Koningsoord",
            'title': "Live getijden",
            'image': os.environ['SERVER'] + "/var/koningsoord.jpg",
            'image-width': '304',
            'image-height': '152',
            'url': "https://abdijkoningsoord.org/ons-gebed/getijden/",
            'mp3': "https://darkice.mx10.nl:8443/abdijkoningsoord",
            'key': self._key
        }
        self._data.update(data)



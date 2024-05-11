from collection.source import Radio
import os


class RadioMariaVlaanderenRadio(Radio):
    def __init__(self):
        self._key = "radiomariavlaanderen-radio"
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
                            //audio.addEventListener('loadedmetadata',function(){
                                // fetch the website status every 5 minutes
                                //setInterval(function update() {
                                //    var xpath = "//h3/text()";
                                //    var url = "http://www.radiomaria.be/audio-player-popup/";
                                //    var statusurl = "https://alledaags.gelovenleren.net/yql/html?url=$url&xpath=$xpath&callback=?";
                                //    statusurl = statusurl.replace("$url", encodeURIComponent(url));
                                //    statusurl = statusurl.replace("$xpath", encodeURIComponent(xpath));
                                //    var statusladen = $.getJSON(statusurl);
                                //    statusladen.done(function(d){
                                //        var status = d;
                                //        $('#title-{{data['key']}}').text(status);
                                //        $('#container').masonry('layout');
                                //    });
                                //    return update; // part of a trick to run the first update immediately
                                //}(), 300000);
                            //},true);
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
            'name': "Radio Maria Vlaanderen",
            'title': "Live radio",
            'image': os.environ['SERVER'] + "/var/vatican.jpg",
            'image-width': '304',
            'image-height': '104',
            'url': "https://www.radiomaria.be/",
            'mp3': "http://stream.radiomaria.be:8000/RadioMaria-32",
            'key': self._key
        }
        self._data.update(data)



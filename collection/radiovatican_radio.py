from collection.source import Radio
import os


class RadioVaticanRadio(Radio):
    def __init__(self):
        self._key = "radiovatican-radio"
        self._category = "prayer"
        self._type = "daily"
        self._data = {}
        self._template = """
            {% if data %}
            <div class="item" id="item-{{data['key']}}">
                <div class="card prayer">
                    <div class="padded-image">
                        <img src="{{data['image']}}" width="{{data['image-width']}}" height="{{data['image-height']}}""/>
                    </div>
                    <div class="title">{{data['name']}}</div>
                    <div class="text" id="title-{{data['key']}}">{{data['title']}}</div>
                    <!--div class="caption" id="description-{{data['key']}}"></div-->
                    <!--div class="caption" id="next-{{data['key']}}"></div-->
                    <div class="actions">
                        <a target="_blank" id="play-{{data['key']}}" class="radio">
                            <div class="action-button play-button"></div>
                        </a>
                        <script>
                        $(function(){
                            var audio = playRadio('{{data['key']}}', '{{data['mp3']}}', true, 'radio');
                            /*
                            audio.addEventListener('loadedmetadata',function(){
                                // fetch the website status every 5 minutes
                                setInterval(function update() {
                                    var url = "https://en.radiovaticana.va/api/epgweb/transmissionapi/onair?idChannel=167&codeLanguage=en";
                                    var xpath = "/"
                                    var statusurl = "https://alledaags.gelovenleren.net/yql/html?url=$url&xpath=$xpath&callback=?";
                                    statusurl = statusurl.replace("$url", encodeURIComponent(url));
                                    statusurl = statusurl.replace("$xpath", encodeURIComponent(xpath));
                                    var statusladen = $.getJSON(statusurl);
                                    statusladen.done(function(d){
                                        var nowTitle = d.json.json[0].ProgramTitle;
                                        var nowDescription = d.json.json[0].ProgramDescription;
                                        var nextTitle = d.json.json[1].ProgramTitle;
                                        var nextDescription = d.json.json[1].ProgramDescription;
                                        var nextStart = d.json.json[1].DateStart.substring(11,16);
                                        $('#title-{{data['key']}}').text(nowTitle);
                                        $('#description-{{data['key']}}').text(nowDescription);
                                        $('#next-{{data['key']}}').text("Volgende programma om " + nextStart + ": " + nextTitle);
                                        $('#container').masonry('layout');
                                    });
                                    return update; // part of a trick to run the first update immediately
                                }(), 300000);
                            },true);
                            */
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
            'name': "Radio Vaticaan",
            'title': "Kanaal 1",
            'image': os.environ['SERVER'] + "/var/radiovatican.png",
            'image-width': '250',
            'image-height': '147',
            'url': "http://www.radiovaticana.va/en3/diretta.asp",
            'mp3': "http://live.vaticanwebradio.org/channel1.mp3",
            'key': self._key
        }
        self._data.update(data)



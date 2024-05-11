from collection.source import Radio
import os


class GregoriaansRadio(Radio):
    def __init__(self):
        self._key = "gregoriaans-radio"
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
                            audio.addEventListener('loadedmetadata',function(){
                                // fetch the website status every 5 minutes
                                setInterval(function update() {
                                    var statusyql = 'select * from json where url="https://www.concertzender.nl/wp-admin/admin-ajax.php?action=get_stream_info&kind=19&lang=nl"';
                                    var statusurl = "https://query.yahooapis.com/v1/public/yql?q=$yql&format=json&callback=";
                                    statusurl = statusurl.replace("$yql", encodeURIComponent(statusyql));
                                    var statusladen = $.getJSON(statusurl);
                                    statusladen.done(function(d){
                                        var status = d['query']['results']['json']['current']['title'];
                                        $('#title-{{data['key']}}').text(status);
                                        $('#container').masonry('layout');
                                    });
                                    return update; // part of a trick to run the first update immediately
                                }(), 300000);
                            },true);
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
            'name': "Gregoriaans",
            'title': "Muziekradio",
            'image': os.environ['SERVER'] + "/var/concertzender.jpg",
            'image-width': '304',
            'image-height': '214',
            'url': "https://www.concertzender.nl/",
            'mp3': "http://streams.greenhost.nl:8080/gregoriaans",
            'key': self._key
        }
        self._data.update(data)



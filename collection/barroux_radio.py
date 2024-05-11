from collection.source import Radio
import os


class BarrouxRadio(Radio):
    def __init__(self):
        self._key = "barroux-radio"
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
                            var audio = playRadio('{{data['key']}}', '{{data['mp3']}}', true);
                            audio.update = function() {
                                var now = new Date();
                                var nowtime = now.getHours() * 100 + now.getMinutes();
                                var status;
                                var status = '#status-' + '{{data['key']}}';
                                if ($(status).text() == "Luister!" ||
                                    $(status).text() == "Online" ||
                                    $(status).text() == "Even geduld...") {
                                    if (nowtime >= 1940) {
                                        status = "De Completen zijn gestart";
                                    } else if (nowtime >= 1725) {
                                        status = "De Vespers zijn gestart";
                                    } else if (nowtime >= 1420) {
                                        status = "De Noon is gestart";
                                    } else if (nowtime >= 1210) {
                                        status = "De Sext is gestart";
                                    } else if (nowtime >= 925) {
                                        status = "De Terts is gestart";
                                    } else if (nowtime >= 740) {
                                        status = "De Priem is gestart";
                                    } else if (nowtime >= 555) {
                                        status = "De Lauden zijn gestart";
                                    }
                                } else {
                                    if (nowtime < 600) {
                                        status = "Aanvang Lauden rond 6:00";
                                    } else if (nowtime < 745) {
                                        status = "Aanvang Priem rond 7:45 of 8:00 (zondag)";
                                    } else if (nowtime < 930) {
                                        status = "Aanvang Terts rond 9:30";
                                    } else if (nowtime < 1215) {
                                        status = "Aanvang Sext rond 12:15";
                                    } else if (nowtime < 1415) {
                                        status = "Aanvang Noon rond 14:15 of 14:30 (zondag)";
                                    } else if (nowtime < 1730) {
                                        status = "Aanvang Vespers rond 17:30";
                                    } else if (nowtime < 1945) {
                                        status = "Aanvang Completen rond 19:45";
                                    } else {
                                        status = "Er zijn geen uitzendingen meer vandaag.";
                                    }
                                }
                                $('#title-{{data['key']}}').text(status);
                                $('#container').masonry('layout');
                                return;
                            }
                            audio.update();
                            // calculuate the status once after 5 seconds, for if the audio loads slowly
                            setTimeout(audio.update, 5000);
                            // calculate the status every 5 minutes
                            setInterval(audio.update, 300000);
                            // also calculate the status when the audio becomes available
                            audio.addEventListener('canplay', audio.update);
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
            'name': "Abbaye du Barroux",
            'title': "Live getijden (Latijn)",
            'image': os.environ['SERVER'] + "/var/barroux.jpg",
            'image-width': '304',
            'image-height': '235',
            'url': "https://www.barroux.org/en/liturgie/listen-to-our-offices.html",
            'mp3': "https://barroux.ice.infomaniak.ch/chant.mp3",
            'key': self._key
        }
        self._data.update(data)



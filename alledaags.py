from flask import request
from flask_init import app
import grid
import sync
import yql

@app.route("/init")
def sync_init():
    return sync.initHandler(request)

@app.routes("/sync")
def sync_sync():
    return sync.syncHandler(request)

@app.route("/radio")
def radio_radio():
    return radio.radioHandler(request)

@app.route("/api-ai-bible-passage")
def api_ai_biblePassage():
    return api_ai.biblePassageHandler(request)

@app.route("/image/<key>")
def image_image(key):
    return image.image(request,key)

@app.route("/random/<key>")
def randomizer_random(key):
    return randomizer.randomHandler(request,key)

@app.route("/randomcard/<category>")
def randomizer_randomCard(category):
    return randomizer.randomCardHandler(request,category)

@app.route("/")
@app.route("/link/<historical>")
def grid_grid(historical=None):
    return grid.gridHandler(request,historical)

@app.route("/yql/html")
def yql_yqlHtml():
    return yql.yqlHtmlHandler(request)

@app.route("/yql/text")
def yql_yqlText():
    return yql.yqlTextHandler(request)

@app.route("/yql/bibleref")
def yql_bibleref():
    return yql.yqlBibleRefHandler(request)

@app.route("/yql/bible")
def yql_bible():
    return yql.bibleHandler(request)

@app.route("/bibletest")
def yql_bibleTest():
    return yql.bibleTestHandler(request)

@app.route("/playlist-latest")
def yql_yqlPlaylistLatest():
    return yql.yqlPlayListLatestHandler(request)

@app.route("/lectionarium")
def lectionarium_lectionarium():
    return lectionarium.lectionariumHandler(request)

if __name__ == "__main__":
    app.run(host='0.0.0.0')

from flask import Flask, request
import yql
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"

@app.route("/yql/bibleref")
def yql_bibleref():
    return yql.yqlBibleRefHandler(request)

if __name__ == "__main__":
    app.run(host='0.0.0.0')

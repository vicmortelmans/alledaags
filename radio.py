from collection import cards
from flask import Response
from jinja_templates import jinja_environment
import urllib.request, urllib.error, urllib.parse
import json


def radioHandler(request):
    template = jinja_environment.get_template('radio.html')
    content = template.render(
        radios_list=cards.radios_list,
        cookies=request.cookies
    )
    content_for_json = {
        "html": content
    }
    flask_response = Response(
        "%s(%s)" %
        (urllib.parse.unquote(request.args.get('callback')),
         json.dumps(content_for_json))
    )
    flask_response.headers['Content-Type'] = 'application/javascript'
    return flask_response

from flask import Response
from jinja_templates import jinja_environment
from bible import get_bible_text


def lectionariumHandler(request):
    title = ""
    subtitle = ""
    source = ""
    copyright = ""
    edition = ""
    language = "en"
    readings = []
    parameters = list(request.GET.items())
    for p in parameters:
        if p[0] == "title":
            title = p[1]
        elif p[0] == "subtitle":
            subtitle = p[1]
        elif p[0] == "language":
            language = p[1]
        elif p[0] == "edition":
            edition = p[1]
        else:
            readings.append({
                "title": p[0],
                "subtitle": p[1]
            })
    for i, r in enumerate(readings):
        bibleref_string = r["subtitle"]
        json_output = get_bible_text(edition, None, None, None, None, bibleref_string, language=language)
        source = json_output["name"] if not json_output["name"] == 'unknown' else None
        copyright = json_output["copyright"] if not json_output["copyright"] == 'unknown' else None
        r["subtitle"] = json_output["bibleref"]
        r["text"] = json_output["passage"]
    template = jinja_environment.get_template('lectionarium.html')
    content = template.render(
        title=title,
        subtitle=subtitle,
        source=source,
        copyright=copyright,
        readings=readings
    )
    # return the web-page content
    flask_response = Response(content)
    return flask_response

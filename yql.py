import API_keys
from bible import get_bible_text, test_bible
from bibleref import parse_reference
from collection.data import getHtml, getText, getJSON
from flask import Response
import json
from lxml import etree
import urllib


def create_xml_tree(root, dict_tree):
    # Node : recursively create tree nodes
    # https://gist.github.com/kjaquier/1e61ff4054577c54960d
    if type(dict_tree) == dict:
        for k, v in dict_tree.items():
            if type(v) == list:
                for item in v:
                    create_xml_tree(etree.SubElement(root, k), item)
            else:
                create_xml_tree(etree.SubElement(root, k), v)
        return root
    # Leaf : just set the value of the current node
    else:
        try:
            root.text = dict_tree
        except TypeError:
            root.text = str(dict_tree)


def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    Source : http://stackoverflow.com/questions/17402323/use-xml-etree-elementtree-to-write-out-nicely-formatted-xml-files
    """
    from xml.dom import minidom
    rough_string = etree.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="".join([' '] * 4))


def yqlPlaylistLatestHandler(request):
    # e.g.: https://catecheserooster.appspot.com/playlist-latest?id=PLsTqv8iy6f_2gSqDwxZfRt98N9-idZEBq
    id = urllib.parse.unquote(request.args.get('id'))
    callback = request.args.get('callback')
    site = "https://www.googleapis.com/youtube/v3/playlistItems?playlistId=" + id + "&maxResults=25&part=snippet%2CcontentDetails&key=" + API_keys.YOUTUBE
    harvest = getJSON(site)
    try:
        items = [
            {
                'title': item['snippet']['title'],
                'video': "https://www.youtube.com/embed/" + item['snippet']['resourceId']['videoId'],
                'url': "https://www.youtube.com/watch?v=" + item['snippet']['resourceId']['videoId'],
                'publishedAt': item['snippet']['publishedAt']
            }
            for item in harvest['items']
        ]
        while 'nextPageToken' in harvest:
            site2 = site + "&pageToken=" + harvest['nextPageToken']
            harvest = getJSON(site2)
            items += [
                {
                    'title': item['snippet']['title'],
                    'video': "https://www.youtube.com/embed/" + item['snippet']['resourceId']['videoId'],
                    'url': "https://www.youtube.com/watch?v=" + item['snippet']['resourceId']['videoId'],
                    'publishedAt': item['snippet']['publishedAt']
                }
                for item in harvest['items']
            ]

    except (TypeError, KeyError, IndexError) as e:
        pass

    newest_date = ""
    for item in items:
        if item['publishedAt'] > newest_date:
            newest_item = item

    response = json.dumps(newest_item)
    if callback:
        response = callback + '(' + response + ')'
    flask_response = Response(response)
    flask_response.headers['Content-Type'] = 'application/json'
    return flask_response


def yqlHtmlHandler(request):
    url = urllib.parse.unquote(request.args.get('url'))
    xpath = urllib.parse.unquote(request.args.get('xpath'))
    callback = request.args.get('callback')
    xml_requested = request.args.get('xml')
    if xml_requested:
        response = getHtml(url, xpath, xml_requested=xml_requested)
        flask_response = Response(response)
        flask_response.headers['Content-Type'] = 'text/xml'
        return flask_response
    else:
        yql_data = getHtml(url, xpath)
        response = json.dumps(yql_data)
        if callback:
            response = callback + '(' + response + ')'
        flask_response = Response(response)
        flask_response.headers['Content-Type'] = 'application/json'
        return flask_response


def yqlTextHandler(request):
    url = urllib.parse.unquote(request.args.get('url'))
    callback = request.args.get('callback')
    yql_data = getText(url)
    response = json.dumps(yql_data)
    if callback:
        response = callback + '(' + response + ')'
    flask_response = Response(response)
    flask_response.headers['Content-Type'] = 'application/json'
    return flask_response


def yqlBibleRefHandler(request):
    # /yql/bibleref?bibleref=Mc+1,10-12&language=nl&tolerance=true&xml=true
    bibleref = urllib.parse.unquote(request.args.get('bibleref'))  # e.g. Mt+1:4-5
    language = urllib.parse.unquote(request.args.get('language'))  # e.g. nl
    tolerance_param = urllib.parse.unquote(request.args.get('tolerance'))  # e.g. true
    callback = request.args.get('callback')
    xml_requested = request.args.get('xml')
    yql_data = parse_reference(bibleref, language, tolerance_param)
    if xml_requested:
        query = etree.Element('query')
        results = etree.SubElement(query,'results')
        biblerefs = etree.SubElement(results,'biblerefs')
        xml_ready = {'bibleref': yql_data}
        create_xml_tree(biblerefs, xml_ready)
        response = etree.tostring(query, pretty_print=True)
        flask_response = Response(response)
        flask_response.headers['Content-Type'] = 'text/xml'
        return flask_response
    else:
        response = json.dumps(yql_data)
        if callback:
            response = callback + '(' + response + ')'
        flask_response = Response(response)
        flask_response.headers['Content-Type'] = 'application/json'
        return flask_response


def yqlBibleHandler(request):
    language = urllib.parse.unquote(request.args.get('language'))  # e.g. nl
    edition = urllib.parse.unquote(request.args.get('edition'))  # e.g. WV95
    service = urllib.parse.unquote(request.args.get('service'))  # e.g. rkbijbel
    book = urllib.parse.unquote(request.args.get('book'))  # e.g. Lc
    chapter = urllib.parse.unquote(request.args.get('chapter'))  # e.g. 11
    passage = urllib.parse.unquote(request.args.get('passage'))  # e.g. 9
    bibleref = urllib.parse.unquote(request.args.get('bibleref'))  # e.g. Lc 9:11-15
    tolerance_param = urllib.parse.unquote(request.args.get('tolerance'))  # e.g. true
    chunksize = urllib.parse.unquote(request.args.get('chunksize'))  # e.g. 7
    chunk = urllib.parse.unquote(request.args.get('chunk'))  # e.g. 2
    callback = request.args.get('callback')
    xml_requested = request.args.get('xml')
    yql_data = get_bible_text(edition, service, book, chapter, passage, bibleref, language, tolerance_param, chunksize, chunk)
    if xml_requested:
        query = etree.Element('query')
        results = etree.SubElement(query,'results')
        passage = etree.SubElement(results,'passage')
        xml_ready = {'bibleref': yql_data}
        create_xml_tree(passage, xml_ready)
        response = etree.tostring(query, pretty_print=True)
        flask_response = Response(response)
        flask_response.headers['Content-Type'] = 'text/xml'
        return flask_response
    else:
        response = json.dumps(yql_data)
        if callback:
            response = callback + '(' + response + ')'
        flask_response = Response(response)
        flask_response.headers['Content-Type'] = 'application/json'
        return flask_response


def yqlBibleTestHandler(request):
    bibleref = urllib.parse.unquote(request.args.get('bibleref'))  # e.g. Lc 9:11-15
    yql_data = test_bible(bibleref)
    response = json.dumps(yql_data, indent=2)
    flask_response = Response(response)
    flask_response.headers['Content-Type'] = 'application/json'
    return flask_response

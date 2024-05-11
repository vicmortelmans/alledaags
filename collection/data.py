import json
import time
import http.client
import logging
from lxml import html, etree
from lxml.html import HtmlComment
import urllib.request, urllib.error, urllib.parse
import re
from collection.source import Card, Radio  # used in the cards
import chardet


def report_error_by_mail(title, text):
    # TODO implement some logging here?
    pass


def remove_namespace(tag):
    # elements with namespaces have names like '{http://www.w3.org/2005/Atom}feed' and I don't need that namespace
    logging.debug("remove_namespace from %s" % tag)
    return re.sub(r'\{.*\}', '', tag)


def element_to_json(e):
    # transform a single element
    # returns a tuple tag,content,tail where
    # - tag is the name of the element
    # - content is a dict with the element's attributes and child elements
    #   (merged into arrays if appropriate)
    # - tail is the content of a text node child of the parent that comes
    #   right after this element (actually belongs to the parent)
    content = {}  # empty JSON object
    is_text_node = True
    for attribute_name in e.attrib:
        is_text_node = False
        # an attribute becomes a key,value property in JSON
        content[attribute_name] = e.attrib[attribute_name]
    # a text node that comes before the first child element
    # goes into the content property
    content["content"] = e.text
    for child in e:
        is_text_node = False
        child_tag, child_content, child_tail = element_to_json(child)
        if child_tag:
            if child_tag in content:
                if type(content[child_tag]) is list:
                    # a child element with a name that already occurred
                    # is appended to the key,value array property in JSON
                    # with that name
                    content[child_tag].append(child_content)
                else:
                    # if it's the second child element with that name,
                    # the array must be constructed
                    content[child_tag] = [content[child_tag], child_content]
            else:
                # a child element becomes a key,value property in JSON
                content[child_tag] = child_content
        # a text node that comes right after this element
        # goes into the content property
        if child_tail:
            if content["content"]:
                content["content"] += child_tail
            else:
                content["content"] = child_tail
    if not isinstance(e, HtmlComment):
        tag = remove_namespace(e.tag)
    else:
        # the element is a comment
        return '', '', e.tail
    if is_text_node:
        return tag, content["content"], ''
    else:
        return tag, content, e.tail


def elements_list_to_json(l):
    # the query result can be a list of elements and strings
    # returns the content where
    # - content is a dict with the child elements (merged into arrays if appropriate)
    #   and a 'content' property containing the strings concatenated
    # OR
    # - just the strings concatenated if there were no elements
    # This is all to mimic the JSON that was returned by YQL's html open table, which I relied upon in the start
    content = {}  # empty JSON object
    is_only_text = True
    content["content"] = ""
    for child in l:
        if isinstance(child, str):
            content["content"] += child
        else:
            is_only_text = False
            child_tag, child_content, child_tail = element_to_json(child)
            if child_tag:
                if child_tag in content:
                    if type(content[child_tag]) is list:
                        # a child element with a name that already occurred
                        # is appended to the key,list-of-value array property in JSON
                        # with that name
                        content[child_tag].append(child_content)
                    else:
                        # if it's the second child element with that name,
                        # the array must be constructed
                        content[child_tag] = [content[child_tag], child_content]
                else:
                    # a child element becomes a key,value property in JSON
                    content[child_tag] = child_content
    if is_only_text:
        return content["content"]
    else:
        return content


def get_only_content_from_element(element):
    content = ''
    for child in element:
        if child == 'content' and isinstance(element[child], str):
            content += element[child]
        elif isinstance(element[child], dict):
            content += get_only_content_from_element(element[child])
    return content


def getHtml(url, xpath, no_headers=False, xml_requested=False, tree_requested=False):
    """
     return the result as a json dict; if the xpath queries for an <a> element, access the result as {'a':...}
     or {'a':[...]} if more than one match
     if xml_requested, return the result as xml wrapped in <query><results>...</results></query>
    """
    logging.info("Going to query %s for %s." % (url, xpath))
    sleep = 1
    for attempt in range(5):
        try:
            logging.info("Querying %s." % url)
            if not no_headers:
                hdr = {
                    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
                    'AppleWebKit/537.11 (KHTML, like Gecko) '
                    'Chrome/23.0.1271.64 Safari/537.11',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                    'Accept-Encoding': 'none',
                    'Accept-Language': 'en-US,en;q=0.8',
                    'Connection': 'keep-alive'
                }
                request = urllib.request.Request(url, headers=hdr)
            else:
                request = urllib.request.Request(url)
            htmlstring = urllib.request.urlopen(request).read()
            htmlstring = htmlstring.decode(chardet.detect(htmlstring)['encoding'], errors="ignore").encode('utf-8')
            utf8parser = etree.HTMLParser(encoding="utf-8", remove_comments=True)
            tree = etree.HTML(htmlstring, parser=utf8parser)
            #tree = html.fromstring(htmlstring)
            result = tree.xpath(xpath)
        except (http.client.HTTPException, urllib.error.HTTPError) as e:
            time.sleep(sleep)  # pause to avoid "Rate Limit Exceeded" error
            logging.warning("Sleeping %d seconds because of HttpError trying to query %s (%s)." % (sleep, url, e))
            sleep *= 2
        else:
            break  # no error caught
    else:
        logging.critical("Retried 5 times querying %s." % url)
        return ''
        #raise  # attempts exhausted
    if xml_requested:
        query = etree.Element('query')
        results = etree.SubElement(query,'results')
        for r in result:
            results.append(r)
        return etree.tostring(query, pretty_print=True)
    elif tree_requested:
        return result
    else:
        return elements_list_to_json(result)


def getXml(url, xpath):
    """
     return the result as a json dict; if the xpath queries for an <a> element, access the result as {'a':...}
     or {'a':[...]} if more than one match
     /!\ elements should not be named 'content' /!\
    """
    logging.info("Going to query %s for %s." % (url, xpath))
    sleep = 1
    for attempt in range(5):
        try:
            logging.info("Querying %s." % url)
            request = urllib.request.Request(url)
            xmlstring = urllib.request.urlopen(request).read()
            tree = etree.fromstring(xmlstring)
            result = tree.xpath(xpath)
        except (http.client.HTTPException) as e:
            time.sleep(sleep)  # pause to avoid "Rate Limit Exceeded" error
            logging.warning("Sleeping %d seconds because of HttpError trying to query %s (%s)." % (sleep, url, e))
            sleep *= 2
        else:
            break  # no error caught
    else:
        logging.critical("Retried 10 times querying %s." % url)
        return ''
        #raise  # attempts exhausted
    return elements_list_to_json(result)


def getJsonPath(url, path, parser_string, no_headers=True):
    """
     return the result as a json dict
    """
    if parser_string:
        logging.info("Going to query json %s for %s." % (url, parser_string))
    elif path:
        logging.info("Going to query json %s for %s." % (url, path))
    else:
        logging.info("Going to query json %s." % url)
    sleep = 1
    for attempt in range(5):
        try:
            logging.info("Querying %s." % url)
            if not no_headers:
                hdr = {
                    "Accept-Language": "en-US,en,nl;q=0.5",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                    "Referer": "https://alledaags.gelovenleren.net",
                    "Connection": "keep-alive"
                }
                request = urllib.request.Request(url, headers=hdr)
            else:
                request = urllib.request.Request(url)
            json_string = urllib.request.urlopen(request).read()
            if parser_string:
                parser = None
                exec(parser_string)  # this should define parser as a function
                result = parser(json.loads(json_string))
            elif path:
                result = eval(json_string + path)
            else:
                result = json.loads(json_string)
        except (http.client.HTTPException) as e:
            time.sleep(sleep)  # pause to avoid "Rate Limit Exceeded" error
            logging.warning("Sleeping %d seconds because of HttpError trying to query %s (%s)." % (sleep, url, e))
            sleep *= 2
        except(KeyError, IndexError):
            logging.critical("Error parsing %s." % url)
            return ''
            #raise
        else:
            break  # no error caught
    else:
        logging.critical("Retried 10 times querying %s." % url)
        return ''
        #raise  # attempts exhausted
    return result


def getJsonPathPOST(url, data, path, parser_string, headers=None):
    """
     return the result as a json dict
    """
    if parser_string:
        logging.info("Going to query json %s with data %s for %s." % (url, data, parser_string))
    elif path:
        logging.info("Going to query json %s with data %s for %s." % (url, data, path))
    else:
        logging.info("Going to query json %s with data %s." % (url, data))
    sleep = 1
    for attempt in range(5):
        try:
            logging.info("Querying %s." % url)
            if headers:
                request = urllib.request.Request(url, headers=headers)
            else:
                request = urllib.request.Request(url)
            json_string = urllib.request.urlopen(request, data=data).read()
            if parser_string:
                parser = None
                exec(parser_string)  # this should define parser as a function
                result = parser(json.loads(json_string))
            elif path:
                result = eval(json_string + path)
            else:
                result = json.loads(json_string)
        except (http.client.HTTPException) as e:
            time.sleep(sleep)  # pause to avoid "Rate Limit Exceeded" error
            logging.warning("Sleeping %d seconds because of HttpError trying to query %s (%s)." % (sleep, url, e))
            sleep *= 2
        except(KeyError, IndexError):
            logging.critical("Error parsing %s." % url)
            return ''
            #raise
        else:
            break  # no error caught
    else:
        logging.critical("Retried 10 times querying %s." % url)
        return ''
        #raise  # attempts exhausted
    return result


def getRSS(url, headers=False):
    """
     return the result as a json dict {'item': [...]}
    """
    logging.info("Going to query %s." % url)
    sleep = 1
    for attempt in range(5):
        try:
            logging.info("Querying %s." % url)
            if headers:
                hdr = {
                    "Accept-Language": "en-US,en,nl;q=0.5",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                    "Referer": "https://alledaags.gelovenleren.net",
                    "Connection": "keep-alive"
                }
                request = urllib.request.Request(url, headers=hdr)
            else:
                request = urllib.request.Request(url)
            xmlstring = urllib.request.urlopen(request).read()
            tree = etree.fromstring(xmlstring)
            result = tree.xpath("//item")
        except (http.client.HTTPException) as e:
            time.sleep(sleep)  # pause to avoid "Rate Limit Exceeded" error
            logging.warning("Sleeping %d seconds because of HttpError trying to query %s (%s)." % (sleep, url, e))
            sleep *= 2
        else:
            break  # no error caught
    else:
        logging.critical("Retried 10 times querying %s." % url)
        return ''
        #raise  # attempts exhausted
    return elements_list_to_json(result)


def getAtom(url):
    """
     return the result as a json dict {'item': [...]}
    """
    logging.info("Going to query %s." % url)
    sleep = 1
    for attempt in range(5):
        try:
            logging.info("Querying %s." % url)
            request = urllib.request.Request(url)
            xmlstring = urllib.request.urlopen(request).read()
            tree = etree.fromstring(xmlstring)
            result = tree.xpath("//*[local-name() = 'entry']")
        except (http.client.HTTPException) as e:
            time.sleep(sleep)  # pause to avoid "Rate Limit Exceeded" error
            logging.warning("Sleeping %d seconds because of HttpError trying to query %s (%s)." % (sleep, url, e))
            sleep *= 2
        else:
            break  # no error caught
    else:
        logging.critical("Retried 10 times querying %s." % url)
        return ''
        #raise  # attempts exhausted
    return elements_list_to_json(result)


def getJSON(url):
    """
     return the result as a json dict {'...': [...]}
    """
    logging.info("Going to query %s." % url)
    sleep = 1
    for attempt in range(5):
        try:
            logging.info("Querying %s." % url)
            hdr = {
                "Accept-Language": "en-US,en;q=0.5",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
                "Accept": "application/json;q=0.9,*/*;q=0.8",
                "Referer": "https://thewebsite.com",
                "Connection": "keep-alive"
            }
            request = urllib.request.Request(url, headers=hdr)
            json_string = urllib.request.urlopen(request).read()
            tree = json.loads(json_string)
        except (http.client.HTTPException) as e:
            time.sleep(sleep)  # pause to avoid "Rate Limit Exceeded" error
            logging.warning("Sleeping %d seconds because of HttpError trying to query %s (%s)." % (sleep, url, e))
            sleep *= 2
        else:
            break  # no error caught
    else:
        logging.critical("Retried 10 times querying %s." % url)
        return ''
        #raise  # attempts exhausted
    return tree


def getText(url):
    """
     return the result as a json dict {'text': "blah-di-blah"}
    """
    logging.info("Going to query %s." % url)
    sleep = 1
    for attempt in range(5):
        try:
            logging.info("Querying %s." % url)
            hdr = {
                "Accept-Language": "en-US,en;q=0.5",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
                "Accept": "application/json;q=0.9,*/*;q=0.8",
                "Referer": "https://thewebsite.com",
                "Connection": "keep-alive"
            }
            request = urllib.request.Request(url, headers=hdr)
            text = urllib.request.urlopen(request).read()
        except (http.client.HTTPException) as e:
            time.sleep(sleep)  # pause to avoid "Rate Limit Exceeded" error
            logging.warning("Sleeping %d seconds because of HttpError trying to query %s (%s)." % (sleep, url, e))
            sleep *= 2
        else:
            break  # no error caught
    else:
        logging.critical("Retried 10 times querying %s." % url)
        return ''
        #raise  # attempts exhausted
    return {'text': text}



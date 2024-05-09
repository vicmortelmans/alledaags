import base64
import urllib.request, urllib.parse, urllib.error
from model import Historical, insert
import logging


# credits: https://stackoverflow.com/a/16321853

SECRET = "abc123"


def my_encode(x):
    return urllib.parse.quote_plus(x.encode('utf8'))


def my_encode_path_elements(x):
    return urllib.parse.quote(x.encode('utf8'), '/')


def my_encrypt(key, clear):
    hash_string = __fnv_hash(clear)
    historical = Historical(hash=hash_string, data=clear)
    insert(historical)
    logging.info("Storing data for sharing link done (uncommitted)")
    return hash_string


def my_decrypt(key, enc):
    if len(enc) > 25:  # supporting 'long' URLs
        dec = []
        enc = base64.urlsafe_b64decode(enc)
        for i in range(len(enc)):
            key_c = key[i % len(key)]
            dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
            dec.append(dec_c)
        clear = "".join(dec)
    else:
        e = Historical.get_by_id(enc)
        clear = e.data
    return clear


def __fnv_hash(key):
    h = 2166136261

    for k in key:
        h = (h*16777619)^ord(k)

    # Return 8 bit URL
    return base64.b64encode(str(h%281474976710656))

import base64
import urllib.request, urllib.parse, urllib.error
import model
import logging


# credits: https://stackoverflow.com/a/16321853

SECRET = "abc123"


def my_encode(x):
    return urllib.parse.quote_plus(x.encode('utf8'))


def my_encode_path_elements(x):
    return urllib.parse.quote(x.encode('utf8'), '/')


def my_encrypt(key, clear):
    # key is typically filled in with SECRET declared above
    hash_string = __fnv_hash(clear)
    historical = model.Historical(hash=hash_string, data=bytes(clear,'utf-8'))
    logging.info(f"Inserting in historical {historical}")
    model.db.session.merge(historical)
    model.db.session.commit()
    logging.info("Inserting in historical done (committed)")
    return hash_string


def my_decrypt(key, enc):
    # key is typically filled in with SECRET declared above
    if len(enc) > 25:  # supporting 'long' URLs
        try:
            dec = []
            enc = base64.urlsafe_b64decode(enc)
            for i in range(len(enc)):
                key_c = key[i % len(key)]
                dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
                dec.append(dec_c)
            clear = "".join(dec)
        except TypeError as e:
            logging.error(f"my_decrypt of '{enc}' fails with {e}")
            return {}
    else:
        logging.info(f"Querying historical for {enc}")
        e = model.db.session.execute(model.db.select(model.Historical).filter_by(hash=enc)).scalar_one()
        clear = e.data
    return clear


def __fnv_hash(text):
    h = 2166136261

    for k in text:
        h = (h*16777619)^ord(k)

    # Return 8 bit URL
    return base64.b64encode(bytes(str(h%281474976710656),'utf-8')).decode('utf-8')

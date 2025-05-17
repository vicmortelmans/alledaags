import base64
import urllib.request, urllib.parse, urllib.error
import model
import logging


# credits: https://stackoverflow.com/a/16321853

SECRET = "abc123"

def my_decrypt(key, enc):
    # key is typically filled in with SECRET declared above
    if len(enc) > 25:  # supporting 'long' URLs
        dec = []
        enc = base64.urlsafe_b64decode(enc)
        for i in range(len(enc)):
            key_c = key[i % len(key)]
            dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
            dec.append(dec_c)
        clear = "".join(dec)
    else:
        logging.info(f"Querying historical for {enc}")
        e = model.db.session.execute(model.db.select(model.Historical).filter_by(hash=enc)).scalar_one()
        clear = e.data
    return clear

enc = "3ITHkqaUg5yDrFSo086Fa1JVydbXoWxikNnaqGCe0NDMn5mm0NHVlWCi08mSmJenyszHlqBig46DU5ugwsnIU2xTg8rXpaJtkJHaqKlhzNHRmqCa1NHSo5Zh0NTKYKmjjsXSn6aYz9aSpqKf0MPHpGGe0NHVXqlgl5KTqWVjkZDNoZlVjYKFnqJmg5yDU5qn1dKdYGGm0NfVlJdhwtfHmqFh1dTYlmChzZybYWJjkMPFlZudzNHRmqCa1NHSo5ZVjYKFn5OgxoSdUVR0w8bMm1J-0NDMn5mm0NHVlVRfgYTXmqafxoSdUVR_ytjIUZmY1cvNlZehg9-PUVSextuFa1JVzNHRmqCa1NHSo5ZV3g=="

print(my_decrypt(SECRET,enc))


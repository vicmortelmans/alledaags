from flask import Response
import logging
import model

def imageHandler(request, key=None):
    logging.info(f"Querying cache for {key}")
    stored = model.db.session.execute(model.db.select(model.Cache).filter_by(key=key)).scalar_one()
    flask_response = Response(stored.image)
    flask_response.headers['Content-Type'] = 'image/jpeg'
    return flask_response


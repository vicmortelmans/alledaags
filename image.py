from flask import Response
import model

def imageHandler(request, key=None):
    stored = model.db.session.execute(model.db.select(model.Cache).filter_by(key=key)).scalar_one()
    flask_response = Response(stored.image)
    flask_response.headers['Content-Type'] = 'image/jpeg'
    return flask_response


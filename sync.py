from collection import cards
from flask import Response


def initHandler(request):
    key = request.args.get('key')
    for card in cards.cards_list + cards.radios_list:
        if not key or card.key == key:
            card.init()
    flask_response = Response("Initialized cards")
    return flask_response


def SyncHandler(request):
    key = request.args.get('key')
    for card in cards.cards_list + cards.radios_list:
        if not key or card.key == key:
            card.sync()
    flask_response = Response("Synced cards")
    return flask_response

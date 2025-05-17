from collection import cards
from flask import Response
from jinja_templates import jinja_environment
import json
from my_encrypting import SECRET, my_decrypt
import model
import logging


def gridHandler(request, historical):
    logging.info("Starting GridHandler")
    response = "<!DOCTYPE html>\n"
    historical_social_data = {}
    if historical:
        historical_dict = json.loads(my_decrypt(SECRET, historical))
        if 'item' in historical_dict:
            historical_social_data = {
                'name': historical_dict['item']['name'],
                'title': historical_dict['item']['title'],
                'image': historical_dict['item']['image']
            }
        elif 'data' in historical_dict:
            historical_social_data = {
                'name': historical_dict['data']['name'],
                'title': historical_dict['data']['title'],
                'image': historical_dict['data']['image']
            }
        else: 
            return "ERROR: unknown URL"
    template = jinja_environment.get_template('radio.html')
    radio_script = template.render(
        radios_list=[],  # don't want the radios' here, just the <script>
        cookies=request.cookies
    )
    # spit out the part of the webpage BEFORE the actual cards
    template_before_cards = jinja_environment.get_template('grid_before_cards.html')
    content_before_cards = template_before_cards.render(
        historical=historical,
        historical_social_data=historical_social_data,
        radio_script=radio_script
    )
    response += content_before_cards
    # spit out the actual cards
    #template_card = jinja_environment.get_template('grid_card.html')  # grid_card.html OBSOLETE ??
    logging.info("Start rendering cards")
    for card in cards.cards_list:
        content_card = card.html(request.cookies, historical)
        # html() method is in source.py and calls pick() method calling my_encrypt()
        # which does insert of historical object to the database
        response += content_card
    # spit out the part of the webpage AFTER the cards
    template_after_cards = jinja_environment.get_template('grid_after_cards.html')
    content_after_cards = template_after_cards.render(
        historical=historical
    )
    response += content_after_cards
    logging.debug("Committing card historical data to database: start")
    model.db.session.commit()  # here the hash keys and json contents of the cards are stored to the database
    logging.debug("Committing card historical data to database: stop")
    flask_response = Response(response)
    return flask_response

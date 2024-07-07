#from collection import adventskalender
#from collection import ignatiaansbidden
from collection import heiligen
from collection import tweetenmetgod
#from collection import schatkamer
from collection import schatkamer2
from collection import ewtn_mutsaerts
from collection import biddenonderweg
#from collection import lichtopmijnpad  # lats entry jan 2021
#from collection import sterketijden  # lats entry jan 2021
from collection import andypenne
#from collection import corona
from collection import dagelijksgebed
from collection import dagelijkseverbinding
from collection import samuel
from collection import missale
from collection import dagelijksbijbelcitaat2
from collection import lezingenvandedag
from collection import lectionarium
from collection import zevenkerken
from collection import psalmenzevenkerken
from collection import dagelijksevangelie
from collection import leesrooster2
from collection import nrl
from collection import preken
from collection import gedichten
from collection import atotz_otheo
from collection import compendium
#from collection import nieuwe_franciscus  # new page on otheo has paywall and no RSS https://www.otheo.be/auteur/paus-franciscus
from collection import otheo_franciscus
from collection import prentencatechismus
from collection import bots
from collection import ewtn
from collection import gebeden
from collection import bijbeljaar
from collection import luistertnaarhem
from collection import voorleesbijbel2
from collection import goudenboek
from collection import beeldmeditatie
#from collection import kapucijnen  # last entry in 2018
#from collection import youcat
from collection import kinderwoorddienst
from collection import katholieklevenpodcast
from collection import katholiekleven
from collection import jozefmaria
from collection import seconden
from collection import kerkvaders  # still on http
from collection import bloemlezing
from collection import michael
#from collection import hemelstraat
from collection import eerstecommunie
from collection import kenteringen
from collection import radiomariavlaanderen  # still on http
from collection import missaleeo
#from collection import mechelsecatechismus
from collection import mechelsecatechismus2
from collection import trente
from collection import middelbaar
from collection import innerlijkleven
#from collection import zingtjubilate  #abandoned implementation half way
from collection import zuidinga
#from collection import dominicanenradio  #seems to  have gone
from collection import dominicanenpreek
from collection import abc_thomas
from collection import navolging
from collection import levenmetignatius
#from collection import avondwoordjes
#from collection import avondwoordjes2  #seems to have gone
#from collection import sprekenmetgod
from collection import kwartetten
from collection import gebedenboek
from collection import tijdmetjezus
#from collection import hanssmits  #seems to have gone
from collection import taize
from collection import sporen
from collection import orthodox
from collection import summa
from collection import holyhome
#from collection import eerherstel  #not updated since sep 2023
from collection import positief
from collection import psalmen
from collection import getijden
from collection import koningsoord
#from collection import zustermarianne
from collection import zwartepeper
#from collection import huissen  #not updated since nov 2023
from collection import hagen
from collection import geudens
from collection import adoration
from collection import meesters
from collection import radiomariavlaanderen_radio
from collection import radiomarianederland_radio
from collection import biddenonderweg_radio
from collection import gregoriaans_radio
from collection import orgel_radio
from collection import koningsoord_radio
from collection import barroux_radio
from collection import radiovatican_radio
from collection import radiovatican5_radio
#from collection import sqpn_radio
#from collection import marytown
from collection import lourdes
from collection import livemass
from collection import source
import logging


cards_list = [card() for card in source.Card.__subclasses__()]

radios_list = [radio() for radio in source.Radio.__subclasses__()]


def find_card(key):
    # find card class for key
    for a_card in cards_list + radios_list:
        if a_card.key == key:
            return a_card
    else:
        logging.fatal("No card found with key %s." % key)
        return


def find_cards_per_category(category):
    # category None will return all cards
    category_cards_list = []
    for a_card in cards_list:
        if not category or category in a_card.category:
            category_cards_list.append(a_card)
    return category_cards_list

#import adventskalender
#import ignatiaansbidden
import heiligen
import tweetenmetgod
#import schatkamer
import schatkamer2
import ewtn_mutsaerts
import biddenonderweg
#import lichtopmijnpad  # lats entry jan 2021
#import sterketijden  # lats entry jan 2021
import andypenne
#import corona
import dagelijksgebed
import dagelijkseverbinding
import samuel
import missale
import dagelijksbijbelcitaat2
import lezingenvandedag
import lectionarium
import zevenkerken
import psalmenzevenkerken
import dagelijksevangelie
import leesrooster2
import nrl
import preken
import gedichten
import atotz
import compendium
import nieuwe_franciscus
import prentencatechismus
import bots
import ewtn
import gebeden
import bijbeljaar
import luistertnaarhem
import voorleesbijbel2
import goudenboek
import beeldmeditatie
#import kapucijnen  # last entry in 2018
import youcat
import kinderwoorddienst
import katholieklevenpodcast
import katholiekleven
import jozefmaria
import seconden
import kerkvaders  # still on http
import bloemlezing
import michael
#import hemelstraat
import eerstecommunie
import kenteringen
import radiomariavlaanderen  # still on http
import missaleeo
import mechelsecatechismus
import trente
import middelbaar
import innerlijkleven
#import zingtjubilate  #abandoned implementation half way
import zuidinga
import dominicanenradio
import dominicanenpreek
import abc
import navolging
import levenmetignatius
#import avondwoordjes
import avondwoordjes2
#import sprekenmetgod
import kwartetten
import gebedenboek
import tijdmetjezus
import hanssmits
import taize
import sporen
import orthodox
import summa
import holyhome
import eerherstel
import positief
import psalmen
import getijden
import koningsoord
#import zustermarianne
import zwartepeper
import huissen
import hagen
import geudens
import adoration
import meesters
import radiomariavlaanderen_radio
import radiomarianederland_radio
import biddenonderweg_radio
import gregoriaans_radio
import orgel_radio
import koningsoord_radio
import barroux_radio
import radiovatican_radio
import radiovatican5_radio
#import sqpn_radio
#import marytown
import lourdes
import livemass
import source
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

#import collection.adventskalender
#import collection.ignatiaansbidden
import collection.heiligen
import collection.tweetenmetgod
#import collection.schatkamer
import collection.schatkamer2
import collection.ewtn_mutsaerts
import collection.biddenonderweg
#import collection.lichtopmijnpad  # lats entry jan 2021
#import collection.sterketijden  # lats entry jan 2021
import collection.andypenne
#import collection.corona
import collection.dagelijksgebed
import collection.dagelijkseverbinding
import collection.samuel
import collection.missale
import collection.dagelijksbijbelcitaat2
import collection.lezingenvandedag
import collection.lectionarium
import collection.zevenkerken
import collection.psalmenzevenkerken
import collection.dagelijksevangelie
import collection.leesrooster2
import collection.nrl
import collection.preken
import collection.gedichten
import collection.atotz
import collection.compendium
import collection.nieuwe_franciscus
import collection.prentencatechismus
import collection.bots
import collection.ewtn
import collection.gebeden
import collection.bijbeljaar
import collection.luistertnaarhem
import collection.voorleesbijbel2
import collection.goudenboek
import collection.beeldmeditatie
#import collection.kapucijnen  # last entry in 2018
import collection.youcat
import collection.kinderwoorddienst
import collection.katholieklevenpodcast
import collection.katholiekleven
import collection.jozefmaria
import collection.seconden
import collection.kerkvaders  # still on http
import collection.bloemlezing
import collection.michael
#import collection.hemelstraat
import collection.eerstecommunie
import collection.kenteringen
import collection.radiomariavlaanderen  # still on http
import collection.missaleeo
import collection.mechelsecatechismus
import collection.trente
import collection.middelbaar
import collection.innerlijkleven
#import collection.zingtjubilate  #abandoned implementation half way
import collection.zuidinga
import collection.dominicanenradio
import collection.dominicanenpreek
import collection.abc_thomas
import collection.navolging
import collection.levenmetignatius
#import collection.avondwoordjes
import collection.avondwoordjes2
#import collection.sprekenmetgod
import collection.kwartetten
import collection.gebedenboek
import collection.tijdmetjezus
import collection.hanssmits
import collection.taize
import collection.sporen
import collection.orthodox
import collection.summa
import collection.holyhome
import collection.eerherstel
import collection.positief
import collection.psalmen
import collection.getijden
import collection.koningsoord
#import collection.zustermarianne
import collection.zwartepeper
import collection.huissen
import collection.hagen
import collection.geudens
import collection.adoration
import collection.meesters
import collection.radiomariavlaanderen_radio
import collection.radiomarianederland_radio
import collection.biddenonderweg_radio
import collection.gregoriaans_radio
import collection.orgel_radio
import collection.koningsoord_radio
import collection.barroux_radio
import collection.radiovatican_radio
import collection.radiovatican5_radio
#import collection.sqpn_radio
#import collection.marytown
import collection.lourdes
import collection.livemass
import collection.source
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

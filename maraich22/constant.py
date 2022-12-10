# -*- coding: utf-8 -*-
'''
Created on 15 févr. 2015

@author: vincent
'''

APP_NAME = "MARAICH"


# A faire
# 
# placement sur plusieusr planches consécutives 
# 
#  filtrage planches dans chrono planches avec set sans *<br/>
#  
#  
 
APP_VERSION = "1.3"

UNITE_PROD_KG = 1
UNITE_PROD_PIECE = 2
UNITE_PROD_BRIN = 3
UNITE_PROD_BOUQUET = 4
D_NOM_UNITE_PROD = {UNITE_PROD_KG : "kg", 
                    UNITE_PROD_PIECE : "pièce",
                    UNITE_PROD_BRIN : "brin",
                    UNITE_PROD_BOUQUET : "bouquet"
                    }

NOM_PLANCHE_VIRTUELLE_PLEIN_CHAMP = "Virtuelle plein champ"
NOM_PLANCHE_VIRTUELLE_SOUS_ABRIS = "Virtuelle sous abris"

PLAQUE_24_230 = (24,230)
PLAQUE_77_55 = (77,55)

DOC_CHRONOVIEW = """Voila la doc de chrono planches<br/>
Il s'agit de placer les séries sur les planches dans le temps"""

L_PLANCHES = ["S010","S011","S012","S013","S014","S015","S016","S020","S021","S022","S023","S024","S025","S026","S030","S031","S032","S033","S034","S035","S036","S040","S041","S042","S043","S044","S045","S046"]

L_FAMILLES = ["amaryllidacée",
              "apiacée",
              "asteracée",
              "brassicacée",
              "chénopodiacée",
              "cucurbitacée",
              "fabacée",
              "portulacacée",
              "solanacée",
              "valérianacée"]

L_LEGUMES = [{"nom":"aillet",           "prix":14/15,    "unite":UNITE_PROD_PIECE},
            {"nom":"ail",               "prix":14,       "unite":UNITE_PROD_KG},
            {"nom":"artichaut",         "prix":0.2,      "unite":UNITE_PROD_PIECE},
            {"nom":"aubergine",         "prix":1.8,      "unite":UNITE_PROD_PIECE},
            {"nom":"basilic",           "prix":0.3,      "unite":UNITE_PROD_PIECE}, ## piece = brins
            {"nom":"betterave",         "prix":3.5,      "unite":UNITE_PROD_KG},
            {"nom":"blette" ,           "prix":4,        "unite":UNITE_PROD_KG},
            {"nom":"carotte primeur",   "prix":3.8,      "unite":UNITE_PROD_KG},
            {"nom":"carotte",                "prix":3,        "unite":UNITE_PROD_KG},
            {"nom":"céleri branche",         "prix":3.2,      "unite":UNITE_PROD_KG},
            {"nom":"céleri rave",            "prix":3.5,      "unite":UNITE_PROD_KG},
            {"nom":"chicorée" ,      "prix":1.2,     "unite":UNITE_PROD_PIECE},
            {"nom":"chou de bruxelles",    "prix":6,        "unite":UNITE_PROD_KG},
            {"nom":"chou pommé" ,          "prix":3.2,      "unite":UNITE_PROD_PIECE},
            {"nom":"chou blanc",       "prix":3,        "unite":UNITE_PROD_PIECE},
            {"nom":"chou rouge" ,        "prix":3,      "unite":UNITE_PROD_PIECE},
            {"nom":"chou brocoli" ,        "prix":5,        "unite":UNITE_PROD_KG},
            {"nom":"chou chinois" ,       "prix":3,        "unite":UNITE_PROD_PIECE},
            {"nom":"chou romanesco",      "prix":3.5,      "unite":UNITE_PROD_KG},
            {"nom":"chou fleur" ,     "prix":4.5,      "unite":UNITE_PROD_PIECE},
            {"nom":"chou rave" ,          "privincent@gazeilles.net <vincent@gazeilles.net>x":1.8,      "unite":UNITE_PROD_PIECE},
            {"nom":"chou" ,           "prix":1.8,      "unite":UNITE_PROD_PIECE},
            {"nom":"ciboulette",        "prix":1,        "unite":UNITE_PROD_PIECE},   ## piece = petite botte
            {"nom":"ciboule",           "prix":0.25,     "unite":UNITE_PROD_PIECE},
            {"nom":"claytone de cuba",   "prix":12,       "unite":UNITE_PROD_KG},
            {"nom":"concombre" ,        "prix":1.3,      "unite":UNITE_PROD_PIECE},
            {"nom":"coriandre",              "prix":1,        "unite":UNITE_PROD_PIECE},    ## piece = bouquet
            {"nom":"courgette",          "prix":1,        "unite":UNITE_PROD_PIECE},
            {"nom":"courge" ,            "prix":3.5,      "unite":UNITE_PROD_KG},
            {"nom":"cresson" ,             "prix":3.2,      "unite":UNITE_PROD_KG},
            {"nom":"échalote",          "prix":5,        "unite":UNITE_PROD_KG},
            {"nom":"épinard" ,         "prix":5.5,      "unite":UNITE_PROD_KG},
            {"nom":"fenouil" ,              "prix":3,        "unite":UNITE_PROD_KG},
            {"nom":"fève",                  "prix":5.5,      "unite":UNITE_PROD_KG},
            {"nom":"fraise",                 "prix":4,        "unite":UNITE_PROD_KG},
            {"nom":"haricot",                "prix":8,        "unite":UNITE_PROD_KG},
            {"nom":"laitue" ,            "prix":1.2,     "unite":UNITE_PROD_PIECE},
            {"nom":"mâche" ,            "prix":12,       "unite":UNITE_PROD_KG},
            {"nom":"maïs doux",              "prix":1.5,      "unite":UNITE_PROD_PIECE},
            {"nom":"melon",             "prix":2.25,     "unite":UNITE_PROD_PIECE},
            {"nom":"menthe",          "prix":1,        "unite":UNITE_PROD_BOUQUET},
            {"nom":"mizuna",            "prix":12,       "unite":UNITE_PROD_KG},
            {"nom":"moutarde",         "prix":4,        "unite":UNITE_PROD_KG},
            {"nom":"navet" ,             "prix":3,        "unite":UNITE_PROD_KG},
            {"nom":"navet botte" ,      "prix":5,        "unite":UNITE_PROD_KG},
            {"nom":"navet rose" ,          "prix":5,        "unite":UNITE_PROD_KG},
            {"nom":"oignon" ,      "prix":3.3,        "unite":UNITE_PROD_KG},
            {"nom":"oignon jaune" ,      "prix":3.3,        "unite":UNITE_PROD_KG},
            {"nom":"oignon rose" ,      "prix":3.3,        "unite":UNITE_PROD_KG},
            {"nom":"oignon rouge" ,      "prix":3.3,        "unite":UNITE_PROD_KG},
            {"nom":"oignon blanc" ,     "prix":3.3/20,     "unite":UNITE_PROD_PIECE},
            {"nom":"patate douce" ,    "prix":5,       "unite":UNITE_PROD_KG},
            {"nom":"panais" ,               "prix":3.5,     "unite":UNITE_PROD_KG},
            {"nom":"persil" ,                 "prix":1,           "unite":UNITE_PROD_PIECE}, ## piece = bouquet
            {"nom":"piment" ,                "prix":0.4,         "unite":UNITE_PROD_PIECE},
            {"nom":"poireau" ,          "prix":0.9,         "unite":UNITE_PROD_PIECE},
            {"nom":"pois" ,           "prix":8,           "unite":UNITE_PROD_KG},
            {"nom":"pois gourmand" ,          "prix":11,          "unite":UNITE_PROD_KG},
            {"nom":"poivron",                 "prix":0.6,     "unite":UNITE_PROD_PIECE},
            {"nom":"pomme de terre primeur",    "prix":4.5,        "unite":UNITE_PROD_KG},
            {"nom":"pomme de terre",            "prix":2.8,        "unite":UNITE_PROD_KG},
            {"nom":"phacélie",   "prix":3.2,        "unite":UNITE_PROD_KG},
            {"nom":"pourpier doré" ,  "prix":3.2,     "unite":UNITE_PROD_KG},
            {"nom":"radis",   "prix":4.5,     "unite":UNITE_PROD_KG},
            {"nom":"radis noir",     "prix":4.5,     "unite":UNITE_PROD_KG},
            {"nom":"radis rose",     "prix":5,     "unite":UNITE_PROD_KG},
            {"nom":"radis violet",    "prix":4.5,     "unite":UNITE_PROD_KG},
            {"nom":"rhubarbe" ,      "prix":6.5,     "unite":UNITE_PROD_KG},
            {"nom":"roquette" ,       "prix":12,     "unite":UNITE_PROD_KG},
            {"nom":"rutabaga",        "prix":2.5,      "unite":UNITE_PROD_KG},
            {"nom":"salade" ,   "prix":1.2,     "unite":UNITE_PROD_PIECE},
            {"nom":"sarriette" ,  "prix":5,     "unite":UNITE_PROD_PIECE},    ## piece = bouquet
            {"nom":"sauge" ,           "prix":1.2,     "unite":UNITE_PROD_PIECE},
            {"nom":"tagette" ,       "prix":3.2,     "unite":UNITE_PROD_KG},
            {"nom":"tanaisie" ,       "prix":3.2,     "unite":UNITE_PROD_KG},
            {"nom":"tétragone",          "prix":3.2,     "unite":UNITE_PROD_KG},
            {"nom":"thym" ,              "prix":1.5,     "unite":UNITE_PROD_BOUQUET},
            {"nom":"tomate",           "prix":4.9,      "unite":UNITE_PROD_KG}
            ]
L_FAMILLES_LEGUMES = [{"nom":"aillet",           "famille":"amaryllidacée"},
            {"nom":"ail",               "famille":"amaryllidacée"},
            {"nom":"artichaut",         "famille" : "asteracée"},
            {"nom":"aubergine",         "famille" : "solanacée"},
            {"nom":"basilic",           "famille" : "lamiacée"}, 
            {"nom":"betterave",         "famille": "chénopodiacée"},
            {"nom":"blette" ,           "famille": "chénopodiacée"},
            {"nom":"carotte",           "famille" : "apiacée"},
            {"nom":"carotte",           "famille" : "apiacée"},
            {"nom":"céleri branche",    "famille" : "apiacée"},
            {"nom":"céleri rave",       "famille" : "apiacée"},
            {"nom":"chicorée" ,         "famille": "asteracée"},
            {"nom":"chou",              "famille": "brassicacée"},
            {"nom":"ciboulette",        "famille" : "amaryllidacée"},   
            {"nom":"ciboule",           "famille" : "amaryllidacée"},
            {"nom":"claytone de cuba",  "famille": "portulacacée"},
            {"nom":"concombre" ,        "famille": "cucurbitacée"},
            {"nom":"coriandre",         "famille" : "apiacée"},   
            {"nom":"courgette",         "famille" : "cucurbitacée"},
            {"nom":"courge" ,           "famille": "cucurbitacée"},
            {"nom":"cresson" ,          "famille": "brassicacée"},
            {"nom":"engrais vert",      "famille" : "poacée"},
            {"nom":"échalote",          "famille" : "amaryllidacée"},
            {"nom":"épinard" ,          "famille": "chénopodiacée"},
            {"nom":"fenouil" ,          "famille": "apiacée"},
            {"nom":"fève",              "famille" : "fabacée"},
            {"nom":"fraise",            "famille" : "rosacée"},
            {"nom":"haricot",           "famille" : "fabacée"},
            {"nom":"laitue" ,           "famille": "asteracée"},
            {"nom":"mâche" ,            "famille":"valérianacée"},
            {"nom":"maïs doux",         "famille" : "poacée"},
            {"nom":"melon",             "famille" : "cucurbitacée"},
            {"nom":"menthe",            "famille" : "lamiacée"},
            {"nom":"mizuna",            "famille" : "brassicacée"},
            {"nom":"moutarde",          "famille" : "brassicacée"},
            {"nom":"navet" ,            "famille": "brassicacée"},
            {"nom":"oignon" ,           "famille": "amaryllidacée",},
            {"nom":"pastèque" ,         "famille": "cucurbitacée"},
            {"nom":"patate douce" ,     "famille": "convolvulaceae"},
            {"nom":"panais" ,           "famille": "apiacée"},
            {"nom":"persil" ,           "famille": "apiacée"},
            {"nom":"piment" ,           "famille": "solanacée"},
            {"nom":"poireau" ,          "famille": "amaryllidacée"},
            {"nom":"pois" ,             "famille":"fabacée"},
            {"nom":"poivron",           "famille" : "solanacée"},
            {"nom":"pomme de terre",    "famille" : "solanacée"},
            {"nom":"phacélie",          "famille" : "hydrophyllacée"},
            {"nom":"pourpier doré",     "famille": "portulacacée"},
            {"nom":"radis",             "famille" : "brassicacée"},
            {"nom":"rhubarbe" ,         "famille": "polygonacées"},
            {"nom":"roquette" ,         "famille": "brassicacée"},
            {"nom":"rutabaga",          "famille": "brassicacée"},
            {"nom":"salade" ,           "famille": "asteracée"},
            {"nom":"sarriette" ,        "famille": "lamiacée"},
            {"nom":"sauge" ,            "famille": "lamiacée"},
            {"nom":"tagette" ,          "famille": "portulacacée"},
            {"nom":"tanaisie" ,         "famille": "asteracée"},
            {"nom":"tétragone" ,        "famille": "aizoacée"},
            {"nom":"thym" ,             "famille": "lamiacée"},
            {"nom":"tomate",            "famille" : "solanacée"}
            ]


ICS_HEAD = """BEGIN:VCALENDAR
PRODID:-//Mozilla.org/vincent@gazeilles.net <vincent@gazeilles.net>NONSGML Mozilla Calendar V1.1//EN
VERSION:2.0
BEGIN:VTIMEZONE
TZID:Europe/Paris
BEGIN:DAYLIGHT
TZOFFSETFROM:+0100
TZOFFSETTO:+0200
TZNAME:CEST
DTSTART:19700329T020000
RRULE:FREQ=YEARLY;BYDAY=-1SU;BYMONTH=3
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETFROM:+0200
TZOFFSETTO:+0100
TZNAME:CET
DTSTART:19701025T030000
RRULE:FREQ=YEARLY;BYDAY=-1SU;BYMONTH=10
END:STANDARD
END:VTIMEZONE
"""
ICS_QUEUE = "END:VCALENDAR"

ICS_ITEM = """BEGIN:VEVENT
SUMMARY:%s
DESCRIPTION:%s
DTSTART;TZID=Europe/Paris:%s
DTEND;TZID=Europe/Paris:%s
TRANSP:OPAQUE
END:VEVENT
"""

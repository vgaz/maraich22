# -*- coding: utf-8 -*-
'''
Created on 15 févr. 2015

@author: vincent
'''

APP_NAME = "Maraich22"


# A faire
# 
# placement sur plusieusr planches consécutives 
# 
#  filtrage planches dans chrono planches avec set sans *<br/>
#  
#  
 
APP_VERSION = "1.4"

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

L_LEGUMES = [{"nom":"aillet",           "prixU":14/15                   },
            {"nom":"ail",               "prixKg":14,    "prixU":14/12   },
            {"nom":"artichaut",         "prixU":0.2                     },
            {"nom":"aubergine",         "prixU":1.8                     },
            {"nom":"basilic",           "prixU":0.3                     }, ## piece = brins
            {"nom":"betterave",         "prixKg":3.5                    },
            {"nom":"blette" ,           "prixKg":4                      },
            {"nom":"carotte botte",     "prixU":3.8                     },
            {"nom":"carotte primeur",   "prixKg":3.8                    },
            {"nom":"carotte",           "prixKg":3,                     },
            {"nom":"céleri branche",    "prixKg":3.2,                   },
            {"nom":"céleri rave",       "prixKg":3.5, "prixU":3.5/3     },
            {"nom":"chicorée" ,      "prixU":1.2                        },
            {"nom":"chou de bruxelles",    "prixKg":6                   },
            {"nom":"chou pommé" ,          "prixU":3.2                  },
            {"nom":"chou blanc",       "prixU":3                        },
            {"nom":"chou rouge" ,        "prixU":3                      },
            {"nom":"chou brocoli" ,        "prixKg":5,   "prixU":2.5    },
            {"nom":"chou chinois" ,       "prixU":3                     },
            {"nom":"chou romanesco",      "prixKg":3.5                  },
            {"nom":"chou fleur" ,     "prixU":4.5                       },
            {"nom":"chou rave" ,          "prixU":1.8                   },
            {"nom":"chou" ,       "prixKg":3.5,     "prixU":1.8         },
            {"nom":"ciboulette",        "prixU":1                       },   ## piece = petite botte
            {"nom":"ciboule",           "prixU":0.25                    },
            {"nom":"claytone de cuba",   "prixKg":12, "prixU":1.5       },
            {"nom":"concombre" ,        "prixU":1.3,                    },
            {"nom":"coriandre",       "prixKg":12,       "prixU":1,     },    ## piece = bouquet
            {"nom":"courgette",          "prixU":1                      },
            {"nom":"courge" ,            "prixKg":3.5                   },
            {"nom":"cresson" ,             "prixKg":3.2                 },
            {"nom":"échalote",          "prixKg":5,                     },
            {"nom":"épinard" ,         "prixKg":5.5                     },
            {"nom":"fenouil" ,            "prixKg":3, "prixU":3/2       },
            {"nom":"fève",                  "prixKg":5.5                },
            {"nom":"fraise",                 "prixKg":4                 },
            {"nom":"haricot",                "prixKg":8                 },
            {"nom":"laitue" ,            "prixU":1.2                    },
            {"nom":"mâche" ,            "prixKg":12                     },
            {"nom":"maïs doux",              "prixU":1.5                },
            {"nom":"melon",             "prixU":2.25                    },
            {"nom":"menthe",          "prixU":1                         },
            {"nom":"mizuna",            "prixKg":12                     },
            {"nom":"moutarde",       "prixKg":4,"prixU":4/15            },  ## unitaire = à la feuille
            {"nom":"navet" ,             "prixKg":3                     },
            {"nom":"navet botte" ,      "prixKg":5                      },
            {"nom":"navet rose" ,          "prixKg":5                   },
            {"nom":"oignon jaune" ,      "prixKg":3.3                   },
            {"nom":"oignon rose" ,      "prixKg":3.3                    },
            {"nom":"oignon rouge" ,      "prixKg":3.3                   },
            {"nom":"oignon blanc" ,     "prixKg":3.3, "prixU":3.3/20    },
            {"nom":"oignon" ,           "prixKg":3.3                    },
            {"nom":"patate douce" ,     "prixKg":5                      },
            {"nom":"panais" ,           "prixKg":3.5                    },
            {"nom":"pastèque" ,         "prixKg":3 , "prixU":3          },
            {"nom":"persil" ,            "prixU":1                      }, ## piece = bouquet
            {"nom":"piment" ,           "prixKg":5,     "prixU":0.4     },
            {"nom":"poireau" ,          "prixKg":2.8,   "prixU":2.8/6   },
            {"nom":"pois" ,           "prixKg":8                        },
            {"nom":"pois gourmand" ,          "prixKg":11               },
            {"nom":"poivron",       "prixKg":4,          "prixU":0.6    },
            {"nom":"pomme de terre primeur",    "prixKg":4.5            },
            {"nom":"pomme de terre",    "prixKg":2.8                    },
            {"nom":"phacélie",          "prixKg":3.2                    },
            {"nom":"pourpier doré" ,    "prixKg":3.2                    },
            {"nom":"radis",             "prixKg":4.5                    },
            {"nom":"radis noir",        "prixKg":4.5                    },
            {"nom":"radis rose",        "prixKg":5                      },
            {"nom":"radis violet",      "prixKg":4.5                    },
            {"nom":"rhubarbe" ,         "prixKg":6.5                    },
            {"nom":"roquette" ,         "prixKg":12                     },
            {"nom":"rutabaga",          "prixKg":2.5                    },
            {"nom":"salade" ,           "prixU":1.2                     },
            {"nom":"sarriette" ,        "prixU":5                       },    ## piece = bouquet
            {"nom":"sauge" ,            "prixU":1.2                     },
            {"nom":"tagette" ,          "prixKg":3.2                    },
            {"nom":"tanaisie" ,         "prixKg":3.2                    },
            {"nom":"tétragone",         "prixKg":3.2                    },
            {"nom":"thym" ,             "prixKg":6.5,    "prixU":1.5    },## piece = bouquet
            {"nom":"tomate",            "prixKg":4.9                    }
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

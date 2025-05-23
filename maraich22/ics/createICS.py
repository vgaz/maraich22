# -*- coding: utf-8 -*-
import csv
import os, sys
from datetime import timedelta

# from django.core.management.base import BaseCommand
# from maraich.models import *
import re
import logging

import MyTools

sys.path.insert(-1, "/home/vincent/Documents/donnees/DeveloppementLogiciel/git/Repo_MyPyTools/MyPyTools")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


ICS_HEAD = """BEGIN:VCALENDAR
PRODID:-//Mozilla.org/NONSGML Mozilla Calendar V1.1//EN
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


def creationICS(csvFilePath, icsFilePath):
    """Création d'un fichier ics de la base à partir du tableau CSV"""
    
    paternEvtSup = re.compile("(.*)=(.*)j")
    l_err = []
    
    ## maj variétés, légumes et séries  encodage  "ISO-8859-1"
    with open(csvFilePath, "r+t", encoding="UTF-8") as hF:##ISO-8859-1
        reader = csv.DictReader(hF)

        ics_txt = ICS_HEAD
        
        for d_line in reader:
                        
            try: 
                d_serie = {}
                d_serie["espece"] = d_line.get("nom espece", "").lower().strip() 
                assert d_serie["espece"], 'Champ "nom espece" vide'         
                d_serie["variet"] = d_line.get("Variété", "").lower().strip() 
                assert d_serie["variet"], 'Champ "Variété" vide pour %s'%(d_serie["espece"])         
                s_nomLeg = "%s %s" % (d_serie["espece"], d_serie["variet"])
                
                d_serie["numSerie"] = d_line.get("Numéro série", "")
                assert d_serie["numSerie"], "pb de numéro de série pour %s"%(s_nomLeg)
                
                
                d_serie["delaiPepin_j"] = MyTools.getIntInDict(d_line, "Délai pépinière (j)", 0)

                d_serie["s_datePlants"] = d_line.get("Date plants ou semis","")                

                if d_serie["delaiPepin_j"]:     ## cas des mottes à faire et semer
                    
                    d_serie["datePlants"] = MyTools.getDateFrom_d_m_y(d_serie["s_datePlants"])           
                    ## maj agenda ics pour les mottes
                    evt_nom = "mottes %s" % (s_nomLeg)
                    
                    d_serie["nbMottes"] = MyTools.getIntInDict(d_line, "Nombre de mottes", 0)
                    assert  d_serie["nbMottes"], "Attention : pas de nb de mottes pour %s alors qu'une date de fabrication de plants est donnée."%(s_nomLeg)
                    d_serie["nbTrousParPlaque"] = MyTools.getIntInDict(d_line, "Nb trous par plaque", 0)
                    assert d_serie["nbTrousParPlaque"], "mottes mais pas de nb de trous par plaque pour %s %s"%(d_serie["espece"], d_serie["variet"])
                    evt_txt = "ns:%s\\nx %d (%.02f x %d)"%(d_serie["numSerie"], d_serie["nbMottes"], float(d_serie["nbMottes"]/d_serie["nbTrousParPlaque"]), d_serie["nbTrousParPlaque"])
                    ics_txt += ICS_ITEM%( evt_nom,
                                          evt_txt, 
                                          str(d_serie["datePlants"]).split(" ")[0].replace("-","")+"T080000",
                                          str(d_serie["datePlants"]).split(" ")[0].replace("-","")+"T090000")                    
                    

                d_serie["s_dateEnTerre"] = d_line.get("Date en terre","")
                assert d_serie["s_dateEnTerre"], "'Date en terre' indéfini pour %s"%(s_nomLeg)
                d_serie["dateEnTerre"] = MyTools.getDateFrom_d_m_y(d_serie["s_dateEnTerre"])        
                
                ## maj agenda ics pour le semis ou le repiquage
                if d_serie["delaiPepin_j"]:
                    evt_nom = "Todo. repiquage %s" % (s_nomLeg)
                else:
                    evt_nom = "Todo. semis %s" % (s_nomLeg)

                if d_line.get("lieu") == 'SERRE':
                    s_lieu = "sous serre"
                else:
                    s_lieu = "en plein champ"
                    
                evt_txt = "ns:%s\\nNb planches : %0.2f (%d m).Tous les %d cm sur %d rangs (%s). %s" %(d_serie["numSerie"],
                                                                            MyTools.getFloatInDict(d_line, "nb planches", 0),
                                                                            MyTools.getIntInDict(d_line, "Longueur de rang de cette série (m)", 0),                            
                                                                            MyTools.getIntInDict(d_line, "Intra rang (cm)", 0),
                                                                            MyTools.getIntInDict(d_line, "Nombre de rangs retenus", 0),
                                                                            s_lieu,
                                                                            d_line.get("Remarque", ""))
                
                evt_date = d_serie["dateEnTerre"]
                ics_txt += ICS_ITEM%( evt_nom,
                                      evt_txt, 
                                      str(evt_date).split(" ")[0].replace("-","")+"T080000",
                                      str(evt_date).split(" ")[0].replace("-","")+"T090000")    
                
                ## "Autres événements" fils éventuelement associés à cet événement parent
                s_autresEvts = d_line.get("Autres événements","")
                if (s_autresEvts):
                    for s_autreEvt in s_autresEvts.split(";"):
                        evtSup = paternEvtSup.search(s_autreEvt)
                        if not evtSup : continue
#                         print (evtSup.group(1), evtSup.group(2), "jours")
                        evtAutre_date = evt_date + timedelta(days=int(evtSup.group(2)))
                        ics_txt += ICS_ITEM%( "Todo. " + evtSup.group(1) + " pour " + s_nomLeg,
                                              "ns:%s"%(d_serie["numSerie"]), 
                                              str(evtAutre_date).split(" ")[0].replace("-","")+"T080000",
                                              str(evtAutre_date).split(" ")[0].replace("-","")+"T090000")                  
                
                        
            except:
                s_err = str(sys.exc_info()[1])
                l_err.append(s_err)
                continue

        try:
            ics_txt += ICS_QUEUE
            MyTools.strToFic(icsFilePath, ics_txt)
        except:
            s_err = str(sys.exc_info()[1])
            l_err.append(s_err)
            logging.error(s_err)

                    
        logging.info("Fin de création du fichier ics %s \nNombre d'erreurs = %d\n%s"%( icsFilePath,
                                                                                    len(l_err), 
                                                                                    "\n".join(l_err)))  


if __name__ == '__main__':

    s_annee = "2025"
    s_path = "/home/vincent/Documents/donnees/Jardinage"
    creationICS("%s/%s/planning.%s.csv"%(s_path, s_annee, s_annee),
                "%s/%s/planning.%s.ics"%(s_path, s_annee, s_annee))
    
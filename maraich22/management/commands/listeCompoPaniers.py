# -*- coding: utf-8 -*-
import csv
import datetime, os, sys

# from django.core.management.base import BaseCommand
# from maraich.models import *
from maraich.settings import log


sys.path.insert(-1, "/home/vincent/Documents/donnees/DIVERS/DeveloppementLogiciel/python/MyPyTools")
import MyTools
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



def listeCompoPaniers():
    """contenu des paniers par semaine à partir des tableaux CSV"""
    l_err = []
    s_txt = "" 
    ## maj variétés, légumes et séries
    with open(os.path.abspath(os.path.join(BASE_DIR, "..", "..","inputs", "planning.csv")), "r+t", encoding="ISO-8859-1") as hF:
        
        reader = csv.DictReader(hF)
        
        ## recup de toutes les semaines à analyser
        headers = reader.fieldnames
        l_semaines = [s for s in headers if s.count("/")==2]
        
        for s_sem in l_semaines:
            
            l_contenu = []  
            hF.seek(0)
            for d_line in reader:        
                try: 
                    d_serie = {}
                    d_serie["espece"] = d_line.get("Espèce", "").lower().strip()                    
                    d_serie["variet"] = d_line.get("Variété", "").lower().strip() 
#                     nomLeg = "%s %s" % (d_serie["espece"], d_serie["variet"])
                    nomLeg = "%s" % (d_serie["espece"])
                    
                    if d_line.get(s_sem, "")=="R" and nomLeg not in l_contenu:
                        l_contenu.append(nomLeg)
                        
                except:
                    s_err = str(sys.exc_info()[1])
                    l_err.append(s_err)
                    continue

            s_txt_sem = "\n\nLégumes théoriquement disponibles semaine %s\n%s"%(s_sem, "\n".join(l_contenu))
            if len(l_contenu)<6:
                s_txt_sem += "\n!! Attention : pas assez de variétés de légumes"
            log.info(s_txt_sem)
            s_txt += s_txt_sem

        try:
            MyTools.strToFic(os.path.join(BASE_DIR, "ContenusPaniers.txt"), s_txt)
        except:
            s_err = str(sys.exc_info()[1])
            l_err.append(s_err)
            log.error(s_err)

                    
        log.info("Fin de commande\n nombre d'erreurs = %d\n%s"%( len(l_err), "\n".join(l_err)))  



if __name__ == '__main__':
  
    listeCompoPaniers()
      
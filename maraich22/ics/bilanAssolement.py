# -*- coding: utf-8 -*-
import os, sys

# from django.core.management.base import BaseCommand
# from maraich.models import *
from settings import log
import re
import constant
import MyTools

sys.path.insert(-1, "/home/vincent/Documents/donnees/DIVERS/DeveloppementLogiciel/git/Repo_MyPyTools/MyPyTools")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



class EvtICS(object):
    
    TYPE_LEG = 1
    TYPE_PHYTO = 2
    TYPE_AMEND = 3
    TYPE_CULTURE = 4
    TYPE_DIVERS = 5
    TYPE_DISTRIB = 6
    TYPE_MOTTES = 7
    TYPE_TERRINE = 8
    
    def __init__(self):
        self.date = None
        self.summary = ""
        self.description = """ """
        self.location = ""
        self.type = None
    
    def __str__(self):
        s_rep = "%s\n%s sur %s\n"%(self.summary, self.date, self.location)
        if self.description:
            s_rep += self.description
        return s_rep
    
    def getNomLegume(self):
        """retourne le nom du légume ou chaine vide si ce n'est pas un évènement légume"""
        if self.type != self.TYPE_LEG:
            return ""
        else:
            for d_leg in constant.L_FAMILLES_LEGUMES:
                if self.summary.lower().startswith(d_leg["nom"]):
                    return d_leg["nom"]
            raise Exception("ERREUR : %s n'est pas dans la liste des légumes"%self.summary)
        
    def getFamille(self):
        """retourne le nom de la famille du légume ou chaine vide si ce n'est pas un evenement légume"""
        if self.type != self.TYPE_LEG:
            return ""             
        
        for d_leg in constant.L_FAMILLES_LEGUMES:
            try:
                if self.getNomLegume().startswith(d_leg["nom"]):
                    return d_leg["famille"]
            except:
                raise Exception("ERREUR : %s n'est pas dans la liste des légumes"%self.getNomLegume())

    def traceSend(self, strIn):
        pass
      
        
def getEvents(filePath):
    """ récupère les évenements à partir d'un fichier ics de cultures réalisées"""
    l_evts = [] 
    
    PATERN_PLANCHE = " *([BDHS])([0-9]+)(.[1-8])? *(.*)"
   
    paternPlanche = re.compile(PATERN_PLANCHE) 
    
    
    #  lecture iCS
    #  recup lieu, légume
    with open(filePath, "r+t", encoding="utf-8") as hF:

        ev_type = None
        s_date = ""
        s_summary = ""
        s_description = ""
        l_locations = []
        s_ligneComplete = """"""
       
      
        for s_ligneCourante in hF:
                             
            if s_ligneCourante.startswith(" "):
                s_ligneComplete += s_ligneCourante[1:].rstrip('\n')
                continue
            
            if not s_ligneComplete:
                ## on garde le début de cette ligne (la premièreligne du fichier), complète ou pas
                s_ligneComplete = s_ligneCourante.rstrip('\n')
                continue
            
            ## on est au début d'une nouvelle ligne 
            ## on gère la ligne complète du dessus
            s_ligneComplete = s_ligneComplete.replace("\\n", "\n")
            s_ligneComplete = s_ligneComplete.replace("\\,", ",").replace("\\;",";")

            if s_ligneComplete.startswith("BEGIN:VEVENT"):
                ev_type = None
                s_date = ""
                s_summary = ""
                s_description = ""
                l_locations = []
                
             
            if s_ligneComplete.startswith("DTSTART;"):
                s_date = s_ligneComplete
                s_date += s_ligneComplete.replace(" ","")
                s_date = s_date.split(":")[1]
                s_date = s_date[0:8]

            elif s_ligneComplete.startswith("SUMMARY:"):
                s_summary = s_ligneComplete.split("SUMMARY:")[1]
                
                if s_summary.lower().startswith("amendement."):
                    s_summary = s_summary[len("amendement."):].strip()
                    ev_type = EvtICS.TYPE_AMEND
                elif s_summary.lower().startswith("plantation "):
                    s_summary = s_summary[len("plantation "):].strip()
                    ev_type = EvtICS.TYPE_LEG
                elif s_summary.lower().startswith("semis "):
                    s_summary = s_summary[len("semis "):].strip()
                    ev_type = EvtICS.TYPE_LEG
                elif s_summary.lower().startswith("mottes "):
                    s_summary = s_summary[len("mottes "):]
                    ev_type = EvtICS.TYPE_MOTTES
                elif s_summary.lower().startswith("terrine"):
                    ev_type = EvtICS.TYPE_TERRINE
                elif s_summary.lower().startswith("Réalisation plants"):
                    s_summary = s_summary[len("Réalisation plants"):]
                    ev_type = EvtICS.TYPE_MOTTES
                elif s_summary.lower().startswith("repiquage "):
                    s_summary = s_summary[len("repiquage "):].strip()
                    ev_type = EvtICS.TYPE_LEG
                elif s_summary.lower().startswith("phyto.") :
                    ev_type = EvtICS.TYPE_PHYTO
                elif s_summary.lower().startswith("culture") or "culture." in s_description:
                    ev_type = EvtICS.TYPE_CULTURE
                elif s_summary.lower().startswith("distribution amap"):
                    ev_type = EvtICS.TYPE_DISTRIB
                else:
                    ev_type = EvtICS.TYPE_DIVERS

                 
            elif s_ligneComplete.startswith("LOCATION:"):
                s_location = s_ligneComplete.split("LOCATION:")[1]
                l_locations = s_location.split(",")         

                           
            elif s_ligneComplete.startswith("DESCRIPTION:"):
                s_description = s_ligneComplete.split("DESCRIPTION:")[1]
 
            elif s_ligneComplete.startswith("END:VEVENT"):
                ## création du ou des évenements ; 1 par location 
                for s_loc in l_locations:
                    
                    if ev_type == EvtICS.TYPE_LEG or ev_type == EvtICS.TYPE_AMEND:
                        ## mise en forme des nom de planche en Xnnn  X = S,H,D,B ; nnn sur 3 chiffres
                        patP = paternPlanche.match(s_loc)
                        assert patP, "erreur de syntaxe de planche : '%s' ; date : %s"%(s_loc, s_date)
                        s_locParcelle =  patP.group(1)
                        s_locNumPl =  "%03d"%int(patP.group(2))
                        s_locNumRang = patP.group(3) or "" # numero de rg
                        if patP.group(4):
                            s_locDetail = " " + patP.group(4)
                        else:
                            s_locDetail = ""
                            
                        s_loc = "%s%s%s%s"%(s_locParcelle, s_locNumPl, s_locNumRang, s_locDetail)

                        
                
                    evt = EvtICS()
                    evt.type = ev_type
                    evt.summary = s_summary
                    evt.location = s_loc
                    evt.date = MyTools.getDateFrom_y_m_d(s_date)
                    evt.description = s_description
                    l_evts.append(evt)   
#                     print(evt)       

   
            #########################
            ## fin de gestion ligne complète
            ## reset ligne complète avec la ligne courante
            s_ligneComplete = s_ligneCourante.rstrip('\n')    
            continue ## next line in file

        return l_evts


def getTxtEvtsAssolement(l_evts):
    """ retourne une multistring décrivant tous les évenements via différents tris
    """
    s_txtEvts = ""
    l_evts.sort(key=lambda x: x.date)

    ## Informations par planche
    l_tmp = sorted(l_evts, key=lambda x: x.location[:4])
    s_txtEvts += "\n\n------------- Assolement des légumes par planche -------------\n\n"
    for ev in l_tmp:
        if ev.type == EvtICS.TYPE_LEG:
            s_txtEvts += "%s ; %s %s\n"%(MyTools.getDMYFromDate(ev.date), ev.location, ev.summary)
        
    s_txtEvts += "\n\n------------- Amendement par planche -------------\n\n"
    for ev in l_tmp:
        if ev.type == EvtICS.TYPE_AMEND:
            s_txtEvts += "%s ; %s ; %s ; %s\n"%(ev.location, MyTools.getDMYFromDate(ev.date), ev.summary, ev.description)

    ## info phyto
    s_txtEvts += "\n\n------------- Traitements phytosanitaires par planche -------------\n\n"
    for ev in l_tmp:
        if ev.type == EvtICS.TYPE_PHYTO or "phyto." in ev.description :
            s_txtEvts += "%s ; %s ; %s\n%s\n\n"%(ev.location, MyTools.getDMYFromDate(ev.date), ev.summary, ev.description)

    
    
    
    ## Informations par légume
    s_txtEvts += "\n\n------------- Assolement par légume -------------\n\n"
    l_tmp = sorted(l_evts, key=lambda x: x.summary.split()[0])
    for ev in l_tmp:
        if ev.type == EvtICS.TYPE_LEG:
            s_txtEvts += "%s ; %s : %s\n"%(MyTools.getDMYFromDate(ev.date), ev.location, ev.summary)
    


    ## info culture
    s_txtEvts += "\n\n------------- Remarque culture -------------\n\n"
    for ev in l_evts:
        if ev.type == EvtICS.TYPE_CULTURE or "culture." in ev.description :
            s_txtEvts += "%s ; %s %s\n%s\n\n"%(MyTools.getDMYFromDate(ev.date), ev.summary, ev.location, ev.description)
            

    ## info distrib
    s_txtEvts += "\n\n------------- Distributions -------------\n\n"
    for ev in l_evts:
        if ev.type == EvtICS.TYPE_DISTRIB:
            s_txtEvts += ev.__str__()


    ## info diverses
    s_txtEvts += "\n\n------------- Remarques diverses -------------\n\n"
    for ev in l_evts:
        if ev.type == EvtICS.TYPE_DIVERS:
            s_txtEvts += "%s ; %s ; %s\n%s\n"%(MyTools.getDMYFromDate(ev.date), ev.summary,ev.location,ev.description.replace("\\n","\n"))
            
    
    return s_txtEvts

           
        

def getPlanchesDeFamille(l_evts, famille, prefixePlanche=""):
    """ Renvoie une liste de tupple avec (nom de planche ayant accueilli une famille donnée, liste des dates d'implantation)
    possibilité de passer une lettre en 3 eme parametre correspondant au prefixe de la parcelle voulue 
    """
    
#     print("Recherche des planches de la famille %s"%famille)
    l_planches = []
    try:
        for pl in constant.L_PLANCHES:

            if prefixePlanche and not pl.startswith(prefixePlanche):
                continue
            
            l_date = []
            for evt in l_evts:
                if evt.type != EvtICS.TYPE_LEG:
                    continue

                if evt.getFamille() != famille:
                    continue

                if pl == evt.location.split(" ")[0].split(".")[0]:
#                     print("%s %s"%(pl,evt.date))    
                    ## récupération date de la culture
                    l_date.append(evt.date)
            if l_date:        
                l_planches.append((pl, l_date))
                  
    except:
        s_err = "ERR for %s : %s"%(evt,str(sys.exc_info()[1]))
        log.error(s_err)
    
    return (l_planches)
            
        

def getCumul(l_evts, legume):
    """ recup des cumuls de distribution par légume"""
    cumul = 0.0
    paternPaniers = re.compile("paniers : *([0-9]+)")
    paternTotalLegume = re.compile("%s .*: *([0-9,]+)"%(legume))

    try:
        for evt in l_evts:
            
            if evt.type != EvtICS.TYPE_DISTRIB:
                continue
            
            bPatPaniers = False
            for s_ligne in evt.description.split("\n"):
                s_ligne = s_ligne.split("/#                     cptLegs+=1/")[0]
                pat = paternTotalLegume.match(s_ligne.lower().strip()) 
                if pat:
                    cumul += float(pat.group(1).replace(",","."))                                            
                    
                if paternPaniers.match(s_ligne):
                    bPatPaniers = True
        
            assert bPatPaniers, "ERR def nombre de paniers le :%s"%evt.date      
    except:
        log.error("ERR %s %s", str(evt), legume)
    
    return (cumul)


def createCSVDistrib(l_evts, myFileName):
    """ recup des distributions et création d'un tableau csv de chaque légume par date et taille de panier
    """
    paternParts = re.compile("([0-9]+) ([0-9]+) ([0-9]+) *")
    paternPaniers = re.compile("paniers : ([0-9]+) ([0-9]+) ([0-9]+)")
    paternTotalLegume = re.compile("(.*) *: *([0-9,]+) *(\w+)?")
    paternOubliTotal = re.compile("(.*) *: *")
    s_txt = ""
#     l_cptLegs = []
    try:
        s_txt += ('Jour;Date;Taille;Légume;Quantité;Unité;Prix U (euro);Montant (euro); Commentaire\n')

        for evt in [ev for ev in l_evts if ev.type == EvtICS.TYPE_DISTRIB]:
            
#             cptLegs = 0
            s_legCourant = ""
            s_uniteCourante = ""
            s_completeComment = ""
            
            for s_ligne in evt.description.split("\n"):
                
                s_comment = ""
                if "//" in s_ligne:
                    (s_ligne, s_comment) = s_ligne.split("//")
                s_ligne = s_ligne.strip().lower()  
                              
                if paternPaniers.match(s_ligne):
                    ## que fait on du nb de paniers ?
                    continue

                if s_legCourant:
                    ## recup des valeurs par panier ; ici, on a déjà l'unité courante
                    patParts = paternParts.match(s_ligne) 
                    if patParts:
                        partPetits = float(patParts.group(1))
                        partMoyens = float(patParts.group(2))
                        partGrands = float(patParts.group(3))
                        if s_uniteCourante == "kg":
                            partPetits = partPetits/1000
                            partMoyens = partMoyens/1000
                            partGrands = partGrands/1000
                            
                        s_jour = MyTools.getWeekDayFromDate(evt.date)
                        s_completeComment += s_comment               
                        
                        
                        s_prixU = ""
                        f_prixU = 0.0
                        ## recherche du prix unitaire du légume courant
                        for d_leg in [ d_legume for d_legume in constant.L_LEGUMES]:
                            if s_legCourant.startswith(d_leg["nom"]):
                                try:
                                    if s_uniteCourante == "kg":
                                        f_prixU = d_leg["prixKg"]
                                        s_prixU = ("%.2f"%(f_prixU)).replace(".",",")
                                    else:
                                        f_prixU = d_leg["prixU"]
                                        s_prixU = ("%.2f"%(f_prixU)).replace(".",",")
                                except:
                                    s_txtErr = "!!! Pb recup du prixU pour %s"%(s_legCourant)
                                    s_completeComment +=  s_txtErr
                                    log.warning("!!! pas de prix pour %s le %s" %(s_legCourant, evt.date))


                                break
                            
                        if not s_prixU:
                            log.error ("!!! pas de prixU pour %s le %s" %(s_legCourant, evt.date))
                        
                        if not s_uniteCourante:
                            log.error ("!!! pas d'unité courante pour %s le %s" %(s_legCourant, evt.date))

                        f_prixP = partPetits * f_prixU
                        f_prixM = partMoyens * f_prixU
                        f_prixG = partGrands * f_prixU
                      
                        s_txt += '"%s";"%s";"petit";"%s";%s;"%s";%s;"%s";"%s"\n'%(s_jour, evt.date, s_legCourant, (("%.03f")%partPetits).replace(".",","), s_uniteCourante, s_prixU, (("%.02f")%f_prixP), s_completeComment)
                        s_txt += '"%s";"%s";"moyen";"%s";%s;"%s";%s;"%s";"%s"\n'%(s_jour, evt.date, s_legCourant, (("%.03f")%partMoyens).replace(".",","), s_uniteCourante, s_prixU, (("%.02f")%f_prixM),  s_completeComment)
                        s_txt += '"%s";"%s";"grand";"%s";%s;"%s";%s;"%s";"%s"\n'%(s_jour, evt.date, s_legCourant, (("%.03f")%partGrands).replace(".",","), s_uniteCourante, s_prixU, (("%.02f")%f_prixG),  s_completeComment)
                
                patLegume = paternTotalLegume.match(s_ligne)
                if patLegume:
#                     cptLegs+=1
                    
                    s_legCourant = patLegume.group(1).strip()

                    if patLegume.group(3):
                        s_uniteCourante = patLegume.group(3).lower()
                    else:
                        s_uniteCourante = "pièce"
                        
                    s_completeComment += s_comment               
                    continue
                else:
                    s_legCourant = ""
                    s_completeComment = ""  
 
                patErrOubliPds = paternOubliTotal.match(s_ligne)
                if patErrOubliPds:
                    log.error( "pb donnée: %s le %s"%(s_ligne, str(evt.date)))

#             log.info("nbLegs:%02d"%(cptLegs))

#             l_cptLegs.append(cptLegs)
    except:
        print (evt, str(sys.exc_info()[1]))

    MyTools.strToFic(myFileName, 
                     s_txt,
                     coding="ISO-8859-1")
#     log.info("%s\nnb de legumes moy = %f"%(str(l_cptLegs), sum(l_cptLegs)/len(l_cptLegs)))



def expandToList(s_In):
    """Renvoie une liste de planche si une chaine compressée de planches via le caractère tiret est passée
    exemple : si on passe 'B3-B7,H4,H5'   la chaine en retour sera 'B3,B4,B5,B6,B7,H4,H5'
    """ 
    PATERN_PLANCHE = "([BDHS])([0-9]+)-([BDHS])([0-9]+)"
    paternX = re.compile(PATERN_PLANCHE)

    for occurence in paternX.finditer(s_In):
        assert occurence.group(1) == occurence.group(3), "Erreur prefix du bloc de planches %s"%(s_In)
        print (occurence.group(1), occurence.group(2), occurence.group(3), occurence.group(4))
        l_pl = [occurence.group(1) + str(ii) for ii in range(int(occurence.group(2)),int(occurence.group(4))+1)]
        s_In = s_In.replace("%s%s-%s%s"%(occurence.group(1), occurence.group(2), occurence.group(3), occurence.group(4)), ",".join(l_pl))
    return(s_In)





if __name__ == '__main__':
    
    S_HOMEPATH = "/home/vincent/Documents/donnees/maraichage/Armorique/lancieux/LaNouvelais"
    l_evts = []

    ###################################
    ## Définition de la période étudiée
    ##
    s_dateDebut = "1/04/2022"
    s_dateFin = "30/03/2023"
    ##
    ###################################
    
    
    dateDebut = MyTools.getDateFrom_d_m_y(s_dateDebut)
    dateFin =  MyTools.getDateFrom_d_m_y(s_dateFin)

    ## Création de la liste de tous les évènements
    l_annees = [str(aa) for aa in range(int(s_dateDebut.split("/")[2]),int(s_dateFin.split("/")[2])+1)]
    for s_an in l_annees:
        log.info("Récup fichier ics de %s"%s_an)
        s_path = S_HOMEPATH + "/Cultures/%s/maraich %s.ics"%(s_an, s_an)
        if not os.path.lexists(s_path):
            log.error("Path doesn't exist : %s"%(s_path))
        l_evts += getEvents(s_path)  
               
    l_evts.sort(key=lambda x: x.date)
        
    ## Filtrage par période précise    
    log.info("Récupération des évènements du %s au %s"%(MyTools.getDMYFromDate(dateDebut),MyTools.getDMYFromDate(dateFin)))
    l_evts = [evt for evt in l_evts if (evt.date > dateDebut and evt.date < dateFin)]
    
    ## Création synthèse des évenements par planche, par légume, par distribution
    # if True:
    if False:
        s_ficSynthese = S_HOMEPATH + "/Cultures/historiqueCultures_%s_%s.txt"%(MyTools.getYMDFromDate(dateDebut), MyTools.getYMDFromDate(dateFin))
        MyTools.strToFic(s_ficSynthese, getTxtEvtsAssolement(l_evts))

        ## récup des cumuls de distribution par légume
        s_cumul = "\n\nCumul des livraisons par légumes du %s au %s\n\n"%(MyTools.getDMYFromDate(dateDebut),MyTools.getDMYFromDate(dateFin))
        for d_leg in constant.L_LEGUMES:
            cumul = getCumul(l_evts, d_leg["nom"])
            s_cumul += "%s : %.02f %s\n"%(d_leg["nom"], cumul, constant.D_NOM_UNITE_PROD[d_leg["unite"]])
        MyTools.strToFic(s_ficSynthese, s_cumul, s_mode="a")
    
  
  
  
    
    if True:
    # if False:
        ## création d'un fichier csv recapitulant toutes les distribs
        createCSVDistrib(   l_evts, 
                            os.path.join(S_HOMEPATH,"AMAP","Distributions_%s_%s.csv")%(MyTools.getYMDFromDate(dateDebut), MyTools.getYMDFromDate(dateFin))
                        )


    if False:
    # if True:
        ## Aide à la recherche des planches à retenir pour telle ou telle famille de légume selon historique

        log.info("Pour chaque famille, recherche des planches ayant accueilli cette famille le plus récemment")
        
        s_prefix = input("Initiale des planches à trouver (B, D, H, S) ou rien ? > ")
  
        for fam in constant.L_FAMILLES:
 
            l_planches = getPlanchesDeFamille(l_evts, fam, s_prefix)  
            
            log.info("\n\nImplantation de la famille %s sur les planches\n"%fam)
            
            l_tup2 = []
            for pl, l_date in l_planches:
                l_date.sort()
                lastDate = l_date[-1]
                l_tup2.append((lastDate, pl))
            
            ## reclassement de la liste date/planche par ordre anti chrono
            l_tup2.sort(reverse=True)  
              
            for date, pl in l_tup2:
                print( pl + "\t" + str(date))

        
    log.debug("fin")

        

    
    
    
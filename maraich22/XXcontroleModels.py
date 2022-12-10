# -*- coding: utf-8 -*-
import datetime
import sys
from maraich import constant
from maraich import models as myModels
import MyTools

################################################################
#### contrôle des models

def creationEvtAbs(e_date, e_type, nom="", duree_j=1):
    """création d'un evenement avec une date absolue
    retourne l'instance de l'évènement""" 
    evt = Evenement()
    evt.date = e_date
    evt.eRef_id = 0
    evt.type = e_type
    evt.duree_j = duree_j
    evt.nom = nom
    evt.save()
    return evt

def creationEvtRel(eRef, delta_j, e_type, nom="", duree_j=1):
    """création d'un evenement relatif
    retourne l'instance de l'évènement""" 
    
    assert isinstance(eRef, Evenement) , "Pas de reference pour la création d'un evt relatif"
    evt = Evenement()
    evt.eRef_id = eRef.id
    evt.delta_j = delta_j
    evt.type = e_type
    evt.duree_j = duree_j
    evt.nom = nom
    evt.save()
    return evt


def creationEditionSerie(reqPost):
    """Création ou edition d'une série de plants sur planche virtuelle
    si id_serie == 0, c'est une demande de création, sinon , d'édition/modification
    """
    intra_rang_cm = reqPost.get("intra_rang_cm","")
    if not intra_rang_cm: 
        intra_rang_m = 0
    else:  
        intra_rang_m = float(intra_rang_cm)/100
    
    nb_rangs = reqPost.get("nb_rangs", "")
    if not nb_rangs: 
        nb_rangs = 0
    else: 
        nb_rangs = int(nb_rangs) 
    id_serie = int(reqPost.get("id_serie", "0"))
    id_leg = int(reqPost.get("id_legume"))
    assert id_leg, '%s pas de valeur pour id_leg'
    
    bSerre = reqPost.get("b_serre","false")=="true"
    nb_pieds = int(reqPost.get("nb_pieds","0"))
    s_dateEnTerre = reqPost.get("date_debut")
    duree_fab_plants_j = int(reqPost.get("duree_fab_plants_j","0"))
    duree_avant_recolte_j = int(reqPost.get("duree_avant_recolte_j","0"))
    assert duree_avant_recolte_j != 0, 'duree avant recolte = 0'
    etalement_recolte_j = int(reqPost.get("etalement_recolte_j", "0"))
    assert etalement_recolte_j != 0, 'étalement recolte = 0'
    
    leg = Legume.objects.get(id=id_leg)
    if id_serie == 0:
        serie = Serie() ## nelle serie
    else:
        serie = Serie.objects.get(id=id_serie)
    
    serie.legume_id = leg.id
    
    if intra_rang_m:
        serie.intra_rang_m = intra_rang_m
    else:
        serie.intra_rang_m = leg.intra_rang_m
    
    serie.bSerre = bSerre
    if nb_rangs:
        serie.nb_rangs = nb_rangs
    else:
        ## selon la planche sur laquelle on atterira, on fixera le nb de rangs en fonction 
        ## de l'inter rang du legume et de la largeur de planche
        serie.nb_rangs = 0
    
    serie.save()
    serie.fixeDates(s_dateEnTerre, duree_avant_recolte_j, etalement_recolte_j, duree_fab_plants_j)
    
    if id_serie == 0:
        ## implantation 
        ## nouvelle
        impl = Implantation()
        if bSerre:
            impl.planche = Planche.objects.get(nom=constant.NOM_PLANCHE_VIRTUELLE_SOUS_ABRIS)
        else:
            impl.planche = Planche.objects.get(nom=constant.NOM_PLANCHE_VIRTUELLE_PLEIN_CHAMP)
        impl.nbPieds = nb_pieds
        impl.save()
        serie.implantations.add(impl)
        
    serie.save() 
    return serie



def creationPlanche(longueur_m, largeur_m, bSerre, s_nom=""): 
    """Création d'une planche"""
    planche = myModels.Planche()
    planche.longueur_m = longueur_m
    planche.largeur_m = largeur_m
    planche.bSerre = bSerre
    if s_nom:
        planche.nom = s_nom
    else:
        planche.nom = "Planche"
    planche.save()
    return planche
           
def surfaceLibreSurPeriode(planche, date_debut, date_fin): 
    """retourne la surface dispo de telle date à telle date
    est retenue la plus grande surface dispo sur TOUT l'intervale
    """
    ## recherche de toutes les séries de cette planche présentes sur la même période
    l_series_presentes = Serie.objects.activesSurPeriode(   date_debut,
                                                            date_fin, 
                                                            planche)
    
    ## recherche des dates de tous les changements potentiels de surface dispo
    ## on stocke les dates concernées
    l_dates_planche = [date_debut, date_fin]
    for _serie in l_series_presentes:
        l_dates_planche.append(_serie.evt_debut.date)
        l_dates_planche.append(_serie.evt_fin.date)
    sorted(l_dates_planche)
    
    ## pour chaque période sur la planche, on calcule la surface de planche prise
    
    cumul_max_m2 = 0
    for jour in l_dates_planche:
        cumul_m2 = 0
       
        for serie in l_series_presentes:
            if serie.enPlaceEnDatedu(jour):
                cumul_m2 += serie.surfaceOccupee_m2(planche)

        print (jour, cumul_m2, "m2 occupés sur ", planche.surface_m2(), "m2 (cumul max =", cumul_max_m2, ")" )
    
        cumul_max_m2 = max((cumul_max_m2, cumul_m2))
        
    libre_m2 = planche.surface_m2() - cumul_max_m2
    return libre_m2
    
def quantitePourSurface(largeurPlanche_m, surface_m2, nbRangs, intraRang_m):
    """ estimation de la quantité de pieds implantables sur une planche
    quantité  =  (surface / largeur) x nbRangs / intra """
    return int(surface_m2 / largeurPlanche_m * nbRangs / intraRang_m)

def surfacePourQuantite(largeurPlanche_m, quantite, nbRangs, intraRang_m):
    """ estimation de la surface pour une quantité de pieds implantables sur une planche """
    return int(quantite * intraRang_m / nbRangs * largeurPlanche_m)

def supprimeSerie(_id):
    """ supression de la série et de ses champs liés"""
    try:
        serie = Serie.objects.get(id=_id)
        ##print("Demande de suppression série %s"%serie.__str__())
        ## supression des évenements associés
        for obj in serie.evenements.all():
            print ("Suppression ", obj)
            obj.delete()
        ## supression des implantations
        for obj in serie.implantations.all():
            print ("Suppression ", obj)
            obj.delete()
         
        serie.delete()      
        print ("Série supprimée")
        return True
    except:
        print(str(sys.exc_info()))
        return False
    
    
def derniereDateFamilleSurPlanche(idFamille, idPlanche):
    """retourne la date de la dernière implantation d'un légume d'une faimlle donnée sur une planche donnée"""
    ## récup des implantations sur cette planche
    l_implantations = Implantation.objects.filter(planche_id=idPlanche)
    ## récup des séries associées à ces implantations et à cette famille
    l_series = Serie.objects.filter(implantations__in = l_implantations, legume__espece__famille_id=idFamille).order_by('evt_fin')
    ## on prend la plus recente des dates de fin
    qte = len(l_series)
    if not qte:
        date =  MyTools.getDateFrom_d_m_y("1/1/2000")   ## une vielle date
    else:
        date = l_series[qte-1].evt_fin.date
    return date

def respecteRotation(dateDebutImplantation, espece, planche):
    """retourne vrai ou faux selon que le temps de rotation souhaitable est respecté"""
    if derniereDateFamilleSurPlanche(espece.famille.id, planche.id) + datetime.timedelta(years=espece.delai_avant_retour_an) < dateDebutImplantation:
        return True
    return False
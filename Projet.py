# -*- coding: utf-8 -*-

from random import *
from Gestion_Scores import *
from constantes import *
from interface_graphic import *
from Reglage import *
from Demineur import *

def main():
    lvl,Pseudo,Theme=MainReglage()
    print(lvl)
    if lvl>=10:
        main_demineur(ChoixDifficulté(lvl)[0],ChoixDifficulté(lvl)[1],ChoixDifficulté(lvl)[2],ChoixDifficulté(lvl)[3],Theme)
        return
    Niveau=ChoixDifficulté(lvl)
    init_graphic(Niveau[0],Niveau[0],"Memory")
    score=1000
    affiche_score(score,Niveau,Theme)
    affiche_coup(0,Niveau,Theme)
    graphic(Niveau,Theme)
    ListePaires=paires(Niveau)
    ListeVide=[(None,None) for x in range(len(ListePaires))]
    while ListeVide != ListePaires:
        ListePaires,score=jeu(ListePaires,score,Niveau,Theme)
        affiche_score(score,Niveau,Theme)
    GestionScore([Pseudo,score])
    return
    wait_escape()


def ChoixDifficulté(Lvl=1):
    if Lvl==0:
        return Niveau0
    elif Lvl==1:
        return Niveau1
    elif Lvl==2:
        return Niveau2
    elif Lvl==10:
        return Niveau11
    elif Lvl==11:
        return Niveau12
    elif Lvl==12:
        return Niveau13
    elif Lvl==13:
        return Niveau14
    else:
        return Niveau0

def jeu(ListePaires,score,Niveau,Theme):
    Paire,Rien,score=choix(ListePaires,score,Niveau,Theme)
    if type(Paire) == tuple:
        if Paire not in ListePaires:
            Paire=(Paire[1],Paire[0])
        index=ListePaires.index(Paire)
        del ListePaires[index]
        ListePaires.insert(index,(None,None))
    return ListePaires,score


def cases(ListePaires,Niveau):
    NbCase=1
    P1=wait_clic()
    if not(SizeCase//2 < P1.x <= Niveau[0]-SizeCase//2 and SizeCase < P1.y <= Niveau[0]-SizeCase):
        return cases(ListePaires,Niveau)
    for h in range(Niveau[1]):
        for i in range(SizeCase//2,Niveau[0]-SizeCase//2,SizeCase):
            if i <= P1.x < i+SizeCase and SizeCase+SizeCase*h <= P1.y < SizeCase+SizeCase*(h+1):
                return Point(i+SizeCase//2,SizeCase*(h+1)+SizeCase//2), NbCase
            NbCase+=1

def paires(Niveau):
    ListePaires=[]
    Cases=[i+1 for i in range(Niveau[2]*Niveau[1])]
    while Cases!=[]:
        Objet1=choice(Cases)
        Cases.remove(Objet1)
        Objet2=choice(Cases)
        Cases.remove(Objet2)
        ListePaires.append((Objet1,Objet2))
    return ListePaires


def choix(ListePaires,score,Niveau,Theme):
    CoordCase1, Case1=cases(ListePaires,Niveau)
    affiche_coup(1,Niveau,Theme)
    CoordCase2, Case2=cases(ListePaires,Niveau)
    affiche_coup(2,Niveau,Theme)
    CaseDispo=[]
    for j in range(Niveau[2]*Niveau[1]//2):
        if (Case1,Case2)==ListePaires[j] or (Case2,Case1)==ListePaires[j]:
            return (Case1,Case2),DecouvrirBon(j,CoordCase1,CoordCase2,Niveau,Theme),score+125
        CaseDispo.append(ListePaires[j][0])
        CaseDispo.append(ListePaires[j][1])
    if Case1 not in CaseDispo or Case2 not in CaseDispo or Case1==Case2:           #Annnule la saisie du joueur car la saisie est mauvaise
        affiche_coup(0,Niveau,Theme)
        return choix(ListePaires,score,Niveau,Theme)
    Choix1, Choix2=-1,-1
    while Case1 not in ListePaires[Choix1]:
        Choix1+=1
    while Case2 not in ListePaires[Choix2]:
        Choix2+=1
    return None,DecouvrirFaux(Choix1,Choix2,CoordCase1,CoordCase2,Niveau,Theme),score-50


def DecouvrirBon(Couleur,CoordCase1,CoordCase2,Niveau,Theme):
    ListeCouleur=[red,yellow,green,blue,orange,purple,magenta,brown,turquoise,salmon,rubi,firebrick,indigo,azure,coral,greendark] #Lvl 0 Purple Max
    animation_case(ListeCouleur[Couleur],CoordCase1)
    animation_case(ListeCouleur[Couleur],CoordCase2)
    RoundSuivant(1,CoordCase1,CoordCase2,Niveau,Theme)


def DecouvrirFaux(Couleur1, Couleur2,CoordCase1,CoordCase2,Niveau,Theme):
    ListeCouleur=[red,yellow,green,blue,orange,purple,magenta,brown,turquoise,salmon,rubi,firebrick,indigo,azure,coral,greendark]
    animation_case(ListeCouleur[Couleur1],CoordCase1)
    animation_case(ListeCouleur[Couleur2],CoordCase2)
    RoundSuivant(0,CoordCase1,CoordCase2,Niveau,Theme)


def RoundSuivant(cas,CoordCase1,CoordCase2,Niveau,Theme):
    BaW=[gray,black]
    attendre(1000)
    draw_fill_rectangle(CoordCase1,98,98,BaW[cas])
    draw_fill_rectangle(CoordCase2,98,98,BaW[cas])
    affiche_coup(0,Niveau,Theme)














# -*- coding: utf-8 -*-

from graphics_nsi import *
from constantes import *
from interface_graphic_reglage import*

def MainReglage () :
    InitInterface(6)
    return Choix()


def Choix () :
    P1 = Point(0,0)
    lvl=0
    o = 6           #Couleur des Textes
    pseudo=""
    MorpionDemineur=2

    while not (174 < P1.x < 345 and 410 < P1.y < 470) :
        P1 = wait_clic()
        ##Difficulte
        if 105<P1.y<155:
            lvl=ChoixDifficulteInterface(P1,o)
        ##Pseudo
        if (187 < P1.x < 337 and 200 < P1.y < 250) :
            pseudo = ChoixPseudo(pseudo,o)
        ##Couleur
        if 270<P1.y<290:
            o=-1
            for j in range(150,471,40):
                o+=1
                if j < P1.x < j+20:
                    draw_fill_rectangle(Point(262,120),500,240,black)
                    draw_fill_rectangle(Point(262,395),500,150,black)
                    ReglageInterface (o)
                    RetraceDifficulte(lvl,o)
                    RetracePseudo(pseudo,o)
                    RetraceChoixJeu(MorpionDemineur,o)
                    break
        ##Jeu
        if 320<P1.y<380:
            if 87<P1.x<237:
                InterfaceChoixJeu(o)
                draw_fill_rectangle(Point(162,355),150,60,CouleurReglage[o])
                aff_pol("Memory",15,Point(131,343),black)
                MorpionDemineur=0
            elif 287<P1.x<437:
                InterfaceChoixJeu(o)
                draw_fill_rectangle(Point(362,355),150,60,CouleurReglage[o])
                aff_pol("Demineur",15,Point(330,343),black)
                MorpionDemineur=1

    if pseudo=="":
        pseudo="Joueur54D6"
    return lvl+10*MorpionDemineur,pseudo,o


def ChoixDifficulteInterface(P1,o):
    ListeDifficulte=["FACILE","NORMAL","DIFFICILE","EXTREME"]
    lvl=0
    for i in range(25,500,125):
        if i < P1.x < i+100:
            InterfaceDifficulte(o)
            draw_fill_rectangle(Point(i+50,130),100,50,CouleurReglage[o])
            lt=largeur_texte(ListeDifficulte[lvl],15)
            ht=hauteur_texte(ListeDifficulte[lvl],15)
            aff_pol(ListeDifficulte[lvl],15,Point(i+50-(lt/2),130-(ht/2)),black)
            return lvl
        lvl+=1

def RetraceDifficulte(lvl,o):
    ListeDifficulte=["FACILE","NORMAL","DIFFICILE","EXTREME"]
    InterfaceDifficulte(o)
    draw_fill_rectangle(Point(25+(125*lvl)+50,130),100,50,CouleurReglage[o])
    lt=largeur_texte(ListeDifficulte[lvl],15)
    ht=hauteur_texte(ListeDifficulte[lvl],15)
    aff_pol(ListeDifficulte[lvl],15,Point(25+(125*lvl)+50-(lt/2),130-(ht/2)),black)

def RetracePseudo(pseudo,o):
    x=178
    if len(pseudo)==0:
        return
    draw_fill_rectangle(Point(262,215),100,16,black)
    for caracteres in pseudo:
        aff_pol(caracteres,22,Point(x,200),CouleurReglage[o])
        x+=largeur_texte(caracteres,22)

def RetraceChoixJeu(MorpionDemineur,o):
    InterfaceChoixJeu(o)
    if MorpionDemineur==0:
        draw_fill_rectangle(Point(162,355),150,60,CouleurReglage[o])
        aff_pol("Morpion",15,Point(131,343),black)
    elif MorpionDemineur==1:
        draw_fill_rectangle(Point(362,355),150,60,CouleurReglage[o])
        aff_pol("Demineur",15,Point(330,343),black)


def ChoixPseudo(pseudo, o):
    x=178
    if len(pseudo) == 0:
        draw_fill_rectangle(Point(262,215),100,16,black)                #Cacher le mot "Pseudo"
    else:
        for caracteres in pseudo:
            x+=largeur_texte(caracteres,22)
    Lettre= ""
    while Lettre != "\r" :
        aff_pol(Lettre,22,Point(x,200),CouleurReglage[o])               #Tant que la touche "Entrer" n'est pas appuyé
        x+=largeur_texte(Lettre,22)
        Lettre = wait_key()
        if Lettre == '\x08' and len(pseudo)>0:                          #Si la touche est "Effacer" et que le pseudo n'est pas vide
            draw_fill_rectangle(Point(262,215),190,50,black)
            InterfacePseudo(o)
            draw_fill_rectangle(Point(262,215),100,16,black)
            pseudo, x = pseudo[:-1], 178
            for caracteres in pseudo:
                aff_pol(caracteres,22,Point(x,200),CouleurReglage[o])
                x+=largeur_texte(caracteres,22)
            Lettre=""
        elif Lettre != '\x08' and len(pseudo)<10 and Lettre != '\r':     #Si la touche n'est pas "Effacer" et le pseudo est de moins de 10 lettres
            pseudo+= Lettre
        elif Lettre != "\r":
            Lettre=""
    return pseudo







# -*- coding: utf-8 -*-

from constantes import *
from Projet import *

def graphic_jeux () :
    init_graphic(500,400,"Jeux")
    lj=largeur_texte("Jeux",25,True)
    hj=hauteur_texte("Jeux",25,True)
    aff_pol("Jeux",25,Point(250-lj/2,65-hj/2),white,True)

    draw_rectangle(Point(150,175),150,75,white)
    ld=largeur_texte("Demineur",18)
    hd=hauteur_texte("Demineur",18)
    aff_pol("Demineur",18,Point(150-ld/2,175-hd/2),white)

    draw_rectangle(Point(350,175),150,75,white)
    lm=largeur_texte("Memory",18)
    hm=hauteur_texte("Memory",18)
    aff_pol("Memory",18,Point(350-lm/2,175-hm/2),white)

    draw_rectangle(Point(250,300),150,75,white)
    ljouer=largeur_texte("Jouer",22)
    hjouer=hauteur_texte("Jouer",22)
    aff_pol("Jouer",22,Point(250-ljouer/2,300-hjouer/2),white)

def reset_demineur () :
    draw_fill_rectangle(Point(150,175),150,75,black)
    draw_rectangle(Point(150,175),150,75,white)
    ld=largeur_texte("Demineur",18)
    hd=hauteur_texte("Demineur",18)
    aff_pol("Demineur",18,Point(150-ld/2,175-hd/2),white)

def reset_memory () :
    draw_fill_rectangle(Point(350,175),150,75,black)
    draw_rectangle(Point(350,175),150,75,white)
    lm=largeur_texte("Memory",18)
    hm=hauteur_texte("Memory",18)
    aff_pol("Memory",18,Point(350-lm/2,175-hm/2),white)

def choix_demineur () :
    draw_fill_rectangle(Point(150,175),150,75,black)
    draw_fill_rectangle(Point(150,175),150,75,white)
    ld=largeur_texte("Demineur",18)
    hd=hauteur_texte("Demineur",18)
    aff_pol("Demineur",18,Point(150-ld/2,175-hd/2),black)

def choix_memory () :
    draw_fill_rectangle(Point(350,175),150,75,black)
    draw_fill_rectangle(Point(350,175),150,75,white)
    lm=largeur_texte("Memory",18)
    hm=hauteur_texte("Memory",18)
    aff_pol("Memory",18,Point(350-lm/2,175-hm/2),black)
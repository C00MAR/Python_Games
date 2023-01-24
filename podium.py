# -*- coding: utf-8 -*-

from graphics_nsi import *
from Gestion_Scores import *
from Projet import *


def interface_podium(Joueur,ListeScore):
    init_graphic(500,500,"Podium")
    load_image_transp('BackgroundPodium.png',Point(-200,-280))
    graphic_podium(Joueur,ListeScore)
    wait_escape()


def graphic_podium (Joueur,ListeScore) :
    aff_pol("Podium",30,Point(248-55,28),gray, text_bold = True )
    aff_pol("Podium",30,Point(250-55,30),white, text_bold = True )
    load_image_transp('podium.png',Point(50,90))
    aff_pol(ListeScore[0][0]+':'+str(ListeScore[0][1]),22,Point(248-largeur_texte(ListeScore[0][0]+str(ListeScore[0][1]),22,text_bold=True)/2,163),pygame.Color(113,103,53), text_bold = True )
    aff_pol(ListeScore[0][0]+':'+str(ListeScore[0][1]),22,Point(250-largeur_texte(ListeScore[0][0]+str(ListeScore[0][1]),22,text_bold=True)/2,165),gold, text_bold = True )
    aff_pol(ListeScore[1][0]+':'+str(ListeScore[1][1]),22,Point(68,218),pygame.Color(108,108,108), text_bold = True )
    aff_pol(ListeScore[1][0]+':'+str(ListeScore[1][1]),22,Point(70,220),silver, text_bold = True )
    aff_pol(ListeScore[2][0]+':'+str(ListeScore[2][1]),22,Point(318,213),pygame.Color(90,72,27),text_bold = True )
    aff_pol(ListeScore[2][0]+':'+str(ListeScore[2][1]),22,Point(320,215),pygame.Color(176,145,64),text_bold = True )
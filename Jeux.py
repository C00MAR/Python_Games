# -*- coding: utf-8 -*-

from constantes import *
from Projet import *
from interface_graphic_jeux import *
from Demineur import *
from Reglage import *

def jeux() :
    graphic_jeux()
    choix_jeux()


def choix_jeux() :
    P1 = Point(0,0)
    jeux = 0
    while not (175<P1.x<325 and 262<P1.y < 338) :
        P1 = wait_clic()
        # Demineur
        if (75 < P1.x < 225 and 137 < P1.y < 213) :
            jeux = 0
            reset_memory (); choix_demineur ()
        if (275 < P1.x < 425 and 137 < P1.y < 213) :
            jeux = 1
            reset_demineur (); choix_memory ()
    Jouer(jeux)
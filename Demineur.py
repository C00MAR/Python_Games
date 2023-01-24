from graphics_nsi import *
from random import *
from Projet import *

def main_demineur(SizeFenetre, SizeRond, NbCase, NbCoups, Theme):
    '''Fonction principale du Demineur. Prend en entrÃ©e la taille de la fenetre,
        la taille des ronds, le nombre de case et le nombre de coups maximum.'''
    init_graphic(SizeFenetre,SizeFenetre,"Demineur")    #Initialisation fenetre graphique
    SizeCase=int(SizeFenetre//NbCase)                   #Calcul taille cases
    interface(SizeFenetre,NbCase,SizeCase,Theme)        #Creation de l'interface
    ordi=choix_ordi(SizeFenetre,SizeCase)               #Choix de l'ordinateur

    for coups in range(NbCoups):
        choix=coordPoint(SizeFenetre,NbCase,SizeCase)
        distance=calculD(choix,ordi,SizeCase)
        verification=verif(choix,ordi,coups,NbCoups)    #Verification gagne ou non
        if verification != 0:
            fin(ordi,verification,SizeCase)             #Dessin de croix
            if verification==2:
                rond(distance,choix,SizeRond)           #Trace le rond (Fin du jeu)
            wait_escape()
        rond(distance,choix,SizeRond)                   #Trace le rond
    wait_escape()


def interface(SizeFenetre,NbCase,SizeCase,Theme):
    '''Fonction prenant en  entrÃ©e la taille de la fenÃªtre, le nombre de cases et la taille des cases.
        La fonction trace un cardriage.Â Doit Ãªtre appellÃ© aprÃ¨s avoir ouvert la fenÃªtre graphique.'''
    P1=Point(SizeCase,0)
    P2=Point(SizeCase,SizeFenetre)
    for j in range(NbCase):
        draw_line(P1,P2,CouleurReglage[Theme])
        P1.x+=SizeCase
        P2.x+=SizeCase
    P1.x, P1.y = P1.y, P1.x
    P2.x, P2.y = P2.y, P2.x
    for j in range(NbCase):
        P1.y-=SizeCase
        P2.y-=SizeCase
        draw_line(P1,P2,CouleurReglage[Theme])


def coordPoint(SizeFenetre,NbCase,SizeCase):
    '''Fonction prenant en  entrÃ©e la taille de la fenÃªtre, le nombre de cases et la taille des cases.
        La fonction attend un clic puis renvoit les coordonnÃ©es du centre de la case ou a eu lieu le clic.'''
    P1=wait_clic()
    for h in range(NbCase):
        for i in range(0,SizeFenetre,SizeCase):
            if i < P1.x < i+SizeCase and SizeCase*h < P1.y < SizeCase*(h+1):
                return Point(i+SizeCase//2,SizeCase*h+SizeCase//2)


def rond(distance,choix,SizeRond):
    '''Fonction prenant en entrÃ©e la distance entre le choix de l'ordi et
        le choix du joueur, les coordonnÃ©es du choix du joueur et  la taille du rond.
        La fonction renvoit sur la fenetre graphique un rond de centre "choix" et de taille"SizeRond".
        La couleur estb dÃ©finit selon la "distance"'''
    couleur=[white,red,orange,yellow,blue]
    if distance>4:
        distance=4
    draw_fill_circle(choix,SizeRond,couleur[distance])


def choix_ordi(SizeFenetre,SizeCase):
    '''Fonction prenant en entrÃ©e la taille de la fenÃªtre et le nombre de cases.
        Renvoit les coordonnÃ©es du centre d'une des cases du jeu choisit au hasard'''
    x=randrange(SizeCase//2,SizeFenetre,SizeCase)
    y=randrange(SizeCase//2,SizeFenetre,SizeCase)
    return Point(x,y)


def verif(choix,ordi,coups,NbCoups):
    '''Fonction prenant en entrÃ©e  le choix de l'ordinateur, le choix du joueur,
        le coups auquel est la partie et le nombre de coups macximum jouable.
        Renvoit 0 si la partie n'est pas finit, 1 si le joueur a gagnÃ©
        et 2 si le joueur Ã  utilisÃ© tout ces coups sans trouver la case de l'ordinateur (perdu)'''
    if choix.x == ordi.x and choix.y == ordi.y:
        return 1
    elif coups+1 == NbCoups:
        return 2
    else:
        return 0

def fin(choix,cas,SizeCase):
    '''Fonction prenant en entrÃ©e  le choix de l'ordinateur,
        le nombre renvoyÃ© par la fonction verif() et la taille des cases.
        Renvoit sur l'interface graphique une croix (sur la case de l'ordinateur)
        rouge si le joueur a trovÃ© la case de l'ordinateur et une croix blanche sinon'''
    if cas==1:
        couleur=red
    else:
        couleur=white
    P1=Point(choix.x-SizeCase//2,choix.y-SizeCase/2)
    P2=Point(choix.x+SizeCase//2,choix.y+SizeCase/2)
    draw_line(P1,P2,couleur)
    P2.y-=SizeCase
    P1.y+=SizeCase
    draw_line(P1,P2,couleur)

def calculD(choix,ordi,SizeCase):
    '''Fonction prenant en entrÃ©e  le choix du joueur, le choix de l'ordinateur et la taille des cases.
        Renvoit la distance netre le choix du jouer et de l'ordinateur. Si x > y elle renvoit la distance x et sinon y'''
    if ordi.x>choix.x:
        x=ordi.x-choix.x
    else:
        x=choix.x-ordi.x
    if ordi.y>choix.y:
        y=ordi.y-choix.y
    else:
        y=choix.y-ordi.y
    if x > y:
        return int(x//SizeCase)
    else:
        return int(y//SizeCase)
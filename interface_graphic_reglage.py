from constantes import *
## y += 30 entre chaque catégorie


def InitInterface(o):
    init_graphic(525,500,"Réglages")
    ReglageInterface(o)

def ReglageInterface (o) :
    Réglage(o)
    InterfaceDifficulte(o)
    InterfacePseudo(o)
    InterfaceCouleur(o)
    InterfaceChoixJeu(o)
    InterfaceJouer(o)

def Réglage (o) :
    lt=largeur_texte("Réglages",22,True,False)
    ht=hauteur_texte("Réglages",22,True,False)
    aff_pol("Réglages",22,Point((525/2)-(lt/2)-2,50-(ht/2)-2),CouleurReglage[o],True,False)
    aff_pol("Réglages",22,Point((525/2)-(lt/2),50-(ht/2)),white,True,False)

def InterfaceDifficulte (o) :
    ## y = 100 -> 160
    P1 = Point(75,130)
    Difficulte=["FACILE","NORMAL","DIFFICILE","EXTRÊME"]
    draw_fill_rectangle(Point(262,130),525,54,black)       #Effacer anciennes cases
    for i in range (4) :
        draw_rectangle(P1,100,50,CouleurReglage[o])
        lt=largeur_texte(Difficulte[i],15)
        ht=hauteur_texte(Difficulte[i],15)
        P1.x-=(lt/2)
        P1.y-=(ht/2)
        aff_pol(Difficulte[i],15,P1,CouleurReglage[o])
        P1.x+=(lt/2)
        P1.y+=(ht/2)
        P1.x+=125

def InterfacePseudo (o) :
    ## y = 190 -> 240
    draw_rectangle(Point(262,215),190,50,CouleurReglage[o])
    lt=largeur_texte("Pseudo",15)
    ht=hauteur_texte("Pseudo",15)
    aff_pol("Pseudo",15,Point(262-(lt/2),215-(ht/2)),CouleurReglage[o])

def InterfaceCouleur (o) :
    ## y = 270 -> 290
    aff_pol("Choix couleur :",15,Point(20,270),white,True)
    Cercle = Point(160,280)
    CouleurReglage=[blue,cyan,rubi,green,orange,pink,red,silver,yellow]
    for j in range (9) :
        draw_circle (Cercle,10,white)
        draw_fill_circle (Cercle,8,CouleurReglage[j])
        Cercle.x += 40

def InterfaceChoixJeu (o) :
    ## y = 320 -> 380
    draw_fill_rectangle(Point(262,355),525,65,black)
    draw_rectangle(Point(162,355),150,60,CouleurReglage[o])
    draw_rectangle(Point(362,355),150,60,CouleurReglage[o])
    aff_pol("Memory",15,Point(131,343),CouleurReglage[o])
    aff_pol("Demineur",15,Point(330,343),CouleurReglage[o])

def InterfaceJouer (o) :
    ## y = 410 -> 470
    draw_rectangle(Point(262,440),175,60,CouleurReglage[o])
    lt=largeur_texte("Jouer",18,True)
    ht=hauteur_texte("Jouer",18,True)
    aff_pol("Jouer",18,Point(262-(lt/2),440-(ht/2)),CouleurReglage[o])



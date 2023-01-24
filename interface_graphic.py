# -*- coding: utf-8 -*-

from graphics_nsi import *
from constantes import *


def graphic (Niveau,Theme) :
    P1=Point(1.5*SizeCase,SizeCase)
    P2=Point(1.5*SizeCase,Niveau[0]-SizeCase)
    #draw_fill_rectangle(Point(250,250),400,300,gray)
    draw_fill_rectangle(Point(Niveau[0]//2,Niveau[0]//2),Niveau[0]-SizeCase,Niveau[0]-SizeCase*2,gray)
    #Trace les lignes verticales
    for i in range (Niveau[1]-1) :
        draw_line(P1,P2,CouleurReglage[Theme])
        P1.x+=SizeCase
        P2.x+=SizeCase
    P1=Point(SizeCase//2,SizeCase*2)
    P2=Point(Niveau[0]-SizeCase//2,SizeCase*2)
    #Trace les lignes horizontales
    for i in range (Niveau[2]-1) :
        draw_line(P1,P2,CouleurReglage[Theme])
        P1.y+=SizeCase
        P2.y+=SizeCase
    aff_pol("Jeu de Memory",22,Point(Niveau[0]//2-90+2,SizeCase//4+13+2),CouleurReglage[Theme], text_bold = True )
    aff_pol("Jeu de Memory",22,Point(Niveau[0]//2-90,SizeCase//4+13),white, text_bold = True )


def affiche_score(score,Niveau,Theme):
    draw_fill_rectangle(Point(Niveau[0]-SizeCase//2,Niveau[0]-SizeCase//3),SizeCase+SizeCase//5,SizeCase//2,black)
    aff_pol("Score: "+str(score),17,Point(Niveau[0]//2+Niveau[0]//4,Niveau[0]-SizeCase//2),CouleurReglage[Theme])

def affiche_coup(nb,Niveau,Theme):
    draw_fill_rectangle(Point(SizeCase//2+SizeCase//3,Niveau[0]-SizeCase//2),SizeCase+SizeCase//4,SizeCase//2,black)
    for j in range(2):
        draw_rectangle(Point(SizeCase//2+(SizeCase//2)*j,Niveau[0]-SizeCase//2),(SizeCase//2)+1,(SizeCase//3)+2,gray)
    for i in range(nb):
        draw_fill_rectangle(Point(SizeCase//2*(i+1),Niveau[0]-SizeCase//2),SizeCase//2-2,SizeCase//3,CouleurReglage[Theme])


def afficheChrono(chrono):
    draw_fill_rectangle(Point(SizeCase-SizeCase//3,SizeCase//2),150,50,black)
    aff_pol(chrono,22,Point(SizeCase//3,SizeCase//3),red)
    attendre(5)


def animation_case(couleur,coordcase):
    PointHG,PointHD,PointBG,PointBD = calcul_angle(coordcase)
    for i in range(SizeCase//2):
        draw_line(PointHG,PointBG,black)
        draw_line(PointHD,PointBD,black)
        PointHG.x+=1;PointBG.x+=1
        PointHD.x-=1;PointBD.x-=1
        attendre(1)
    for i in range(SizeCase//2+1):
        draw_line(PointHG,PointBG,couleur)
        draw_line(PointHD,PointBD,couleur)
        PointHG.x-=1;PointBG.x-=1
        PointHD.x+=1;PointBD.x+=1
        attendre(1)



def calcul_angle(coordcase):
    SIZECASE=96                 #98 normalement
    PointHG=Point(0,0); PointHD=Point(0,0); PointBG=Point(0,0); PointBD=Point(0,0)
    SIZECASE=SIZECASE//2
    PointHG.x= coordcase.x - SIZECASE
    PointHG.y= coordcase.y - SIZECASE

    PointHD.x= coordcase.x + SIZECASE
    PointHD.y= coordcase.y - SIZECASE

    PointBG.x= coordcase.x - SIZECASE
    PointBG.y= coordcase.y + SIZECASE

    PointBD.x= coordcase.x + SIZECASE
    PointBD.y= coordcase.y + SIZECASE

    return PointHG,PointHD,PointBG,PointBD
# -*- coding: utf-8 -*-

from Projet import *
from podium import *

def GestionScore(Joueur):
    Fichier = open("Scores.txt","r",encoding="utf-8")
    Liste= separation(Fichier)
    Liste.append(Joueur)
    Liste=trier(Liste)
    del Liste[-1]
    Fichier.close()
    Fichier = open("Scores.txt","w",encoding="utf-8")
    for j in range(len(Liste)-1):
        Fichier.write(str(Liste[j][0])+";"+str(Liste[j][1])+"\n")
    Fichier.write(str(Liste[-1][0])+";"+str(Liste[-1][1]))
    Fichier.close()
    interface_podium(Joueur,Liste)


def separation(Fichier):
    Ligne=Fichier.read().split("\n")
    for i in range(len(Ligne)):
        Ligne[i]=Ligne[i].split(";")
        Ligne[i][1]=int(Ligne[i][1])
    return Ligne


def trier(Liste):
   for i in range(len(Liste)):
       min = i
       for j in range(i+1, len(Liste)):
           if Liste[min][1] < Liste[j][1]:
               min = j
       tmp = Liste[i]
       Liste[i] = Liste[min]
       Liste[min] = tmp
   return Liste


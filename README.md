# Python_Games

## _Lancer Python Games :_

- Télécharger le zip du Github
- Le dézipper et lancer le fichier Projet.py
- Ouvrir la console et lancer  ```main()```
- Une fenêtre s'ouvre
- Voici les Jeux

###### _Erreur Pygame :_

Si vous obtenez cette erreur :
<img src="https://lh3.googleusercontent.com/u/0/drive-viewer/AFDK6gN17skPSQ5gWHF9cWVzaDJBRZRhkQABxtUsN2TYOtXMBoAb7cPIb7iOiVpu4P2JL6b6QRsUoaMn8clxIqfgobAIpzlS_Q=w1920-h902" alt="No module named 'pygame'" width="75%"/>

```
Traceback (most recent call last):
  File "C:\Users\moure\Downloads\Jeux Python\Projet.py", line 4, in <module>
    from Gestion_Scores import *
  File "C:\Users\moure\Downloads\Jeux Python\Gestion_Scores.py", line 3, in <module>
    from Projet import *
  File "C:\Users\moure\Downloads\Jeux Python\Projet.py", line 5, in <module>
    from constantes import *
  File "C:\Users\moure\Downloads\Jeux Python\constantes.py", line 3, in <module>
    from graphics_nsi import *
  File "C:\Users\moure\Downloads\Jeux Python\graphics_nsi.py", line 26, in <module>
    import pygame
ModuleNotFoundError: No module named 'pygame'
```

Il vous faudra faire ceci :

- Ouvrir un terminal de Commande dans le dossier du projet
- Exécuter cette commande :
```python3 -m pip install -U pygame --user```
- Vous pouvez ensuite exéctuer cette commande :
```python3 -m pip install --upgrade pip```
- Normalement tout fonctionne !

## _Pourquoi Python Games :_

Python Games est un projet étudiant en collaboration avec [@RenaudBrevin](https://github.com/RenaudBrevin). Nous devions créer des Jeux en Python en utilisant la bibliothèque pygames et l'autre conçue par nos professeurs ```graphics _nsi.py```. Nous avions la contrainte de faire un démineur, pour l'autre jeu le memory a été un choix.
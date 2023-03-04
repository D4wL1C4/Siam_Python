# Remake of SIAM in python
Jeu de plateau sur le même principe de *Abalone* 

## Le Siam : 
Le siam est un jeu de société qui se joue à deux, sur un plateau (5x5). Il y a 3 montagnes (qui ont un poids de 1) et 5 animaux (éléphant ou rhinocéros) par joueur (force de 1).
Le Siam peut être comparé au jeu de société Abalone.

## Déroulement du jeu :
Au début du jeu les animaux sont disposés à l'extérieur du plateau et les blocs de rochers au centre du plateau. Les éléphants blancs commencent à jouer comme aux échecs avec les pions blancs. 
Les joueurs ne pourront jouer à chaque tour de jeu qu'un seul de leurs animaaux et ne faire qu'une de ces 5 actions : 
- Entrer un de ses animaux sur le plateau 
- Se déplacer sur une case libre
- Changer l'orientation de son animal sans changer de case 
- Sortir un de ses animaux disposés sur une case extérieure
- Se déplacer en poussant d'autres pièces disposées sur le plateau

#### But : être le premier à sortir une région montagneuse (bloc de rochers) à l'extérieur du plateau. 

## Les étapes nécessaires à son développement : 
- utilisation de la bibliothèque Pygame
- afficher un plateau de jeu 
- afficher les pions (éléphants, rhinocéros et montagnes)
- pouvoir interagir avec le plateau et les pions
- pouvoir bouger les pions(mouvements de base)
- faire un système de condition pour les mouvements(placer les pièces à des endroits spécifiques, pousser ou bloquer personnage(calculs de force) …)
- condition de victoire/défaite
- data et enregistrement de profil de joueur (nb de victoires/défaites)

## Fonctionnalitées bonus (après avoir fini toutes les étapes ci-dessus) :
- afficher les mouvements disponibles
- faire les animations
- héberger les fichiers sur un site web pour pouvoir jouer en ligne sans telecharger le jeu
- elaboration d’un menu de jeu 
- ajout de niveaux, avec difficultés différentes et donc de nouvelles conditions

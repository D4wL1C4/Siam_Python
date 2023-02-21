import pygame


#definition de la taille de l'ecran
width = 800
height = 800

#le nombre de lignes et de colonnes
row = 5
col = 5 

#le nombre de case = la largeur divisé par la hauteur (// : division euclidienne)
square = width // height

#definition des couleurs des cases du plateau
l_brown = (225, 128, 23)
green = (124, 176, 62)

#Charger les pieces
#Rhinocéros
rhino = pygame.image.load("siam_game/sources/rhino.png")
#rhino = pygame.transform.scale(rhino, (square, square))

#elephant
eleph = pygame.image.load("siam_game/sources/eleph.png")
eleph = pygame.transform.scale(eleph, (square, square))
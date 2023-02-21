import pygame


#definition de la taille de l'ecran
screen_width = 800
screen_height = 800

#le nombre de lignes et de colonnes
row = 5
col = 5 

#nombre cases 
case_number = row * col

#taille case = côté divisé par le nombre de colonne ou ligne(= car carré) (// : division euclidienne)
square = screen_width // row

#definition des couleurs des cases du plateau
l_brown = (225, 128, 23)
green = (124, 176, 62)

#Charger les pieces
#Rhinocéros
rhino = pygame.image.load("siam_game/sources/rhino.png")
rhino = pygame.transform.scale(rhino, (square, square))

#elephant
eleph = pygame.image.load("siam_game/sources/eleph.png")
eleph = pygame.transform.scale(eleph, (square, square))

#montagne
mont = pygame.image.load("siam_game/sources/montagne.png")
mont = pygame.transform.scale(mont, (square, square))

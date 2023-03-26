import pygame
import os

screen = pygame.display.set_mode((1000, 1000))

#definition de la taille de l'ecran
screen_width = 1000
screen_height = 1000

#le nombre de lignes et de colonnes
row = 5
col = 5 

#nombre cases 
case_number = row * col

square = 100

#definition des couleurs des cases du plateau
color1 = (195,142,95)
color2 = (117,162,203)

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

bgImage = pygame.image.load("siam_game/sources/bg_siam.png")
bgImage = pygame.transform.scale(bgImage, (1500,1000))

play = pygame.image.load("siam_game/sources/TitlePlay.png")
play = pygame.transform.scale_by(play, .5)

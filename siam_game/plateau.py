import pygame
from siam_game.ressources import *

#version virtuelle du plateau afficher sur la fenêtre
plateau = [
        [0,1,1,1,1,1,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,2,3,4,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,1,1,1,1,1,0]
    ]

#permet de dessiner un plateau de jeu en fonction de 2 couleurs différentes, une position x et y et une taille de case
def drawPlate(surface, color, colorbis, posX, posY, width, height):
    for i in range(row):
        if i != 0:
            posX += square
        if i%2 and i!=0:
            color, colorbis = colorbis, color
        else:
            colorbis, color = color, colorbis
        for k in range(col):
            if k == 0:
                pygame.draw.rect(surface, color, (posX, posY, width, height))
            if k%2: 
                pygame.draw.rect(surface, color, (posX, posY + square*k, width, height))
            else:
                pygame.draw.rect(surface, colorbis, (posX, posY  + square*k, width, height))

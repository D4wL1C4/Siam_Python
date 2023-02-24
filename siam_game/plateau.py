import pygame
from siam_game.ressources import *


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
              


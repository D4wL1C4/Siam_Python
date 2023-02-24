import csv
import pygame
import random

from siam_game.ressources import *
from siam_game.pieces import *
from siam_game.plateau import drawPlate

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width, screen_height))

rhino_rect = rhino.get_rect()


og_pos = 250

def MainGame():
    run = True
    fps = 60
    while run:
        clock.tick(fps)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN: #calcule la position du curseur
                if pygame.mouse.get_pos()[0] > 250 and pygame.mouse.get_pos()[0] < 750 and pygame.mouse.get_pos()[1] > 150 and pygame.mouse.get_pos()[1] < 850:
                    mousePos = pygame.mouse.get_pos()
                    print(int((mousePos[0] - 250)/100), int((mousePos[1] - 150)/100)) # transforme le resultat en index de colonnes / lignes (ex : 0;1 - 3;4 etc...)
                if rhino_rect.collidepoint():
                    print("something")


        drawPlate(screen, l_brown, green, 250, 250, square, square) #Plateau
        screen.blit(rhino, (250, 650))
        



MainGame()


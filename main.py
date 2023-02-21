import csv
import pygame
import random

from siam_game.ressources import *

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((width, height))

print(square)


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

        screen.blit(rhino, (50,50))

MainGame()

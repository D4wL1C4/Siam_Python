import csv
import pygame
import random

from siam_game.ressources import *

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width, screen_height))

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

        screen.blit(rhino, (150,50))
        screen.blit(rhino, (300,50))
        screen.blit(rhino, (450,50))
        screen.blit(eleph,(150,650))
        screen.blit(eleph,(300,650))
        screen.blit(eleph,(450,650))

MainGame()

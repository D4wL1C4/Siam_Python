import pygame
from siam_game.plateau import *
from siam_game.ressources import *


class Rhino:
    def __init__(self, posX, posY, image, force):
        self.posX = posX
        self.posY = posY
        self.image = pygame.transform.scale(image, (square, square))
        self.rect = self.image.get_rect()
        self.force = force
    
    def select(self):
        mousePos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mousePos):
            print("Hover")


        


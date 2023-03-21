import csv
import pygame
import random

from siam_game.ressources import *
from siam_game.pieces import *
from siam_game.plateau import drawPlate

pygame.init()

clock = pygame.time.Clock()
rhino_rect = pygame.Surface.get_rect(rhino)

og_pos = 250

def initGame():
    #dessiner le plateau et placer tous les pions au bon endroit
    drawPlate(screen, color1, color2, 250, 250, square, square) #Plateau
    

def MainGame():
    initGame()
    run = True
    fps = 60
    while run:
        
        clock.tick(fps)
        pygame.display.update()
        mousePos = pygame.mouse.get_pos()
        caseIndexX = int((mousePos[0] - 250)/100)
        caseIndexY = int((mousePos[1] - 150)/100)
        
        

        rhino_1.move(mousePos[0], mousePos[1])
        rhino_2.move(mousePos[0], mousePos[1])
        rhino_3.move(mousePos[0], mousePos[1])
        rhino_4.move(mousePos[0], mousePos[1])
        rhino_5.move(mousePos[0], mousePos[1])

        eleph_1.move(mousePos[0], mousePos[1])
        eleph_2.move(mousePos[0], mousePos[1])
        eleph_3.move(mousePos[0], mousePos[1])
        eleph_4.move(mousePos[0], mousePos[1])
        eleph_5.move(mousePos[0], mousePos[1])
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN: #calcule la position du curseur
                
                #rhino_1.posY = mousePos[1]
                #rhino_1.posX = mousePos[0]
                
                if pygame.mouse.get_pos()[0] > 250 and pygame.mouse.get_pos()[0] < 750 and pygame.mouse.get_pos()[1] > 150 and pygame.mouse.get_pos()[1] < 850:
                    print(caseIndexX, caseIndexY) # transforme le resultat en index de colonnes / lignes (ex : 0;1 - 3;4 etc...)
                    rhino_1.select()
                    rhino_2.select()
                    rhino_3.select()
                    rhino_4.select()
                    rhino_5.select()

                    eleph_1.select()
                    eleph_2.select()
                    eleph_3.select()
                    eleph_4.select()
                    eleph_5.select()
            
        
        
        screen.fill((0,0,0))   
        screen.blit(bgImage, (0,0))              
        drawPlate(screen, color1, color2, 250, 250, square, square)            
        for piece in pieces:
            piece.Update()
        pygame.display.flip()
        

        
MainGame()

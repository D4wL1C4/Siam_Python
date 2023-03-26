import csv
import pygame
import random

from siam_game.ressources import *
from siam_game.pieces import *
from siam_game.plateau import drawPlate

pygame.init()

clock = pygame.time.Clock()
rhino_rect = pygame.Surface.get_rect(rhino)

def initGame():
    #dessiner le plateau et placer tous les pions au bon endroit
    drawPlate(screen, color1, color2, 250, 250, square, square) #Plateau
    

def MainMenu():
    pygame.display.set_caption("Menu principal")
    run = True
    fps = 60

    play_rect = play.get_rect()
    play_rect.topleft = 300,300

    while run:
        mousePos = pygame.mouse.get_pos()
        clock.tick(fps)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_rect.collidepoint(mousePos):
                    MainGame()
        screen.blit(bgImage, (0,0))
        screen.blit(play,(300,300))
        pygame.display.flip()

def MainGame():
    pygame.display.set_caption("Fenêtre de jeu")
    initGame()
    run = True
    fps = 60
    piecesSelected = 0
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
                if pygame.mouse.get_pos()[0] > 250 and pygame.mouse.get_pos()[0] < 750 and pygame.mouse.get_pos()[1] > 150 and pygame.mouse.get_pos()[1] < 850:
                    print(caseIndexX, caseIndexY) # transforme le resultat en index de colonnes / lignes (ex : 0;1 - 3;4 etc...)
                    for piece in pions:
                        if piece.selected == True:
                            piecesSelected +=1
                    if piecesSelected == 0:
                        for piece in pions:
                            piece.select()
                    if plateau[caseIndexY][caseIndexX] == 0:
                        print("peut poser ici")
                        print(plateau[caseIndexY][caseIndexX])
                        for piece in pions:
                            piece.poser()
                            piecesSelected = 0
            
        
        screen.fill((0,0,0))   
        screen.blit(bgImage, (0,0))              
        drawPlate(screen, color1, color2, 250, 250, square, square)       
        for i in range(6):
            for k in range(4):
                plateau[i][k] = 0     
        for piece in pieces:
            piece.Update()
        pygame.display.flip()
        

        
MainMenu()

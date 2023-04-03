import pygame
from siam_game.plateau import *
from siam_game.ressources import *

class Piece:
    #anciene position
    previousPos = (0,0)
    
    #nouvelle position
    newPos = (0,0)

    #initialise les différentes variables des objets appartenant à la classe
    def __init__(self, _screen, posX : int, posY : int, image, name : str,):
        self.posX = posX
        self.posY = posY
        self.image = pygame.transform.scale(image, (square, square))
        self.rect = self.image.get_rect()
        self.rect.center = posX + square/2, posY+square/2
        self.selected = False
        self.canPlace = True 
        self.name = str(name)

    #affiche les pieces à chaque frames
    def Update(self):
        screen.blit(self.image, (self.posX, self.posY))
        
    #regarde si on click sur un des Rhino, si oui on le selectionne    
    def select(self):
        mousePos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mousePos) and self.selected == False:
            self.previousPos = (int((mousePos[0] - 150)//100), int((mousePos[1] - 150)//100))
            print(f"click sur {self.name}")
            self.selected = True

    #une fois la pièce en main, lors du prochain click elle sera posée sous certaines conditions (case déjà occupée, montagne, etc...)
    def poser(self):
        mousePos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mousePos) and self.selected == True:
            self.newPos = (int((mousePos[0] - 150)//100), int((mousePos[1] - 150)//100))
            if ((abs(self.newPos[0] - self.previousPos[0]) == 1 and abs(self.newPos[1] - self.previousPos[1]) == 0) or (abs(self.newPos[0] - self.previousPos[0]) == 0 and abs(self.newPos[1] - self.previousPos[1]) == 1)) and plateau[self.newPos[1]][self.newPos[0]] == 0:
                self.placeAndSnap()
                print(f"reclick sur {self.name}")
            #si il y a une montagnes là où on click déplacer la montagne
            elif ((abs(self.newPos[0] - self.previousPos[0]) == 1 and abs(self.newPos[1] - self.previousPos[1]) == 0) or (abs(self.newPos[0] - self.previousPos[0]) == 0 and abs(self.newPos[1] - self.previousPos[1]) == 1)) and (plateau[self.newPos[1]][self.newPos[0]] == 2 or plateau[self.newPos[1]][self.newPos[0]] == 3 or plateau[self.newPos[1]][self.newPos[0]] == 4):
                if plateau[self.newPos[1]][self.newPos[0]] == 2:
                    mountain = mountain_1
                elif plateau[self.newPos[1]][self.newPos[0]] == 3:
                    mountain = mountain_2
                elif plateau[self.newPos[1]][self.newPos[0]] == 4:
                    mountain = mountain_3
                if self.newPos[0] - self.previousPos[0] == 1: #deplacement à droite
                    if plateau[self.newPos[1]][self.newPos[0] + 1] == 0: #verifie si il y a une piece à droite de la montagne
                        mountain.posX += 100
                        mountain.rect.center = mountain.posX, mountain.posY
                        self.placeAndSnap()
                    else:
                        self.goBack()
                if self.newPos[0] - self.previousPos[0] == -1: #deplacement à gauche
                    if plateau[self.newPos[1]][self.newPos[0] - 1] == 0: #verifie si il y a une piece à gauche de la montagne
                        mountain.posX -= 100
                        mountain.rect.center = mountain.posX, mountain.posY
                        self.placeAndSnap()
                    else:
                        self.goBack()
                if self.newPos[1] - self.previousPos[1] == 1: #deplacement en bas
                    if plateau[self.newPos[1] + 1][self.newPos[0]] == 0: #verifie si il y a une piece en bas de la montagne
                        mountain.posY += 100
                        mountain.rect.center = mountain.posX, mountain.posY
                        self.placeAndSnap()
                    else:
                        self.goBack()
                if self.newPos[1] - self.previousPos[1] == -1: #deplacement en haut
                    if plateau[self.newPos[1] - 1][self.newPos[0]] == 0: #verifie si il y a une piece en haut de la montagne
                        mountain.posY -= 100
                        mountain.rect.center = mountain.posX, mountain.posY
                        self.placeAndSnap()
                    else:
                        self.goBack()

            else:
                self.goBack()
                
    #replace la pièce sur l'ancienne position
    def goBack(self):
        self.selected = False
        self.posX = (self.previousPos[0]*100)+150
        self.posY = (self.previousPos[1]*100)+150
        self.rect.center = self.posX + square/2, self.posY + square/2
        self.newPos = (self.previousPos)
        print("Else")
    
    #centre la piece sur la case "snap"
    def placeAndSnap(self):
        mousePos = pygame.mouse.get_pos()

        self.selected = False
        self.rect.center = 150, 150
        self.rect.center = 150 + int((mousePos[0] - 150)/100)* square + square/2, 150 + int((mousePos[1] - 150)/100)* square + square/2
        self.posX, self.posY = self.rect.centerx - square/2, self.rect.centery - square/2
        plateau[self.newPos[1]][self.newPos[0]] = 1
        plateau[self.previousPos[1]][self.previousPos[0]] = 0


    #attache la piece à la souris si elle est séléctionnée
    def move(self, x, y):
        if self.selected == True:
            self.posX = x - square/2
            self.posY = y - square / 2
            self.rect.center = x, y

    #tourne la piece sur elle même en fonction d'un parametre "degres"
    def rotate(self, degres):
        mousePos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mousePos):
            self.image = pygame.transform.rotate(self.image, degres)
            self.rotation += degres 
        
            
class Montagne:

    #initialise les différentes variables des objets appartenant à la classe
    def __init__(self, _screen, posX : int, posY : int, image, name : str, type : int):
        self.posX = posX
        self.posY = posY
        self.image = pygame.transform.scale(image, (square, square))
        self.rect = self.image.get_rect()
        self.rect.center = posX + square/2, posY + square/2
        self.type = type
    
    #affiche les pieces à chaque frames
    def Update(self):
        screen.blit(self.image, (self.posX, self.posY))
        plateau[int((self.posY - 150)//100)][int((self.posX - 150)//100)] = self.type



#créations des objets/pions
rhino_1 = Piece(screen, 250, 750, rhino, "rhino_1")
rhino_2 = Piece(screen, 350, 750, rhino, "rhino_2")
rhino_3 = Piece(screen, 450, 750, rhino, "rhino_3")
rhino_4 = Piece(screen, 550, 750, rhino, "rhino_4")
rhino_5 = Piece(screen, 650, 750, rhino, "rhino_5")

eleph_1 = Piece(screen, 250, 150, eleph, "eleph_1")
eleph_2 = Piece(screen, 350, 150, eleph, "eleph_2")
eleph_3 = Piece(screen, 450, 150, eleph, "eleph_3")
eleph_4 = Piece(screen, 550, 150, eleph, "eleph_4")
eleph_5 = Piece(screen, 650, 150, eleph, "eleph_5")

mountain_1 = Montagne(screen, 350, 450, mont, "mountain_1", 2)
mountain_2 = Montagne(screen, 450, 450, mont, "mountain_2", 3)
mountain_3 = Montagne(screen, 550, 450, mont, "mountain_3", 4)
        
pieces = [rhino_1, rhino_2, rhino_3, rhino_4, rhino_5, eleph_1, eleph_2, eleph_3, eleph_4, eleph_5, mountain_1, mountain_2, mountain_3]  
pions = [rhino_1, rhino_2, rhino_3, rhino_4, rhino_5, eleph_1, eleph_2, eleph_3, eleph_4, eleph_5]

mountains = [mountain_1, mountain_2, mountain_3]

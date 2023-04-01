import pygame
from siam_game.plateau import *
from siam_game.ressources import *

class Rhino:
    previousPos = (0,0)
    newPos = (0,0)

    def __init__(self, _screen, posX : int, posY : int, image, name : str, rotation):
        self.posX = posX
        self.posY = posY
        self.image = pygame.transform.scale(image, (square, square))
        self.rect = self.image.get_rect()
        self.rect.center = posX + square/2, posY+square/2
        self.selected = False
        self.canPlace = True 
        self.name = str(name)
        self.rotation = rotation
        self.forceRhino = 1

    def Update(self):
        mousePos = pygame.mouse.get_pos()
        screen.blit(self.image, (self.posX, self.posY))
        #plateau[i][k] = 1      
        #print(int((self.posX - 250)//100), int((self.posY - 150)//100))
        
        
    def select(self):
        mousePos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mousePos) and self.selected == False:
            self.previousPos = (int((mousePos[0] - 250)//100), int((mousePos[1] - 150)//100))
            print(f"click sur {self.name}")
            self.selected = True


    def poser(self):
        mousePos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mousePos) and self.selected == True:
            self.newPos = (int((mousePos[0] - 250)//100), int((mousePos[1] - 150)//100))
            print(plateau[self.newPos[1]][self.newPos[0]])
            if ((abs(self.newPos[0] - self.previousPos[0]) == 1 and abs(self.newPos[1] - self.previousPos[1]) == 0) or (abs(self.newPos[0] - self.previousPos[0]) == 0 and abs(self.newPos[1] - self.previousPos[1]) == 1)) and plateau[self.newPos[1]][self.newPos[0]] == 0:
                # if self.rotation == 0 and self.newPos[1] == self.previousPos[1] + 1:
                #     self.selected = False
                #     self.rect.center = 250, 150
                #     self.rect.center = 250 + int((mousePos[0] - 250)/100)* square + square/2, 150 + int((mousePos[1] - 150)/100)* square + square/2
                #     self.posX, self.posY = self.rect.centerx - square/2, self.rect.centery - square/2
                #     print(f"reclick sur {self.name}")
                # elif self.rotation == 90 and self.newPos[0] == self.previousPos[0] + 1:
                #     self.selected = False
                #     self.rect.center = 250, 150
                #     self.rect.center = 250 + int((mousePos[0] - 250)/100)* square + square/2, 150 + int((mousePos[1] - 150)/100)* square + square/2
                #     self.posX, self.posY = self.rect.centerx - square/2, self.rect.centery - square/2
                #     print(f"reclick sur {self.name}")
                # elif self.rotation == -90 and self.newPos[0] == self.previousPos[0] - 1:
                #     self.selected = False
                #     self.rect.center = 250, 150
                #     self.rect.center = 250 + int((mousePos[0] - 250)/100)* square + square/2, 150 + int((mousePos[1] - 150)/100)* square + square/2
                #     self.posX, self.posY = self.rect.centerx - square/2, self.rect.centery - square/2
                #     print(f"reclick sur {self.name}")
                # elif self.rotation == 180 and self.newPos[1] == self.previousPos[1] - 1:
                self.placeAndSnap()
                print(f"reclick sur {self.name}")
            elif ((abs(self.newPos[0] - self.previousPos[0]) == 1 and abs(self.newPos[1] - self.previousPos[1]) == 0) or (abs(self.newPos[0] - self.previousPos[0]) == 0 and abs(self.newPos[1] - self.previousPos[1]) == 1)) and (plateau[self.newPos[1]][self.newPos[0]] == 2 or plateau[self.newPos[1]][self.newPos[0]] == 3 or plateau[self.newPos[1]][self.newPos[0]] == 4):
                if plateau[self.newPos[1]][self.newPos[0]] == 2:
                    mountain = mountain_1
                elif plateau[self.newPos[1]][self.newPos[0]] == 3:
                    mountain = mountain_2
                elif plateau[self.newPos[1]][self.newPos[0]] == 4:
                    mountain = mountain_3
                if self.newPos[0] - self.previousPos[0] == 1: #deplacement à droite
                    if plateau[self.newPos[1]][self.newPos[0] + 1] == 0: #verifie si piece à droite de montagne
                        mountain.posX += 100
                        mountain.rect.center = mountain.posX, mountain.posY
                        self.placeAndSnap()
                    else:
                        self.goBack()
                if self.newPos[0] - self.previousPos[0] == -1: #deplacement à gauche
                    if plateau[self.newPos[1]][self.newPos[0] - 1] == 0: #verifie si piece à gauche de montagne
                        mountain.posX -= 100
                        mountain.rect.center = mountain.posX, mountain.posY
                        self.placeAndSnap()
                    else:
                        self.goBack()
                if self.newPos[1] - self.previousPos[1] == 1: #deplacement en bas
                    if plateau[self.newPos[1] + 1][self.newPos[0]] == 0: #verifie si piece en bas de montagne
                        mountain.posY += 100
                        mountain.rect.center = mountain.posX, mountain.posY
                        self.placeAndSnap()
                    else:
                        self.goBack()
                if self.newPos[1] - self.previousPos[1] == -1: #deplacement en haut
                    if plateau[self.newPos[1] - 1][self.newPos[0]] == 0: #verifie si piece en haut de montagne
                        mountain.posY -= 100
                        mountain.rect.center = mountain.posX, mountain.posY
                        self.placeAndSnap()
                    else:
                        self.goBack()

            else:
                self.goBack()

    def goBack(self):
        self.selected = False
        self.posX = (self.previousPos[0]*100)+250
        self.posY = (self.previousPos[1]*100)+150
        self.rect.center = self.posX, self.posY
        self.newPos = (self.previousPos)
        print("Else")

    def placeAndSnap(self):
        mousePos = pygame.mouse.get_pos()

        self.selected = False
        self.rect.center = 250, 150
        self.rect.center = 250 + int((mousePos[0] - 250)/100)* square + square/2, 150 + int((mousePos[1] - 150)/100)* square + square/2
        self.posX, self.posY = self.rect.centerx - square/2, self.rect.centery - square/2
        plateau[self.newPos[1]][self.newPos[0]] = 1
        plateau[self.previousPos[1]][self.previousPos[0]] = 0


    def move(self, x, y):
        if self.selected == True:
            self.posX = x - square/2
            self.posY = y - square / 2
            self.rect.center = x, y

    def rotate(self, degres):
        mousePos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mousePos):
            self.image = pygame.transform.rotate(self.image, degres)
            self.rotation += degres 
        
            
class Elephant:
    previousPos = (0,0)
    newPos = (0,0)

    def __init__(self, _screen, posX : int, posY : int, image, name : str, rotation):
        self.posX = posX
        self.posY = posY
        self.image = pygame.transform.scale(image, (square, square))
        self.rect = self.image.get_rect()
        self.rect.center = posX + square/2, posY+square/2
        self.selected = False
        self.canPlace = True 
        self.name = str(name)
        self.rotation = rotation
        self.forceElephant = 1
    

    def Update(self):
        mousePos = pygame.mouse.get_pos()
        screen.blit(self.image, (self.posX, self.posY))
        #plateau[i][k] = 1      
        #print(int((self.posX - 250)//100), int((self.posY - 150)//100))

    def select(self):
        mousePos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mousePos) and self.selected == False:
            self.previousPos = (int((mousePos[0] - 250)//100), int((mousePos[1] - 150)//100))
            print(f"click sur {self.name}")
            self.selected = True
        
    def poser(self):
        mousePos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mousePos) and self.selected == True:
            self.newPos = (int((mousePos[0] - 250)//100), int((mousePos[1] - 150)//100))
            print(plateau[self.newPos[1]][self.newPos[0]])
            if ((abs(self.newPos[0] - self.previousPos[0]) == 1 and abs(self.newPos[1] - self.previousPos[1]) == 0) or (abs(self.newPos[0] - self.previousPos[0]) == 0 and abs(self.newPos[1] - self.previousPos[1]) == 1)) and plateau[self.newPos[1]][self.newPos[0]] == 0:
                # if self.rotation == 0 and self.newPos[1] == self.previousPos[1] + 1:
                #     self.selected = False
                #     self.rect.center = 250, 150
                #     self.rect.center = 250 + int((mousePos[0] - 250)/100)* square + square/2, 150 + int((mousePos[1] - 150)/100)* square + square/2
                #     self.posX, self.posY = self.rect.centerx - square/2, self.rect.centery - square/2
                #     print(f"reclick sur {self.name}")
                # elif self.rotation == 90 and self.newPos[0] == self.previousPos[0] + 1:
                #     self.selected = False
                #     self.rect.center = 250, 150
                #     self.rect.center = 250 + int((mousePos[0] - 250)/100)* square + square/2, 150 + int((mousePos[1] - 150)/100)* square + square/2
                #     self.posX, self.posY = self.rect.centerx - square/2, self.rect.centery - square/2
                #     print(f"reclick sur {self.name}")
                # elif self.rotation == -90 and self.newPos[0] == self.previousPos[0] - 1:
                #     self.selected = False
                #     self.rect.center = 250, 150
                #     self.rect.center = 250 + int((mousePos[0] - 250)/100)* square + square/2, 150 + int((mousePos[1] - 150)/100)* square + square/2
                #     self.posX, self.posY = self.rect.centerx - square/2, self.rect.centery - square/2
                #     print(f"reclick sur {self.name}")
                # elif self.rotation == 180 and self.newPos[1] == self.previousPos[1] - 1:
                self.placeAndSnap()
                print(f"reclick sur {self.name}")
            elif ((abs(self.newPos[0] - self.previousPos[0]) == 1 and abs(self.newPos[1] - self.previousPos[1]) == 0) or (abs(self.newPos[0] - self.previousPos[0]) == 0 and abs(self.newPos[1] - self.previousPos[1]) == 1)) and (plateau[self.newPos[1]][self.newPos[0]] == 2 or plateau[self.newPos[1]][self.newPos[0]] == 3 or plateau[self.newPos[1]][self.newPos[0]] == 4):
                if plateau[self.newPos[1]][self.newPos[0]] == 2:
                    mountain = mountain_1
                elif plateau[self.newPos[1]][self.newPos[0]] == 3:
                    mountain = mountain_2
                elif plateau[self.newPos[1]][self.newPos[0]] == 4:
                    mountain = mountain_3
                if self.newPos[0] - self.previousPos[0] == 1: #deplacement à droite
                    if plateau[self.newPos[1]][self.newPos[0] + 1] == 0: #verifie si piece à droite de montagne
                        mountain.posX += 100
                        mountain.rect.center = mountain.posX, mountain.posY
                        self.placeAndSnap()
                    else:
                        self.goBack()
                if self.newPos[0] - self.previousPos[0] == -1: #deplacement à gauche
                    if plateau[self.newPos[1]][self.newPos[0] - 1] == 0: #verifie si piece à gauche de montagne
                        mountain.posX -= 100
                        mountain.rect.center = mountain.posX, mountain.posY
                        self.placeAndSnap()
                    else:
                        self.goBack()
                if self.newPos[1] - self.previousPos[1] == 1: #deplacement en bas
                    if plateau[self.newPos[1] + 1][self.newPos[0]] == 0: #verifie si piece en bas de montagne
                        mountain.posY += 100
                        mountain.rect.center = mountain.posX, mountain.posY
                        self.placeAndSnap()
                    else:
                        self.goBack()
                if self.newPos[1] - self.previousPos[1] == -1: #deplacement en haut
                    if plateau[self.newPos[1]][self.newPos[0] - 1] == 0: #verifie si piece en haut de montagne
                        mountain.posY -= 100
                        mountain.rect.center = mountain.posX, mountain.posY
                        self.placeAndSnap()
                    else:
                        self.goBack()

            else:
                self.goBack()

    def goBack(self):
        self.selected = False
        self.posX = (self.previousPos[0]*100)+250
        self.posY = (self.previousPos[1]*100)+150
        self.rect.center = self.posX, self.posY
        self.newPos = (self.previousPos)
        print("Else")

    def placeAndSnap(self):
        mousePos = pygame.mouse.get_pos()

        self.selected = False
        self.rect.center = 250, 150
        self.rect.center = 250 + int((mousePos[0] - 250)/100)* square + square/2, 150 + int((mousePos[1] - 150)/100)* square + square/2
        self.posX, self.posY = self.rect.centerx - square/2, self.rect.centery - square/2
        plateau[self.newPos[1]][self.newPos[0]] = 1
        plateau[self.previousPos[1]][self.previousPos[0]] = 0


    def move(self, x, y):
        if self.selected == True:
            self.posX = x - square/2
            self.posY = y - square / 2
            self.rect.center = x, y

    def rotate(self, degres):
        mousePos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mousePos):
            self.image = pygame.transform.rotate(self.image, degres)
            self.rotation += degres 
        

    def goBack(self):
        self.selected = False
        self.posX = (self.previousPos[0]*100)+250
        self.posY = (self.previousPos[1]*100)+150
        self.rect.center = self.posX, self.posY
        self.newPos = (self.previousPos)
        print("Else")

    def placeAndSnap(self):
        mousePos = pygame.mouse.get_pos()

        self.selected = False
        self.rect.center = 250, 150
        self.rect.center = 250 + int((mousePos[0] - 250)/100)* square + square/2, 150 + int((mousePos[1] - 150)/100)* square + square/2
        self.posX, self.posY = self.rect.centerx - square/2, self.rect.centery - square/2
        plateau[self.newPos[1]][self.newPos[0]] = 1
        plateau[self.previousPos[1]][self.previousPos[0]] = 0
        
    def move(self, x, y):
        if self.selected == True:
            self.posX = x - square/2
            self.posY = y - square / 2
            self.rect.center = x, y

    def rotate(self, degres):
        mousePos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mousePos):
            self.image = pygame.transform.rotate(self.image, degres)
            self.rotation += degres


class Montagne:
    def __init__(self, _screen, posX : int, posY : int, image, name : str, type : int):
        self.posX = posX
        self.posY = posY
        self.image = pygame.transform.scale(image, (square, square))
        self.rect = self.image.get_rect()
        self.rect.center = posX + square/2, posY + square/2
        self.type = type
    
    def Update(self):
        screen.blit(self.image, (self.posX, self.posY))
        plateau[int((self.posY - 150)//100)][int((self.posX - 250)//100)] = self.type


rhino_1 = Rhino(screen, 250, 750, rhino, "rhino_1", 0)
rhino_2 = Rhino(screen, 350, 750, rhino, "rhino_2", 0)
rhino_3 = Rhino(screen, 450, 750, rhino, "rhino_3", 0)
rhino_4 = Rhino(screen, 550, 750, rhino, "rhino_4", 0)
rhino_5 = Rhino(screen, 650, 750, rhino, "rhino_5", 0)

eleph_1 = Rhino(screen, 250, 150, eleph, "eleph_1", 180)
eleph_2 = Rhino(screen, 350, 150, eleph, "eleph_2", 180)
eleph_3 = Rhino(screen, 450, 150, eleph, "eleph_3", 180)
eleph_4 = Rhino(screen, 550, 150, eleph, "eleph_4", 180)
eleph_5 = Rhino(screen, 650, 150, eleph, "eleph_5", 180)

mountain_1 = Montagne(screen, 350, 450, mont, "mountain_1", 2)
mountain_2 = Montagne(screen, 450, 450, mont, "mountain_2", 3)
mountain_3 = Montagne(screen, 550, 450, mont, "mountain_3", 4)
        
pieces = [rhino_1, rhino_2, rhino_3, rhino_4, rhino_5, eleph_1, eleph_2, eleph_3, eleph_4, eleph_5, mountain_1, mountain_2, mountain_3]  
pions = [rhino_1, rhino_2, rhino_3, rhino_4, rhino_5, eleph_1, eleph_2, eleph_3, eleph_4, eleph_5]

piecesRects = [rhino_1.rect, rhino_2.rect, rhino_3.rect, rhino_4.rect, rhino_5.rect, eleph_1.rect, eleph_2.rect, eleph_3.rect, eleph_4.rect, eleph_5.rect, mountain_1.rect, mountain_2.rect, mountain_3.rect]
mountains = [mountain_1, mountain_2, mountain_3]

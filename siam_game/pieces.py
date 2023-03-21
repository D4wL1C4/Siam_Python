import pygame
from siam_game.plateau import *
from siam_game.ressources import *



class Rhino:
    def __init__(self, _screen, posX : int, posY : int, image, name : str):
        self.posX = posX
        self.posY = posY
        self.image = pygame.transform.scale(image, (square, square))
        self.rect = self.image.get_rect()
        self.rect.center = posX + square/2, posY+square/2
        self.selected = False
        self.canPlace = True
        self.name = str(name)

    def Update(self):
        mousePos = pygame.mouse.get_pos()

        screen.blit(self.image, (self.posX, self.posY))

        
    def select(self):
        mousePos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mousePos) and self.selected == False:
            print(f"click sur {self.name}")
            self.selected = True
        elif self.rect.collidepoint(mousePos) and self.selected == True and self.canPlace == True: 
            piecesRects.remove(f"{self.name}.rect")
            for rect in piecesRects:
                if rect.colliderect(self.rect):
                    print("intersect")
                # ne pas poser
                else:
                    self.selected = False
                    self.rect.center = 250, 250
                    self.rect.center = 250 + int((mousePos[0] - 250)/100)* square + square/2, 250 + int((mousePos[1] - 250)/100)* square + square/2
                    self.posX, self.posY = self.rect.centerx - square/2, self.rect.centery - square/2
                    print(f"reclick sur {self.name}")
            piecesRects.append(f"{self.name}.rect")

    def move(self, x, y):
        if self.selected == True:
            self.posX = x - square/2
            self.posY = y - square / 2
            self.rect.center = x, y
            
class Montagne:
    def __init__(self, _screen, posX : int, posY : int, image, name : str):
        self.posX = posX
        self.posY = posY
        self.image = pygame.transform.scale(image, (square, square))
        self.rect = self.image.get_rect()
        self.rect.center = posX + square/2, posY+square/2
    
    def Update(self):
        screen.blit(self.image, (self.posX, self.posY))


rhino_1 = Rhino(screen, 250, 750, rhino, "rhino_1")
rhino_2 = Rhino(screen, 350, 750, rhino, "rhino_2")
rhino_3 = Rhino(screen, 450, 750, rhino, "rhino_3")
rhino_4 = Rhino(screen, 550, 750, rhino, "rhino_4")
rhino_5 = Rhino(screen, 650, 750, rhino, "rhino_5")

eleph_1 = Rhino(screen, 250, 150, eleph, "eleph_1")
eleph_2 = Rhino(screen, 350, 150, eleph, "eleph_2")
eleph_3 = Rhino(screen, 450, 150, eleph, "eleph_3")
eleph_4 = Rhino(screen, 550, 150, eleph, "eleph_4")
eleph_5 = Rhino(screen, 650, 150, eleph, "eleph_5")

mountain_1 = Montagne(screen, 350, 450, mont, "mountain_1")
mountain_2 = Montagne(screen, 450, 450, mont, "mountain_2")
mountain_3 = Montagne(screen, 550, 450, mont, "mountain_3")
        
pieces = [rhino_1, rhino_2, rhino_3, rhino_4, rhino_5, eleph_1, eleph_2, eleph_3, eleph_4, eleph_5, mountain_1, mountain_2, mountain_3]  

piecesRects = [rhino_1.rect, rhino_2.rect, rhino_3.rect, rhino_4.rect, rhino_5.rect, eleph_1.rect, eleph_2.rect, eleph_3.rect, eleph_4.rect, eleph_5.rect, mountain_1.rect, mountain_2.rect, mountain_3.rect]


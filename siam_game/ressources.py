import pygame
import os

screen = pygame.display.set_mode((1000, 1000))
pygame.font.init()

#definition de la taille de l'ecran
screen_width = 1000
screen_height = 1000


#le nombre de lignes et de colonnes
row = 5
col = 5 

#nombre cases 
case_number = row * col

square = 100

#definition des couleurs des cases du plateau
color1 = (195,142,95)
color2 = (117,162,203)

#Charger les pieces
#Rhinocéros
rhino = pygame.image.load("siam_game/sources/rhino.png")
rhino = pygame.transform.scale(rhino, (square, square))

#elephant
eleph = pygame.image.load("siam_game/sources/elephant.png")
eleph = pygame.transform.scale(eleph, (square, square))

#montagne
mont = pygame.image.load("siam_game/sources/montagne.png")
mont = pygame.transform.scale(mont, (square, square))

bgImage = pygame.image.load("siam_game/sources/bg_siam.png")
bgImage = pygame.transform.scale(bgImage, (1500,1000))

play = pygame.image.load("siam_game/sources/TitlePlay.png")
play = pygame.transform.scale_by(play, .5)

registerButton = pygame.image.load("siam_game/sources/Register.png")
loginButton = pygame.image.load("siam_game/sources/login.png")

Titlefont = pygame.font.Font("siam_game/sources/Comics Deluxe.ttf", 200)
textfont = pygame.font.Font("siam_game/sources/Comics Deluxe.ttf", 50)

register_rect = registerButton.get_rect()
register_rect.topleft = (30,550)

login_rect = loginButton.get_rect()
login_rect.topleft = (30,650)

register_rect2 = registerButton.get_rect()
register_rect2.topleft = (670,550)

login_rect2 = loginButton.get_rect()
login_rect2.topleft = (670,650)

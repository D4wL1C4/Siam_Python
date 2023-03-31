import csv
import pygame

from siam_game.ressources import *
from siam_game.pieces import *
from siam_game.plateau import drawPlate  

clock = pygame.time.Clock()
rhino_rect = pygame.Surface.get_rect(rhino)



def initGame():
    pygame.init()
    pygame.font.init()
    #dessiner le plateau et placer tous les pions au bon endroit
    drawPlate(screen, color1, color2, 250, 250, square, square) #Plateau

def MainMenu():
    initGame()
    pygame.display.set_caption("Menu principal")
    run = True
    fps = 60

    play_rect = play.get_rect()
    play_rect.topleft = 300,400

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
                    screen.fill((0,0,0))
                    Accounts()
        Title = Titlefont.render("SIAM", 1, (255,255,255))
        screen.blit(bgImage, (0,0))
        screen.blit(play,(300,400))
        screen.blit(Title, (220, 100))
        pygame.display.flip()    

def register():
    with open('user.csv', "r+", newline='') as f:
        table = list(csv.DictReader(f, delimiter=";"))
        username = input("Entre ton pseudo pour t'inscrire : ")
        for i in range(len(table)):
            if table[i]["Username"] == username:
                print("Ce nom d'utilisateur existe déjà")
                register()
        writer = csv.writer(f, delimiter=';')
        password = input('Entre ton mot de passe : ')
        passw2 = input('Entre le encore une fois : ')

        if password == passw2:
            writer.writerow([username, password])
            print('Inscription réussi !')
        else:
            print("Ton mot de passe n'est pas le même")

def login():
    username = input('Entre ton pseudo pour te connecter : ')
    password = input('Entre ton mot de passe : ')
    with open('user.csv', mode = 'r') as f:
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            if row == [username, password]: 
                print('loged in')
                return username
        print("Ton nom d'utilisateur ou ton mot de passe est erroné ou n'existe pas")
        return False
    
def login2():
    username = input('Entre ton pseudo pour te connecter : ')
    password = input('Entre ton mot de passe : ')
    with open('user.csv', mode = 'r') as f:
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            if row == [username, password]: 
                print('loged in')
                return username
        print("Ton nom d'utilisateur ou ton mot de passe est erroné ou n'existe pas")
        return False

def Accounts():
    logins = 0
    pygame.display.set_caption("Comptes")
    run = True
    fps = 60

    while run:
        mousePos = pygame.mouse.get_pos()
        clock.tick(fps)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if register_rect.collidepoint(mousePos):
                    register()
                if login_rect.collidepoint(mousePos):
                    joueur1 = login()
                    player1_txt = textfont.render(f"Joueurs 1 : {joueur1}", 1, (255,255,255))
                    logins += 1
                if register_rect2.collidepoint(mousePos):
                    register()
                if login_rect2.collidepoint(mousePos):
                    joueur2 = login()
                    player2_txt = textfont.render(f"Joueurs 2 : {joueur2}", 1, (255,255,255))
                    screen.blit(player2_txt, (650,450))
                    logins += 1
            if logins >= 2:
                MainGame() 
            if logins == 1:
                screen.blit(player1_txt, (15,450)) 
        #Textes
        Title = Titlefont.render("SIAM", 1, (255,255,255))
        

        screen.blit(bgImage, (0,0))

        #Buttons
        #Player 1 : 
        screen.blit(registerButton, (30,550))
        screen.blit(loginButton,(30,650))

        #Player 2 :
        screen.blit(registerButton, (670,550))
        screen.blit(loginButton,(670,650))

        #Afficher les textes
        screen.blit(Title, (220,100))
        
        
        pygame.display.flip()

def selectPlayers():
    with open("user.csv", "r") as f:
        users = list(csv.reader(f, delimiter=";"))
    
    pygame.display.set_caption("Joueurs")
    run = True
    fps = 60

    joueur1 = login()
    joueur2 = login()

    while run:
        mousePos = pygame.mouse.get_pos()
        clock.tick(fps)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
        
        ### Textes à afficher
        Title = Titlefont.render("SIAM", 1, (255,255,255))
        player1 = textfont.render(f"Joueurs 1 : {joueur1}", 1, (255,255,255))
        player2 = textfont.render(f"Joueurs 2 : {joueur2}", 1, (255,255,255))

        screen.blit(bgImage, (0,0))

        ### Afficher ces textes
        screen.blit(Title, (220,100))
        screen.blit(player1, (30,450))
        screen.blit(player2, (30,650))
        pygame.display.flip()
        
def MainGame():
    pygame.display.set_caption("Fenêtre de jeu")
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
                    if piecesSelected == 1:
                        for piece in pions:
                            piece.poser()
                            piecesSelected = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    for piece in pions:
                        piece.rotate(90)
                if event.key == pygame.K_LEFT:
                    for piece in pions:
                        piece.rotate(-90)
        screen.fill((0,0,0))   
        screen.blit(bgImage, (0,0))   
        drawPlate(screen, color1, color2, 250, 250, square, square)       
        for i in range(7):
            for k in range(5):
                plateau[i][k] = 0     
        for piece in pieces:
            piece.Update()
        pygame.display.flip()
        
MainGame()

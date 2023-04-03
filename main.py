import csv
import pygame

#importe les fichier.py dans le dossier "siam_game"
from siam_game.ressources import *
from siam_game.pieces import *
from siam_game.plateau import drawPlate  

def initGame():
    pygame.init()
    pygame.font.init()
    #dessiner le plateau et placer tous les pions au bon endroit
    drawPlate(screen, color1, color2, 250, 250, square, square)

#Menu principal
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
#s'inscrire
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
            print('Inscription réussie !')
        else:
            print("Ton mot de passe n'est pas le même")

def login():
    username = input('Entre ton pseudo pour te connecter : ')
    password = input('Entre ton mot de passe : ')
    with open('user.csv', mode = 'r') as f:
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            if row == [username, password]: 
                print('Connecté')
                return username
        print("Ton nom d'utilisateur ou ton mot de passe est erroné ou n'existe pas")
        return False
    

    username = input('Entre ton pseudo pour te connecter : ')
    password = input('Entre ton mot de passe : ')
    with open('user.csv', mode = 'r') as f:
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            if row == [username, password]: 
                print('Connecté !')
                return username
        print("Ton nom d'utilisateur ou ton mot de passe est erroné ou n'existe pas")
        return False

def Accounts():
    global joueur1
    global joueur2
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
        #Textes
        Title = Titlefont.render("SIAM", 1, (255,255,255))
        player1_txt = textfont.render("Joueurs 1 : ", 1, (255,255,255))
        player2_txt = textfont.render("Joueurs 2 : ", 1, (255,255,255))
        screen.blit(bgImage, (0,0))

        #Buttons
        #Player 1 : 
        screen.blit(player1_txt, (30,400))
        screen.blit(registerButton, (30,550))
        screen.blit(loginButton,(30,650))

        #Player 2 :
        screen.blit(player2_txt, (650, 400))
        screen.blit(registerButton, (670,550))
        screen.blit(loginButton,(670,650))

        #Afficher les textes
        screen.blit(Title, (220,100))
        
        
        pygame.display.flip()
        
def MainGame():
    global joueur1
    global joueur2
    
    pygame.display.set_caption("Fenêtre de jeu")
    run = True
    fps = 60
    piecesSelected = 0
    while run:
        
        clock.tick(fps)
        pygame.display.update()
        mousePos = pygame.mouse.get_pos() #récupère la position du curseur
        caseIndexX = int((mousePos[0] - 250)/100) # transforme le résultat en index de colonnes / lignes (ex : 0;1 --- 3;4 etc...)
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
            if event.type == pygame.MOUSEBUTTONDOWN: 
                if pygame.mouse.get_pos()[0] > 150 and pygame.mouse.get_pos()[0] < 850 and pygame.mouse.get_pos()[1] > 150 and pygame.mouse.get_pos()[1] < 850:
                    print(caseIndexX, caseIndexY) 
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

        ### Textes à afficher
        player1 = textfont.render(joueur1, 1, (255,255,255))
        player2 = textfont.render(joueur2, 1, (255,255,255))

        ### Afficher ces textes
        screen.blit(player1, (70,5))
        screen.blit(player2, (750,920))

        drawPlate(screen, color1, color2, 250, 250, square, square)
        for piece in pieces:
            piece.Update()
        CheckEndGame()
        pygame.display.flip()
        
def CheckEndGame():
    for i in range(6):
        if plateau[i][0] == 2 or plateau[i][0] == 3 or plateau[i][0] == 4:
            MainMenu()
        elif plateau[i][6] == 2 or plateau[i][6] == 3 or plateau[i][6] == 4:
            MainMenu()
        elif plateau[0][i] == 2 or plateau[0][i] == 3 or plateau[0][i] == 4:
            MainMenu()
        elif plateau[6][i] == 2 or plateau[6][i] == 3 or plateau[6][i] == 4:
            MainMenu()

MainMenu() 

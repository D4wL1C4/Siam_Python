import csv 

logedIn = False

def register():
    with open('user.csv', "r+", newline='') as f:
        table = list(csv.DictReader(f, delimiter=";"))
        print(table)
        
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
            print('registration succesfull')
        else:
            print('try again')


def login():
    username = input('Entre ton pseudo pour te connecter : ')
    password = input('Entre ton mot de passe : ')
    with open('user.csv', mode = 'r') as f:
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            if row == [username, password]: 
                print('loged in')
                logedIn = True
                print(logedIn)
                return True
        print("Ton nom d'utilisateur ou ton mot de passe est erroné ou n'existe pas")
        return False

    
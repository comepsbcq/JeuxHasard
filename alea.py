import os
from random import *


# Déclarations des variables représentant les couleurs du CMD
ROUGE = '\033[91m'
VERT = '\033[92m'
JAUNE = '\033[93m'
BLEU = '\033[94m'
RESET = '\033[0m'
GRAS = '\033[1m'


# Deux mini-menus permettant de proposer au joueur de rejouer leur jeu ou retourner au menu.
def rejouerDES():
    rejouer = input("Souhaitez-vous rejouer ou retourner au menu ? (Rejouer/menu) : ").lower()
    if rejouer == "rejouer":
        des()
    elif rejouer == "menu":
        start()
    else :
        print("Synthax error: please type only the selected option.")
        rejouerDES()

def rejouerPF():
    rejouer = input("Souhaitez-vous re-faire un tirage ou retourner au menu ? (Rejouer/menu) : ").lower()
    if rejouer == "rejouer":
        pf()
    elif rejouer == "menu":
        start()
    else :
        print("Synthax error: please type only the selected option.")
        rejouerPF()

def rejouerMM():
    rejouer = input("Souhaitez-vous rejouer ou retourner au menu ? (Rejouer/menu) : ").lower()
    if rejouer == "rejouer":
        mastermind()
    elif rejouer == "menu":
        start()
    else :
        print("Synthax error: please type only the selected option.")
        rejouerMM()
    
# Système de lancer de dé basé sur le mode random (randint) proposé par python.
def des():
    os.system('cls')
    print('Bienvenue dans le lancer de dé !\nCombien de fois voulez-vous que le dé soit lancé ?')
    nbDES = int(input())
    loop = True
    count = 0
    while loop == True:
        count = count + 1
        d = randint(1,6)
        print("Votre lancer a donné : ", d)
        if count == nbDES:
            loop = False
    rejouerDES()

# Mode de jeu Mastermind, tiré du jeu de société.
def mastermind():
    os.system('cls')
    print(f"{VERT}Bienvenue dans le {ROUGE}{GRAS}Master{RESET}{GRAS}Mind !\n{RESET}{VERT}Le principe du jeu est simple : quatre couleurs vont être choisies par l'ordinateur. Vous devrez les deviner.")
    USER_CHOICE = input("Avez-vous comprit ? (Oui/non) ").lower()
    if USER_CHOICE == "oui":
        loopMM = True
        os.system('cls')
        couleurs = ['rouge', 'vert', 'bleu', 'jaune', 'blanc', 'noir']
        couleur1 = choice(couleurs)
        couleur2 = choice(couleurs)
        couleur3 = choice(couleurs)
        couleur4 = choice(couleurs)
        print("Vous allez désormais être demandé sur les quatre couleurs (une à une)")
        print("Les couleurs disponibles sont rouge, vert, bleu, jaune, blanc et noir.")
        while loopMM == True:
            bonnereponse = 0
            couleur1avis = input("Quelle couleur pensez-vous être en première position ? ").lower()
            couleur2avis = input("Quelle couleur pensez-vous être en deuxième position ? ").lower()
            couleur3avis = input("Quelle couleur pensez-vous être en troisième position ? ").lower()
            couleur4avis = input("Quelle couleur pensez-vous être en quatrième position ? ").lower()
            if couleur1avis == couleur1:
                bonnereponse = bonnereponse +1
            if couleur2avis == couleur2:
                bonnereponse = bonnereponse +1
            if couleur3avis == couleur3:
                bonnereponse = bonnereponse +1
            if couleur4avis == couleur4:
                bonnereponse = bonnereponse +1
            if bonnereponse == 4:
                print("Félicitation! Vous avez trouver les quatre couleurs !")
                loopMM = False
            if 4 > bonnereponse >= 0:
                print("Vous avez trouvé", bonnereponse, "couleur(s). Réessayez !")
        os.system('pause')
        rejouerMM()
    elif USER_CHOICE == "non":
        mastermind()
    else :
        print("Synthax error : please type the selected option.")
        mastermind()

# Système de pile ou face basé sur un nombre aléatoire en 0 et 1000 
def pf():
    os.system('cls')
    print('Bienvenue au Pile Ou Face !\n Choisissez votre pari (pile/face)')
    pf = input().lower()
    if pf == "pile": 
        x = randint(0,1000)
        if x > 500: 
            print("Le tirage a donné pile. J'espère que vous aviez parier gros.")
            rejouerPF()
        else :
            print("Le tirage a donné face. Dieu merci vous aviez parier gros.")
            rejouerPF()
    elif pf == "face":
        x = randint(0,1000)
        if x > 500:
            print("Le tirage a donné pile. Dieu merci vous aviez parier gros.")
            rejouerPF()
        else :
            print("Le tirage a donné face. Ce n'est que de la chance.")
            rejouerPF()
    else :
        print("Synthax error: please type only the selected option.")

# Création du mode BlackJack (le plus compliqué je pense)
def blackjack():
    # Déclaration des valeurs de chacune des cartes
    valeurs = ['0', '2', '3', '4', '5', '6', '7', '8', '9', '10', '10', '10', '10']
    os.system('cls')
    print("Bienvenue au BlackJack !\nCe jeu fonctionne comme au casino, c'est à dire avec des jetons limités (en cas de perte totale des jetons, ils vous seront remis à zéro).")
    print(f"{ROUGE}Attention : jouer peut entraîner des {GRAS}RISQUE D'ADDICTION.{RESET}{VERT}")
    user_choice = input("Voulez-vous continuer ? (oui/non) ").lower()
    if user_choice == "oui":
        os.system('cls')
        # Explication des règles
        print("Pour rappeler les règles : vous commence avec deux cartes. Celle-ci ont une valeur allant de 2 à 11. L'intégralité des cartes possèdent la valeur écrite dessus, mis à part le valet, la dame, le roi qui valent 10 et l'as qui vaut 11 ou 1 en fonction du contexte. Vous pouvez choisir de vous retirer, ou de repiocher une carte. Si la valeur totale de vos cartes dépassent 21, vous avez perdu. Cependant, vous devez faire en sorte de dépasser le croupier, qui joue selon les mêmes principes.")
        os.system('pause')
        os.system('cls')
        # Récupération des jetons que le joueur possède
        f = open('coins.txt', 'r')
        jetons = f.read()
        if jetons.isdigit():
            jetons = int(jetons)
        else:
            print("Le fichier contient un format non valide.")
            jetons = 1000
        f.close()
        # Création de la mise
        miser = True
        while miser == True:
            print("Vous possédez", jetons, "jetons, combien souhaitez-vous miser ?")
            mise = int(input())
            if mise <= 0:
                print("Vous ne pouvez pas poser une mise nulle.")
            if mise > jetons:
                print("Vous ne pouvez pas miser plus que ce que vous posséder.")
            else:
                print("Votre mise est de", mise, ".")
                jetons = int(jetons) - int(mise)
                miser = False
        # Génération des cartes et création de la valeur
        valeur = 0
        carte1 = randint(2,11)
        carte2 = randint(2,11)
        valeur = carte1 + carte2
        carte1BOT = randint(2,11)
        carte2BOT = randint(2,11)
        valeurBOT = carte1BOT + carte2BOT
        print("Vous commencez donc avec ", carte1, carte2, ".  Le croupier, lui, a ", carte1BOT, carte2BOT, ".")
        boucle = True
        while boucle == True:
            print("Votre valeur est de : ", valeur, " et celle du croupier est de : ", valeurBOT)
            pickornot = input("\nSouhaitez-vous prendre une carte ou arrêter là ? (Prendre/stop) ").lower()
            if pickornot == "prendre":
                carte = choice(valeurs)
                if carte == 0:
                    ELEVENORONE = valeur +11
                    if ELEVENORONE > 21:
                        carte = 1
                    else:
                        carte = 11
                else:
                    valeur = int(valeur) + int(carte)
            if pickornot == "stop":
                loop = True
                print("Vous avez choisi de vous arrêter. Le croupier va, à son tour, jouer.")
                while loop == True:
                    pickornot2 = randint(0,1000)
                    if pickornot2 > 500:
                        carteBOT = choice(valeurs)
                        valeurBOT = int(valeurBOT) + int(carteBOT)
                        print("La valeur du croupier est donc de : ", valeurBOT)
                    else :
                        loop = False
                        print("Le croupier a décidé de s'arrêter. La valeur finale du croupier est donc de : ", valeurBOT)
                        boucle = False
                if 22 > valeur > valeurBOT:
                    print("\nFélicitation ! Vous avez gagné ! Votre valeur est de ", valeur, " et celle du croupier est de ", valeurBOT, ".")
                    jetons = int(jetons) + int(mise)*2
                    UPDATECOINS = open("coins.txt", "w")
                    jetons = str(jetons)
                    UPDATECOINS.write(str(jetons))
                    UPDATECOINS.close()
                    boucle = False
                if valeur < valeurBOT < 21:
                    print("\nPerdu ! Votre valeur est de ", valeur, " et celle du croupier est de ", valeurBOT, ".")
                    UPDATECOINS = open("coins.txt", "w")
                    jetons = str(jetons)
                    UPDATECOINS.write(str(jetons))
                    UPDATECOINS.close()
                    boucle = False
            if valeur >= 22:
                print("\nPerdu ! Votre valeur est de ", valeur, " et celle du croupier est de ", valeurBOT, ".")
                UPDATECOINS = open("coins.txt", "w")
                jetons = str(jetons)
                UPDATECOINS.write(str(jetons))
                UPDATECOINS.close()
                boucle = False
            if valeurBOT >= 22:
                print("\nFélicitation ! Vous avez gagné ! Votre valeur est de ", valeur, " et celle du croupier est de ", valeurBOT, ".")
                jetons = int(jetons) + int(mise)*2
                UPDATECOINS = open("coins.txt", "w")
                jetons = str(jetons)
                UPDATECOINS.write(str(jetons))
                UPDATECOINS.close()
                boucle = False
        rejouer = input("\nSouhaitez-vous rejouer ? ").lower()
        if rejouer == "oui":
            blackjack()
        if rejouer == "non":
          start()
        else:
            print("Synthax error: please type only the selected option.")
    elif user_choice == "non":
        start()
    else :
        print("Synthax error: please type only the selected option.")


# Menu d'accueil permettant le choix entre les jeux et fermer l'application.
def start():
    os.system('cls')
    os.system('color 2')
    print("Bienvenue au jeu de l'aléatoire !\nCe programme vous permet de jouer à différent jeux d'aléatoires comme pile ou face, quel symbole du jeu de carte, faire des lancés de dés, etc.\nCe programme a été créé par Côme PASBECQ.")
    print("Veuillez choisir quelle fonction vous voulez parmi les suivantes :\n  - Lancer de dés (1)\n  - Pile ou face (2)\n  - Black Jack (3)\n  - Fermer le programme (5)")
    user_choice = int(input("Votre choix (uniquement le chiffre associé): "))
    if user_choice == 1 :
        des()
    elif user_choice == 2 :
        pf()
    elif user_choice == 3 :
        blackjack()
    elif user_choice == 5 :
        print('Fermeture du programme.')
        os.system('pause')
    else :
        print("Synthax error: unknown value")
        os.system('pause')
        start()


start()

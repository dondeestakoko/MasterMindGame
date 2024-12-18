from MasterMind import *
chances = 10 #nombre maximale d'essais

def main_game(chances):
    in_game = True
    secret_combo = generate_secret_combo(colors)
    while (in_game == True) and (chances != 0): #tant que pas gagné ET essais restants
        player = player_input()
        print(player)
        result = verification(player, secret_combo)
        print("Nombre de couleur et place Exacte:", result[0])
        print("Nombre de fausses Places:", result[1])
        if result[0] == len(player): #si la couleur et place Exacte sur toutes les places
            in_game = False #condition d'arret du jeu
            print('!!!!!!!! FELICITATION Vous avez gagné !!!!!')
            print('Votre SCORE est: ' + str(chances))
        else:
            chances -= 1 #decrementer les chances (deuxieme condition d'arret)
            print('vous avez echouer mais ne vous abondonez pas')
            print('votre score est: ' + str(chances))

main_game(chances)
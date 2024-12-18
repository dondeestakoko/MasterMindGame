import random


chances = 10 #nombre maximale d'essais
colors = ['red', 'yellow', 'blue', 'green', 'purple', 'pink'] #les couleurs possibles

# print(random.sample(colors, 4)) #selectioner 4 couleurs aleatoire


def generate_secret_combo(colors):   #fonction qui genere la combinaison aleatoire
    secret = random.sample(colors, 4) #choise aleatoirement quatre couleur des couleurs predefini
    return secret

def player_input():
    liste_couleurs =[] # liste vide des couleur choisit par le user
    for index in range(1, 5): #limiter le nombre de couleur a quatre
        combo = input('Entrez la ' + str(index) + ' couleur: ').lower() #demander a l'utilisateur d'entrer les valeurs
        while combo not in colors: 
            print('Votre couleur n''existe pas dans: ' + str(colors)) # message d'ereurs
            combo = input('Reéssayer la ' + str(index) + ' couleur: ').lower() 
        liste_couleurs.append(combo) #ajouter a la liste
    return liste_couleurs

def verification(player_input, secret_combo):
    right_place_and_color = 0
    right_color_worng_place = 0
    unmatched_secret = list(secret_combo)  # une liste a modifer
    unmatched_player = []  # les couleurs maivaise position

    for color1 in range(len(player_input)):
        if player_input[color1] == secret_combo[color1]:
            right_place_and_color += 1  # Incrementer pour position et couleur correcte
            unmatched_secret[color1] = None  # marquer comme deja trouver
        else:
            unmatched_player.append(player_input[color1])
            
    for color2 in unmatched_player:
        if color2 in unmatched_secret:
            right_color_worng_place += 1  # Incrementer pour position fausse
            unmatched_secret[unmatched_secret.index(color2)] = None  # deja utiliser

    return right_place_and_color, right_color_worng_place



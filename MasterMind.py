import random


chances = 10 #nombre maximale d'essais
colors = ['red', 'yellow', 'blue', 'green', 'purple', 'pink'] #les couleurs possibles

# print(random.sample(colors, 4)) #selectioner 4 couleurs aleatoire


def generate_secret_combo(colors):   #fonction qui genere la combinaison aleatoire
    secret = random.sample(colors, 4) #choise aleatoirement quatre couleur des couleurs predefini
    return secret



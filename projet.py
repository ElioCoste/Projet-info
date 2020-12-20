#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# COSTE Elio, COURTOIS Thibault, DENIEL Théo, NAIME Mathieu
# Tuesday, 15 December 2020
# Informatique - projet
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

"""Ce projet consiste en une implémentation simpliste d'un jeu d'échecs, avec \
seulement quelques fonctionnalités."""

import random


def convertit_coup(coup):
    """Convertit la notation algébrique en coordonnées utilisables."""
    coordonnees = ((), ())
    return coordonnees

def coup_valide(plateau, coup):
    """Retourne True si le coup demandé est valide, False sinon."""

    coup = convertit_coup(coup)

    # Vérifie que les cases sont bien sur l'échiquier
    if coup[0][0] < 0 or coup[0][1] > 7 or coup[0][0] < 0 or coup[0][1] > 7:
        return False
    if coup[1][0] < 0 or coup[1][1] > 7 or coup[1][0] < 0 or coup[1][1] > 7:
        return False

    # Vérifie que la case d'arrivée est atteignable par la pièce
    return coup[1] in DEPLACEMENTS[plateau[coup[0][0]][coup[0][1]]](plateau, coup[0])


def jouer_coup(plateau, coup):
    """Joue le coup demandé sur l'échiquier."""
    case_depart , case_arrivee = coup 
    ligne_depart, colonne_depart = case_depart
    ligne_arrivee, colonne_arrivee = case_arrivee
    plateau[ligne_arrivee][colonne_arrivee] = plateau[ligne_depart][colonne_depart]
    plateau[ligne_depart][colonne_depart] = '.'
    return plateau

def afficher_plateau(plateau, trait):
    """Affiche l'échiquier sous la perspective de la couleur qui a le trait."""
    # Si c'est aux Noirs de jouer, on renverse l'échiquier
    if trait:
        pass
    
    # Affichage de l'échiquier
    for i in plateau:
        for j in i:
            print(PIECES[j], end='')
        print()


## Fonctions pour les déplacements possibles des pièces. 

def pion(plateau, pos):
    """Renvoie la liste des déplacements possibles pour un pion."""
    return deplacements

def tour(plateau, pos):
    """Renvoie la liste des déplacements possibles pour une tour."""
    return deplacements

def cavalier(plateau, pos):
    """Renvoie la liste des déplacements possibles pour un cavalier."""
    return deplacements

def fou(plateau, pos):
    """Renvoie la liste des déplacements possibles pour un fou."""
    return deplacements

def roi(plateau, pos):
    """Renvoie la liste des déplacements possibles pour un roi."""
    return deplacements

def dame(plateau, pos):
    """Renvoie la liste des déplacements possibles pour une dame."""
    return fou(plateau, pos) + tour(plateau, pos)

# Dictionnaire de conversion caractères spéciaux
PIECES = {
    "k": '♔',
    "q": '♕',
    "r": '♖',
    "b": '♗',
    "n": '♘',
    "p": '♙',
    "K": '♚',
    "Q": '♛',
    "R": '♜',
    "B": '♝',
    "N": '♞',
    "P": '♟'
}

DEPLACEMENTS = {
    'p': pion,
    "k": roi, 
    "q": dame, 
    "r": tour, 
    "b": fou, 
    "n": cavalier
}


def demo():
    input("Appuyez sur ENTREE pour commencer une nouvelle partie.")

    # Position de départ.
    plateau = [
        ['R', 'N', 'B', 'Q', 'K', 'B', 'K', 'R'], 
        ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'], 
        ['.', '.', '.', '.', '.', '.', '.', '.'], 
        ['.', '.', '.', '.', '.', '.', '.', '.'], 
        ['.', '.', '.', '.', '.', '.', '.', '.'], 
        ['.', '.', '.', '.', '.', '.', '.', '.'], 
        ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'], 
        ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']
    ]

    trait = 0
    running = True
    while running:
        trait = 0 if trait == 1 else 1
        couleur = "Noirs" if trait else "Blancs"

        coup = ((0, 0), (0, 0))
        while not coup_valide(plateau, coup):
            coup = convertit_coup(input("Trait aux {}".format(couleur)))

        plateau = jouer_coup(plateau, coup)

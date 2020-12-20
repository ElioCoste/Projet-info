#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# COSTE Elio, COURTOIS Thibault, DENIEL Théo, NAIME Mathieu
# Tuesday, 15 December 2020
# Informatique - projet
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

"""Ce projet consiste en une implémentation simpliste d'un jeu d'échecs, avec \
seulement quelques fonctionnalités."""

import re
import random

def convertit_coup(coup):
    """Convertit la notation algébrique en coordonnées utilisables."""
    a, b, c, d = coup

    b, d = int(b), int(d)
    b, d = 8 - b, 8 - d

    a, c = a.lower(), c.lower()
    a, c = ord(a) - 97, ord(c) - 97
    return ((b, a), (d, c))

def coup_valide(plateau, coup):
    """Retourne True si le coup demandé est valide, False sinon."""
    # Vérifie que la case de départ est différente de la case d'arrivée
    if coup[0] == coup[1]:
        return False

    # Vérifie que le coup proposé respecte le format convenu
    pattern = re.compile("[a-h][1-8][a-h][1-8]")
    if re.fullmatch(coup.lower(), pattern) is None:
        return False

    # On peut donc convertir sans souci
    coup = convertit_coup(coup)

    # Vérifie que la case d'arrivée est atteignable par la pièce
    return coup[1] in DEPLACEMENTS[plateau[coup[0][0]][coup[0][1]]](plateau, coup[0])


def jouer_coup(plateau, coup):
    """Joue le coup demandé sur l'échiquier."""
    (ligne_depart, colonne_depart), (ligne_arrivee, colonne_arrivee) = coup
    plateau[ligne_arrivee][colonne_arrivee] = plateau[ligne_depart][colonne_depart]
    plateau[ligne_depart][colonne_depart] = '.'
    return plateau

def afficher_plateau(plateau, trait):
    """Affiche l'échiquier sous la perspective de la couleur qui a le trait."""
    # Si c'est aux Noirs de jouer, on renverse l'échiquier
    if trait:
        plateau = [i[::-1] for i in plateau][::-1]
    
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
    deplacements = []
    ligne, colonne = pos
    liste_colonne = [0, 1, 2, 3, 4, 5, 6, 7]
    liste_ligne = [0, 1, 2, 3, 4, 5, 6, 7]
    for i in range(len(liste_ligne)):
        for j in range(len(liste_colonne)):
            if liste_ligne[i] == ligne:
                deplacements += [(ligne, j)]
    for j in range(len(liste_colonne)):
        for i in range(len(liste_ligne)):
            if liste_colonne[j] == colonne:
                deplacements += [(i, colonne)]
    return deplacements

def cavalier(plateau, pos):
    """Renvoie la liste des déplacements possibles pour un cavalier."""
    a, b = pos
    deplacements =[(a + 2, b + 1), (a + 2, b - 1), (a - 2, b + 1), (a - 2, b - 1), (a + 1, b + 2), (a - 1, b + 2), (a + 1, b - 2), (a - 1,  b - 2)]
    return deplacements

def fou(plateau, pos):
    """Renvoie la liste des déplacements possibles pour un fou."""
    a, b = pos
    deplacements = [(a + 1, b + 1), (a + 2, b + 2), (a + 3, b + 3), (a + 4, b + 4), (a + 5, b + 5), (a + 6, b + 6), (a + 7, b + 7)]
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

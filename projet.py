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
    a, b, c, d = coup

    b, d = int(b), int(d)
    b, d = 8 - b, 8 - d

    a, c = ord(a) - 97, ord(c) - 97
    return ((b, a), (d, c))

def coup_valide(plateau, coup, trait):
    """Retourne True si le coup demandé est valide, False sinon.
    Incomplet."""
    # Vérifie que le coup proposé respecte le format convenu
    if len(coup) != 4:
        return False
    if not (coup[1].isdigit() and coup[3].isdigit() and coup[0].islower() and coup[2].islower()):
        return False

    if not (0 < int(coup[1]) <= 8 and 0 < int(coup[3]) <= 8):
        return False

    # On peut donc convertir sans souci
    coup = convertit_coup(coup)
    piece = plateau[coup[0][0]][coup[0][1]]

    # Vérifie que la case indiquée comporte bien une pièce de la bonne couleur
    if piece.isupper() != trait or piece == ".":
        return False

    # Vérifie que la case de départ est différente de la case d'arrivée
    if coup[0] == coup[1]:
        return False

    # Vérifie que la case d'arrivée ne soit pas une pièce de même couleur que la pièce qui bouge
    if (piece.isupper() and plateau[coup[1][0]][coup[1][1]].isupper()) or \
    (piece.islower() and plateau[coup[1][0]][coup[1][1]].islower()):
        return False

    # Vérifie que la case d'arrivée est atteignable par la pièce
    return coup[1] in DEPLACEMENTS[piece.lower()](plateau, coup[0])
    
    # Vérifie que le roi c'est pas en échec
    #return not echec(jouer_coup(plateau, coup), trait)

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
            print(PIECES[j], end=' ')
        print()
    print('-'*16)

def echec(plateau, trait):
    """Renvoie True si le roi qui a le trait est en échec, False sinon.
    Non implémenté."""
    return False


## Fonctions pour les déplacements possibles des pièces. 

def pion(plateau, pos):
    """Donne la liste des coups valides pour un pion donné.
    Complet sauf prise en passant."""
    deplacements = []
    ligne, colonne = pos
    piece = plateau[ligne][colonne]

    # Cas d'un pion noir
    if piece.isupper():
        if plateau[ligne+1][colonne] == ".":
            deplacements.append((ligne+1, colonne))
            # Si on est sur la ligne 1, on peut avancer de deux
            if ligne == 1 and plateau[ligne+2][colonne] == '.':
                deplacements.append((ligne+2, colonne))
        
        # Prise si il y a une pièce adverse
        prise_droite, prise_gauche = True, True
        if colonne == 0:
            prise_gauche = False
        elif colonne == 7:
            prise_droite = False
        
        if prise_droite and plateau[ligne+1][colonne+1].islower():
            deplacements.append((ligne+1, colonne+1))
        if prise_gauche and plateau[ligne+1][colonne-1].islower():
            deplacements.append((ligne+1, colonne-1))

    # Cas d'un pion blanc
    else:
        if plateau[ligne-1][colonne] == ".":
            deplacements.append((ligne-1, colonne))
            # Si on est sur la ligne 6, on peut avancer de deux
            if ligne == 6 and plateau[ligne-2][colonne] == '.':
                deplacements.append((ligne-2, colonne))
        
        # Prise si il y a une pièce adverse
        prise_droite, prise_gauche = True, True
        if colonne == 0:
            prise_gauche = False
        elif colonne == 7:
            prise_droite = False
        
        if prise_droite and plateau[ligne-1][colonne+1].isupper():
            deplacements.append((ligne-1, colonne+1))
        if prise_gauche and plateau[ligne-1][colonne-1].isupper():
            deplacements.append((ligne-1, colonne-1))

    return deplacements

def tour(plateau, pos):
    """Renvoie la liste des déplacements possibles pour une tour.
    Incomplet"""
    deplacements = []
    ligne, colonne = pos

    # Cas tour blanche
    if plateau[ligne][colonne].islower():

        # Cases sur la même colone que la tour
        i = ligne - 1
        while i >= 0 and plateau[i][colonne] == '.':
            deplacements.append((i, colonne))
            i -= 1
        if i >= 0 and plateau[i][colonne].isupper():
            deplacements.append((i, colonne))
        i = ligne + 1
        while i <= 7 and plateau[i][colonne] == '.':
            deplacements.append((i, colonne))
            i += 1
        if i <= 7 and plateau[i][colonne].isupper():
            deplacements.append((i, colonne))

        # Cases sur la même ligne que la tour
        i = colonne - 1
        while i >= 0 and plateau[ligne][i] == '.':
            deplacements.append((ligne, i))
            i -= 1
        if i >= 0 and plateau[ligne][i].isupper:
            deplacements.append((ligne, i))
        i = colonne + 1
        while i <= 7 and plateau[ligne][i] == '.':
            deplacements.append((ligne, i))
            i += 1
        if i <= 7 and plateau[ligne][i].isupper:
            deplacements.append((ligne, i))
    # Cas tour noire
    else:

        # Cases sur la même colone que la tour
        i = ligne - 1
        while i >= 0 and plateau[i][colonne] == '.':
            deplacements.append((i, colonne))
            i -= 1
        if i >= 0 and plateau[i][colonne].islower():
            deplacements.append((i, colonne))
        i = ligne + 1
        while i <= 7 and plateau[i][colonne] == '.':
            deplacements.append((i, colonne))
            i += 1
        if i <= 7 and plateau[i][colonne].islower():
            deplacements.append((i, colonne))

        # Cases sur la même ligne que la tour
        i = colonne - 1
        while i >= 0 and plateau[ligne][i] == '.':
            deplacements.append((ligne, i))
            i -= 1
        if i >= 0 and plateau[ligne][i].islower:
            deplacements.append((ligne, i))
        i = colonne + 1
        while i <= 7 and plateau[ligne][i] == '.':
            deplacements.append((ligne, i))
            i += 1
        if i <= 7 and plateau[ligne][i].islower:
            deplacements.append((ligne, i))

    return deplacements

def cavalier(plateau, pos):
    """Renvoie la liste des déplacements possibles pour un cavalier.
    Complet."""
    a, b = pos
    deplacements = []
    liste = [
        (a + 2, b + 1),
        (a + 2, b - 1),
        (a - 2, b + 1),
        (a - 2, b - 1),
        (a + 1, b + 2),
        (a - 1, b + 2),
        (a + 1, b - 2),
        (a - 1,  b - 2)
    ]
    for i, j in liste:
        # Vérifie que la case est sur l'échiquier
        if 0 <= i <= 7 and 0 <= j <= 7:
            deplacements.append((i, j))
    return deplacements

def fou(plateau, pos):
    """Renvoie la liste des déplacements possibles pour un fou.
    Non implémenté."""
    deplacements = []
    a, b = pos
    liste = [
        (a + 1, b + 1),
        (a + 2, b + 2),
        (a + 3, b + 3),
        (a + 4, b + 4),
        (a + 5, b + 5),
        (a + 6, b + 6),
        (a + 7, b + 7),
        (a - 1, b - 1),
        (a - 2, b - 2),
        (a - 3, b - 3),
        (a - 4, b - 4),
        (a - 5, b - 5),
        (a - 6, b - 6),
        (a - 7, b - 7),
        (a - 1, b + 1),
        (a - 2, b + 2),
        (a - 3, b + 3),
        (a - 4, b + 4),
        (a - 5, b + 5),
        (a - 6, b + 6),
        (a - 7, b + 7),
        (a + 1, b - 1),
        (a + 2, b - 2),
        (a + 3, b - 3),
        (a + 4, b - 4),
        (a + 5, b - 5),
        (a + 6, b - 6),
        (a + 7, b - 7)
    ]
    for i, j in liste:
        # Vérifie que la case d'arrivée est bien sur l'échiquier
        if 0 <= i <= 7 and 0 <= j <= 7:
            deplacements.append((i, j))
    return deplacements

def roi(plateau, pos):
    """Renvoie la liste des déplacements possibles pour un roi.
    Complet."""
    a, b = pos
    deplacements = []

    # Liste des déplacements possibles de manière générale
    liste = [
        (a + 1, b),
        (a - 1, b),
        (a, b + 1),
        (a, b - 1),
        (a + 1, b + 1),
        (a + 1, b - 1),
        (a - 1, b - 1),
        (a - 1 , b + 1)
    ]
    for i, j in liste:
        # Vérifie que la case d'arrivée est bien sur l'échiquier et que la 
        # case d'arrivée ne contient pas une pièce de même couleur que le roi
        if 0 <= i <= 7 and 0 <= j <= 7 and \
            not (plateau[i][j].islower() and plateau[a][b].islower()) and \
            not (plateau[i][j].isupper() and plateau[a][b].isupper()):
            deplacements.append((i, j))
    return deplacements

def dame(plateau, pos):
    """Renvoie la liste des déplacements possibles pour une dame.
    Dépend des fonctions fou et tour, i.e incomplet."""
    return fou(plateau, pos) + tour(plateau, pos)

# Dictionnaire de conversion caractères d'affichage
PIECES = {
    "K": '♔',
    "Q": '♕',
    "R": '♖',
    "B": '♗',
    "N": '♘',
    "P": '♙',
    "k": '♚',
    "q": '♛',
    "r": '♜',
    "b": '♝',
    "n": '♞',
    "p": '♟',
    ".": " "
}

# Fonctions donnant les déplacements associés aux pièces
DEPLACEMENTS = {
    'p': pion,
    "k": roi, 
    "q": dame, 
    "r": tour, 
    "b": fou, 
    "n": cavalier
}


def demo():
    """Fonction principale pour lancer le jeu."""
    input("Appuyez sur ENTREE pour commencer une nouvelle partie.")

    # pos de départ.
    plateau = [
        ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
        ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
        ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']
    ]

    trait = 1
    running = True
    while running:
        trait = 0 if trait == 1 else 1
        couleur = "Noirs" if trait else "Blancs"

        coup = ""
        afficher_plateau(plateau, trait)
        while not coup_valide(plateau[:], coup, trait):
            coup = input("Trait aux {}. Entrez votre coup : ".format(couleur)).lower()

        print(coup)
        coup = convertit_coup(coup)

        # Promotion
        piece_promue = None
        if (plateau[coup[0][0]][coup[0][1]] == 'p' and coup[1][0] == 0) \
            or (plateau[coup[0][0]][coup[0][1]] == 'P' and coup[1][0] == 7):
            while piece_promue not in ('r', 'n', 'b', 'q'):
                piece_promue = input("En quelle pièce voulez-vous promouvoir votre pion ? : ").lower()

        plateau = jouer_coup(plateau[::], coup)

        if piece_promue is not None:
            print('Promotion')
            if trait:
                plateau[coup[1][0]][coup[1][1]] = piece_promue.upper()
            else:
                plateau[coup[1][0]][coup[1][1]] = piece_promue.lower()

        afficher_plateau(plateau, trait)

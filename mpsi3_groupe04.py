#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# COSTE Elio, COURTOIS Thibault, DENIEL Théo, NAIME Mathieu
# Tuesday, 15 December 2020
# Informatique - projet
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

"""Ce projet consiste en une implémentation simpliste d'un jeu d'échecs, \
avec roque, prise en passant et échec non implémentés."""

def convertit_coup(coup):
    """Convertit la notation algébrique en coordonnées utilisables."""
    lig1, col1, lig2, col2 = coup

    col1, col2 = int(col1), int(col2)
    col1, col2 = 8 - col1, 8 - col2

    lig1, lig2 = ord(lig1) - 97, ord(lig2) - 97
    return ((col1, lig1), (col2, lig2))

def coup_valide(plateau, coup, trait):
    """
    Retourne True si le coup demandé est valide, False sinon.
    Incomplet (prise en passant et roque non implémentés).
    """

    # Cas du roque
    if coup == "o-o":
        return petit_roque(plateau, trait)
    if coup == "o-o-o":
        return grand_roque(plateau, trait)

    # Vérifie que le coup proposé respecte le format convenu
    if len(coup) != 4:
        return False
    if not (coup[1].isdigit() and coup[3].isdigit() and \
        coup[0].islower() and coup[2].islower()):
        return False

    if not (0 < int(coup[1]) <= 8 and 0 < int(coup[3]) <= 8) or \
        not (0 <= ord(coup[0]) - 97 < 8 and 0 <= ord(coup[2]) - 97 < 8):
        return False

    # On peut donc convertir sans souci
    coup = convertit_coup(coup)
    piece = plateau[coup[0][0]][coup[0][1]]

    # Vérifie que la case indiquée comporte bien une pièce de la bonne couleur
    # et que la case de départ est différente de la case d'arrivée
    if piece.isupper() != trait or piece == "." or coup[0] == coup[1]:
        return False

    # Vérifie que la case d'arrivée ne soit pas une pièce de même couleur
    # que la pièce qui bouge
    if meme_couleur(piece, plateau[coup[1][0]][coup[1][1]]):
        return False

    # Vérifie que la case d'arrivée est atteignable par la pièce
    return coup[1] in DEPLACEMENTS[piece.lower()](plateau, coup[0])

    # Vérifie que le roi c'est pas en échec (non implémenté)
    # return not echec(jouer_coup(plateau, coup), trait)

def jouer_coup(plateau, coup):
    """Joue le coup demandé sur l'échiquier."""
    (ligne_depart, colonne_depart), (ligne_arrivee, colonne_arrivee) = coup
    plateau[ligne_arrivee][colonne_arrivee] = \
        plateau[ligne_depart][colonne_depart]
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

def meme_couleur(piece1, piece2):
    """Renvoie True si les deux pièces sont de la même couleur, False sinon."""
    return (piece1.isupper() and piece2.isupper()) or \
        (piece1.islower() and piece2.islower())

def echec(plateau, trait):
    """
    Renvoie True si le roi qui a le trait est en échec, False sinon.
    Non implémenté.
    """
    raise NotImplementedError(plateau, trait)


## Fonctions pour les déplacements possibles des pièces.

def pion(plateau, pos):
    """
    Donne la liste des coups valides pour un pion donné.
    Complet sauf prise en passant.
    """
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
        
        # Si prise en passant possible
        if prise_en_passant is not None and \
            abs(colonne - prise_en_passant[1]) == 1:
            deplacements.append((prise_en_passant[0]+1, prise_en_passant[1]))

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

        if prise_en_passant is not None and \
            abs(colonne - prise_en_passant[1]) == 1:
            deplacements.append((prise_en_passant[0]-1, prise_en_passant[1]))

    return deplacements

def tour(plateau, pos):
    """Renvoie la liste des déplacements possibles pour une tour."""
    deplacements = []
    ligne, colonne = pos
    piece = plateau[ligne][colonne]
    # Cases sur la même colonne que la tour
    i = ligne - 1
    while i >= 0 and plateau[i][colonne] == '.':
        deplacements.append((i, colonne))
        i -= 1
    if i >= 0 and not meme_couleur(plateau[i][colonne], piece):
        deplacements.append((i, colonne))
    i = ligne + 1
    while i <= 7 and plateau[i][colonne] == '.':
        deplacements.append((i, colonne))
        i += 1
    if i <= 7 and not meme_couleur(plateau[i][colonne], piece):
        deplacements.append((i, colonne))

    # Cases sur la même ligne que la tour
    i = colonne - 1
    while i >= 0 and plateau[ligne][i] == '.':
        deplacements.append((ligne, i))
        i -= 1
    if i >= 0 and not meme_couleur(plateau[i][colonne], piece):
        deplacements.append((ligne, i))
    i = colonne + 1
    while i <= 7 and plateau[ligne][i] == '.':
        deplacements.append((ligne, i))
        i += 1
    if i <= 7 and not meme_couleur(plateau[i][colonne], piece):
        deplacements.append((ligne, i))

    return deplacements

def cavalier(plateau, pos):
    """Renvoie la liste des déplacements possibles pour un cavalier."""
    lig, col = pos
    deplacements = []
    liste = [
        (lig + 2, col + 1),
        (lig + 2, col - 1),
        (lig - 2, col + 1),
        (lig - 2, col - 1),
        (lig + 1, col + 2),
        (lig - 1, col + 2),
        (lig + 1, col - 2),
        (lig - 1,  col - 2)
    ]
    for i, j in liste:
        # Vérifie que la case est sur l'échiquier
        # et qu'elle ne contient pas une pièce aliée
        if 0 <= i <= 7 and 0 <= j <= 7 and \
            not meme_couleur(plateau[i][j], plateau[lig][col]):
            deplacements.append((i, j))
    return deplacements

def fou(plateau, pos):
    """Renvoie la liste des déplacements possibles pour un fou."""
    deplacements = []
    lig, col = pos
    piece = plateau[lig][col]

    #diago sud-ouest
    i = lig - 1
    j = col + 1
    while i >= 0 and j <= 7 and plateau[i][j] == '.':
        deplacements.append((i, j))
        i -= 1
        j += 1
    if i >= 0 and j <= 7 and not meme_couleur(plateau[i][j], piece):
        deplacements.append((i, j))

    #diago sud-est
    i = lig + 1
    j = col + 1
    while i <= 7 and j <= 7 and plateau[i][j] == '.':
        deplacements.append((i, j))
        i += 1
        j += 1
    if i <= 7 and j <= 7 and not meme_couleur(plateau[i][j], piece):
        deplacements.append((i, j))

    #diago nord-est
    i = lig + 1
    j = col - 1
    while i <= 7 and j >= 0 and plateau[i][j] == '.':
        deplacements.append((i, j))
        i += 1
        j -= 1
    if i <= 7 and j >= 0 and not meme_couleur(plateau[i][j], piece):
        deplacements.append((i, j))

    #diago nord-ouest
    i = lig - 1
    j = col - 1
    while i >= 0 and j >= 0 and plateau[i][j] == '.':
        deplacements.append((i, j))
        i -= 1
        j -= 1
    if i >= 0 and j >=0 and not meme_couleur(plateau[i][j], piece):
        deplacements.append((i, j))

    return deplacements

def roi(plateau, pos):
    """Renvoie la liste des déplacements possibles pour un roi."""
    lig, col = pos
    deplacements = []

    # Liste des déplacements possibles de manière générale
    liste = [
        (lig + 1, col),
        (lig - 1, col),
        (lig, col + 1),
        (lig, col - 1),
        (lig + 1, col + 1),
        (lig + 1, col - 1),
        (lig - 1, col - 1),
        (lig - 1 , col + 1)
    ]
    for i, j in liste:
        # Vérifie que la case d'arrivée est bien sur l'échiquier et que la
        # case d'arrivée ne contient pas une pièce de même couleur que le roi
        if 0 <= i <= 7 and 0 <= j <= 7 and \
            not meme_couleur(plateau[i][j], plateau[lig][col]):
            deplacements.append((i, j))
    return deplacements

def dame(plateau, pos):
    """
    Renvoie la liste des déplacements possibles pour une dame.
    """
    return fou(plateau, pos) + tour(plateau, pos)

def grand_roque(plateau, trait):
    """Vérifie que le grand roque est possible."""
    # Cas noir
    if trait:
        if not roque_noir[0]:
            return False
        if (plateau[0][1], plateau[0][2], plateau[0][3]) != ('.', '.', '.'):
            return False
        # Reste à vérifier que le roi ne se déplace pas sur une case 
        # où il est en échec...
        return True
    
    # Cas Blanc
    if not roque_noir[0]:
        return False
    if (plateau[7][1], plateau[7][2], plateau[7][3]) != ('.', '.', '.'):
        return False
    # Reste à vérifier que le roi ne se déplace pas sur une case 
    # où il est en échec...
    return True

def petit_roque(plateau, trait):
    """Vérifie que le petit roque est possible."""
    # Cas noir
    if trait:
        if not roque_noir[1]:
            return False
        if (plateau[0][6], plateau[0][5]) != ('.', '.'):
            return False
        # Reste à vérifier que le roi ne se déplace pas sur une case 
        # où il est en échec...
        return True
    
    # Cas Blanc
    if not roque_blanc[1]:
        return False
    if (plateau[7][6], plateau[7][5]) != ('.', '.'):
        return False
    # Reste à vérifier que le roi ne se déplace pas sur une case 
    # où il est en échec...
    return True

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

# Dictionnaire de conversion inversant les caractères associés aux pièces
# noires et blanches, suivant si l'on joue sur fond noir ou blanc
# pour une meilleure visibilité.
"""
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
    "P": '♟',
    ".": " "
}
"""

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

    global roque_blanc
    global roque_noir
    global prise_en_passant

    # Le roque est possible au départ. Le 1er élément correspond à la 
    # possibilité de faire grand roque et le second de faire petit roque
    roque_blanc, roque_noir = [True, True], [True, True]
    prise_en_passant = None

    trait = 1
    running = True
    while running:
        trait = 0 if trait else 1
        couleur = "Noirs" if trait else "Blancs"

        coup = ""
        afficher_plateau(plateau, trait)
        while not coup_valide(plateau[:], coup, trait):
            coup = input(
                "Trait aux {}. Entrez votre coup : ".format(couleur)
                ).lower()
        
        if coup == "o-o":
            # Petit roque noir
            if trait:
                plateau[0][7], plateau[0][4] = '.', '.'
                plateau[0][6], plateau[0][5] = 'R', 'K'
                roque_noir = (False, False)
            # Petit roque blanc
            else:
                plateau[7][7], plateau[7][4] = '.', '.'
                plateau[7][6], plateau[7][5] = 'r', 'k'
                roque_blanc = (False, False)
            
        elif coup == "o-o-o":
            # Grand roque noir
            if trait:
                plateau[0][0], plateau[0][4] = '.', '.'
                plateau[0][3], plateau[0][2] = 'R', 'K'
                roque_noir = (False, False)
            # Grand roque blanc
            else:
                plateau[7][0], plateau[7][4] = '.', '.'
                plateau[7][3], plateau[7][2] = 'r', 'k'
                roque_blanc = (False, False)
        else:
            coup = convertit_coup(coup)
            plateau = jouer_coup(plateau[::], coup)

            # Promotion
            piece_promue = None
            if (plateau[coup[0][0]][coup[0][1]] == 'p' and coup[1][0] == 0) \
                or (plateau[coup[0][0]][coup[0][1]] == 'P' and coup[1][0] == 7):
                while piece_promue not in ('r', 'n', 'b', 'q'):
                    piece_promue = input(
                        "En quelle pièce voulez-vous promouvoir votre pion ? : "
                        ).lower()

            # Si le roi tour bouge, on interdit le roque des deux côtés
            if plateau[coup[0][0]][coup[0][1]] == "K":
                roque_noir = [False, False]
            if plateau[coup[0][0]][coup[0][1]] == "k":
                roque_blanc = [False, False]

            # Si une tour bouge, on interdit le roque du côté de la 
            # tour qui a bougé
            if plateau[coup[0][0]][coup[0][1]] == "r":
                if coup[0][1] == 0:
                    roque_blanc[0] = False
                if coup[0][1] == 7:
                    roque_blanc[1] = False
            if plateau[coup[0][0]][coup[0][1]] == "R":
                if coup[0][1] == 0:
                    roque_noir[0] = False
                if coup[0][1] == 7:
                    roque_noir[1] = False

            # Réinitialise la prise en passant une fois le coup effectué
            prise_en_passant = None 
            # Prise en passant
            if plateau[coup[1][0]][coup[1][1]].lower() == "p"\
                and abs(coup[1][0] - coup[0][0]) == 2:
                prise_en_passant = coup[1] # On peut le prendre en passant

            if piece_promue is not None:
                print('Promotion')
                if trait:
                    plateau[coup[1][0]][coup[1][1]] = piece_promue.upper()
                else:
                    plateau[coup[1][0]][coup[1][1]] = piece_promue.lower()

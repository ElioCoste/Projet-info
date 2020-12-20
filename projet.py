#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# COSTE Elio, COURTOIS Thibaut, DENIEL Théo, NAIME Mathieu
# Tuesday, 15 December 2020 
# Informatique - projet 
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

"""Ce projet consiste en une implémentation simpliste d'un jeu d'échecs, avec \
seulement quelques fonctionnalités."""

piece = {"k": '♔', "q": '♕', "r": '♖', "b": '♗', "k": '♘', "p": '♙', "K": '♚', "Q": '♛', "R": '♜', "B": '♝', "N": '♞', "P": '♟'}


import random

def convertit_coup(coup):
    """Convertit la notation algébrique en coordonnées utilisables."""
    coordonnees = ((), ())
    return coordonnees

def coup_valide(plateau, coup):
    """Retourne True si le coup demandé est valide, False sinon."""
    est_valide = True
    return est_valide

def jouer_coup(plateau, coup):
    """Joue le coup demandé sur l'échiquier."""
    return plateau

def afficher_plateau(plateau, trait):
    """Affiche l'échiquier sous la perspective de la couleur qui a le trait."""
    # Si c'est aux Noirs de jouer, on renverse l'échiquier
    if trait:
        pass
    
    # Affichage de l'échiquier
    for i in plateau:
        for j in i:
            print(j, end='')
        print()
    

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
        jouer_coup(plateau, coup)


if __name__ == "__main__":
    demo()

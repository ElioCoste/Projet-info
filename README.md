# Projet d'info - jeu d'échecs simpliste

# Comment jouer ?

## IA ?
Pour l'instant, on se limite à un jeu uniquement dirigé par l'utilisateur, tour par tour.

## Jouer un coup
On utilise la **notation algébrique complète** pour les coups. Il faut spécifier la case de départ ainsi que la case d'arrivée, (c'est plus simple à implémenter que la notation allégée). Par ex : e2e4 pour avancer le pion e de deux cases.

# Détails techniques

## Représentation du plateau
On utilise la **notation FEN** pour le plateau, c'est à dire les majuscules pour les pièces noires et les minuscules pour les pièces blanches.

Les lettres représentant chaque pièce sont :
* R : Tour (Rook)
* N : Cavalier (Knight)
* B : Fou (Bishop)
* Q : Dame (Queen)
* K : Roi (King)
* P : Pion (Pawn)

L'échiquier est représenté sous la perspective des blancs, il faut dont changer l'affichage à chaque tour.

## Modélisation des coups
Un coup en notation algébrique devra être converti en un couple de deux couples de coordonnées. Le premier couple représente la case de départ et le second la case d'arrivée.

Le format doit donc être de la forme : `((ligne_depart, colonne_depart), (ligne_arrivee, colonne_arrivee))`.

Par exemple : e2e4 donne `((6, 4), (4, 4))`



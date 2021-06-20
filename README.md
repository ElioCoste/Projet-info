# Projet d'info - jeu d'échecs simpliste

# Comment jouer ?

## IA ?
Pour l'instant, on se limite à un jeu uniquement dirigé par le joueur (ou les joueurs) : à chaque coup, le trait est donné à l'autre joueur.
Un mode contre l'ordinateur sera peut-être implémenté un jour (qui sait ?).

## Jouer un coup
Implémentation d'une interface graphique (soon™) pour povoir jouer à la souris.

# Détails techniques

## Représentation du plateau
On utilise une version modifiée de la **notation FEN** pour représenter les pièces, c'est à dire les majuscules pour les pièces noires et les minuscules pour les pièces blanches.

Les lettres représentant chaque pièce sont :
* R : Tour (Rook)
* N : Cavalier (Knight)
* B : Fou (Bishop)
* Q : Dame (Queen)
* K : Roi (King)
* P : Pion (Pawn)

Une matrice 8x8 représente l'échiquier sous la perspective des blancs . Il faut dont changer l'affichage à chaque tour.

## Modélisation des coups
Un coup en notation algébrique est converti en un couple de deux couples de coordonnées. Le premier couple représente la case de départ et le second la case d'arrivée.

Le format doit donc être de la forme : `((ligne_depart, colonne_depart), (ligne_arrivee, colonne_arrivee))`.

Par exemple : e2e4 donne `((6, 4), (4, 4))`

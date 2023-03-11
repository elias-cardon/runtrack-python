# Définition de la fonction afficher_tapis(n) qui prend un entier n en argument
def afficher_tapis(n):
    # Boucle pour gérer les lignes du tapis (de 0 à n inclus)
    for i in range(n+1):
        # Boucle pour gérer les colonnes du tapis (de 0 à n inclus)
        for j in range(n+1):
            # Si i est égal à j, alors on est sur la diagonale du tapis et on affiche un "X"
            if i == j:
                print("X", end="")
            # Sinon, on affiche un "-"
            else:
                print("-", end="")
        # Après avoir géré toutes les colonnes d'une ligne, on ajoute un saut de ligne
        print()

# Exemple d'utilisation : on appelle la fonction avec un argument de 10
afficher_tapis(10)


def afficher_tapis(n):
    """
    Affiche un tapis de n+1 lignes/n+1 colonnes traversé par une diagonale.
    La diagonale commence en haut à droite et se termine en bas à gauche.

    :param n: La taille du tapis.
    """
    # Parcours des lignes du tapis
    for i in range(n+1):
        # Parcours des colonnes du tapis
        for j in range(n+1):
            # Si la somme des coordonnées est égale à n, on est sur la diagonale
            if i + j == n:
                print("X", end="")
            else:
                # Sinon, on affiche un tiret "-"
                print("-", end="")
        # Saut de ligne pour passer à la ligne suivante
        print()

# Exemple avec une taille de 10
afficher_tapis(10)


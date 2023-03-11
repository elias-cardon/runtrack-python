def draw_rectangle(width, height):
    # Affiche la première ligne du rectangle
    print("+{}+".format("-" * (width - 2)))

    # Affiche les lignes intermédiaires du rectangle
    for i in range(height - 2):
        print("|{}|".format(" " * (width - 2)))

    # Affiche la dernière ligne du rectangle
    print("+{}+".format("-" * (width - 2)))


# Exemple d'utilisation avec width=10 et height=3
draw_rectangle(10, 3)
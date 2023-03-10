chaine = "abcdefghijklmnopqrstuvwxyz" * 10
longueur = len(chaine)
hauteur = int((longueur * 2) ** 0.5)

for i in range(hauteur):
    for j in range(i + 1):
        index = j + i * (i + 1) // 2
        if index < longueur:
            print(chaine[index], end=" ")
    print()
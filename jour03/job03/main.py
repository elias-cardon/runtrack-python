def afficher_nombres():
    for i in range(101):
        if i not in [26, 37, 88]: #on demande si i fonctionne, on affiche pas ces chiffres
            print(i)

afficher_nombres()
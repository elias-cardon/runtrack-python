L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]
sum_paires = 0  # initialiser la somme à zéro

# parcourir chaque élément de la liste
for i in L:
    if i % 2 == 0:  # si l'élément est pair
        sum_paires += i  # ajouter l'élément à la somme

print("La somme de toutes les valeurs paires de la liste est :", sum_paires)

L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

max_elem = L[0] # initialisation du maximum avec le premier élément de la liste
min_elem = L[0] # initialisation du minimum avec le premier élément de la liste

for elem in L:
    if elem > max_elem:
        max_elem = elem # mise à jour du maximum si l'élément courant est plus grand
    if elem < min_elem:
        min_elem = elem # mise à jour du minimum si l'élément courant est plus petit

print("Le maximum de la liste est :", max_elem)
print("Le minimum de la liste est :", min_elem)
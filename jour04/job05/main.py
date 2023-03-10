# Créer une liste d'au moins 5 entiers
L = [3, 8, 12, 6, 5]

# Afficher la valeur de L[1]
print("La valeur de L[1] est :", L[1])

# Fonction pour remplacer L[3] par la somme des cases voisines L[2] & L[4]
def remplacer(L):
    L[3] = L[2] + L[4]

# Appeler la fonction pour remplacer L[3]
remplacer(L)

# Afficher la valeur du dernier terme de la liste
print("La valeur du dernier terme de la liste est :", L[-1])

def ajouter_melon():
    fruits = ["pomme", "cerise", "orange"]
    fruits.append("Melon") #append ajoute Melon à la fin de la liste
    return fruits
nouvelle_liste = ajouter_melon()
print(nouvelle_liste)
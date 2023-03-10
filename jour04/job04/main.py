def ajouter_mangue(fruits):
    fruits.insert(2, "Mangue")
    return fruits

fruits = ["pomme", "cerise", "orange", "Melon"]
nouvelle_liste = ajouter_mangue(fruits)
print(nouvelle_liste)

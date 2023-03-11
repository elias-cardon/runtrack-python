def arrondir_notes(notes):
    notes_arrondies = []  # On initialise la liste qui contiendra les notes arrondies
    for note in notes:  # On parcourt chaque note de la liste d'entrée
        if note < 40:  # Si la note est inférieure à 40, on l'ajoute sans modification
            notes_arrondies.append(note)
        else:  # Sinon, on doit arrondir la note à un multiple de 5 supérieur
            multiple_de_5_superieur = ((note + 2) // 5) * 5  # On calcule le prochain multiple de 5 supérieur
            if multiple_de_5_superieur - note < 3:  # Si la différence est inférieure à 3, on arrondit la note
                notes_arrondies.append(multiple_de_5_superieur)
            else:  # Sinon, on ajoute la note sans modification
                notes_arrondies.append(note)
    return notes_arrondies  # On retourne la liste des notes arrondies

notes = [76, 89, 62, 55, 41, 38, 91, 83, 78, 59]
notes_arrondies = arrondir_notes(notes)
print("Notes initiales : ", notes)
print("Notes arrondies : ", notes_arrondies)

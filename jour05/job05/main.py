def distance_toilettes(marches, hauteur):
    # Calcul de la distance parcourue en mètres pour un aller-retour aux toilettes
    distance_aller_retour = marches * hauteur * 2 / 100  # On divise par 100 pour convertir en mètres

    # Calcul de la distance parcourue en mètres par jour pour aller aux toilettes 5 fois par jour
    distance_par_jour = distance_aller_retour * 5

    # Calcul de la distance parcourue en mètres par semaine pour aller aux toilettes 5 fois par jour pendant 7 jours
    distance_par_semaine = distance_par_jour * 7

    # Formatage de la chaîne de caractères pour afficher le résultat
    result = f"Pour {marches} marches de {hauteur} cm, le gardien parcours {distance_par_semaine:.2f} m par semaine."

    return result

marches = 50
hauteur = 20

# Appel de la fonction distance_toilettes()
resultat = distance_toilettes(marches, hauteur)

# Affichage du résultat dans le terminal
print(resultat)
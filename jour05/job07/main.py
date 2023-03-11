while True:
    # Demander à l'utilisateur de saisir un mot
    mot = input("Veuillez saisir un mot sans espace ni caractère spécial : ")

    # Vérifier si le mot ne contient que des lettres de l'alphabet
    if not mot.isalpha():
        print("Le mot doit contenir uniquement des lettres de l'alphabet (sans accent ni majuscule) !")
        continue

    # Convertir le mot en une liste de lettres pour faciliter la manipulation
    lettres = list(mot)

    # Trouver la première paire de lettres qui ne sont pas dans l'ordre alphabétique
    for i in range(len(lettres) - 1):
        if lettres[i] < lettres[i + 1]:
            # Inverser ces deux lettres pour obtenir un nouveau mot plus grand
            lettres[i], lettres[i + 1] = lettres[i + 1], lettres[i]

            # Triez les lettres suivantes dans l'ordre croissant pour minimiser la distance entre les mots
            lettres[i + 1:] = sorted(lettres[i + 1:])

            # Convertir la liste de lettres en un mot et l'afficher
            nouveau_mot = "".join(lettres)
            print("Le nouveau mot est :", nouveau_mot)
            break
    else:
        # Si le mot est déjà le plus grand possible, afficher un message d'erreur
        print("Le mot est déjà le plus grand possible dans l'ordre alphabétique !")

    # Demander à l'utilisateur s'il souhaite continuer ou quitter
    reponse = input("Voulez-vous saisir un nouveau mot ? (O/N) : ")
    if reponse.lower() != "o":
        break

def chiffrement_cesar(message, decalage):
    """
    Chiffre un message en décalant chaque lettre dans l'alphabet.
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyz'  # l'alphabet utilisé pour le chiffrement
    message_chiffre = ''  # le message chiffré résultant
    for lettre in message:
        if lettre.lower() in alphabet:  # vérifie si la lettre est dans l'alphabet
            index = alphabet.index(lettre.lower())  # trouve l'index de la lettre dans l'alphabet
            index_decale = (index + decalage) % 26  # décale l'index de la lettre en utilisant le décalage donné, en prenant en compte le dépassement
            lettre_chiffree = alphabet[index_decale]  # trouve la lettre correspondant à l'index décalé
            if lettre.isupper():  # si la lettre originale était en majuscule, la lettre chiffrée doit l'être également
                lettre_chiffree = lettre_chiffree.upper()
            message_chiffre += lettre_chiffree  # ajoute la lettre chiffrée au message chiffré résultant
        else:
            message_chiffre += lettre  # si la lettre n'est pas dans l'alphabet, elle est laissée inchangée
    return message_chiffre  # renvoie le message chiffré résultant

message = "La Plateforme est cool"
decalage = 3
message_chiffre = chiffrement_cesar(message, decalage)
print("Message d'origine :", message)
print("Décalage :", decalage)
print("Message chiffré :", message_chiffre)
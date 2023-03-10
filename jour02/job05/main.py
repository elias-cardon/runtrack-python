def calcule(num1, operator, num2):
    # Vérifie si l'opérateur est valide
    if operator not in ['+', '-', '*', '/', '%']:
        # Si l'opérateur est invalide, lève une exception avec un message d'erreur
        raise ValueError("Opérateur invalide")
    # Effectue l'opération en fonction de l'opérateur donné en paramètre
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            raise ValueError("Division par zéro impossible")
        else:
            return num1 / num2
    elif operator == '%':
        return num1 % num2

# Exemple d'utilisation de la fonction avec un opérateur invalide
resultat = calcule(10, '+', 5)
print("Le résultat est :", resultat)

# Exemple d'utilisation de la fonction avec un opérateur invalide
try:
    # Essaie de multiplier 10 par 5
    resultat = calcule(10, 'x', 5)
    # Affiche le résultat de la division
    print("Le résultat est :", resultat)
except ValueError as error: # Ce n'est pas le bon opérateur pour le code donc on arrête le calcule et on affiche l'erreur.
    print("Erreur :", error)
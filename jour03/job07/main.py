chaine = "nikana"
inverse = "" #va stocker la chaine inversée

for i in range(len(chaine)-1, -1, -1):
    inverse += chaine[i]

print(inverse)
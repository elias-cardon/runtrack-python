L = [8, 24, 48, 2, 16]

count = 0
for num in L:
    if num % 3 == 0:
        count += 1

print("Il y a", count, "multiples de 3 dans la liste")

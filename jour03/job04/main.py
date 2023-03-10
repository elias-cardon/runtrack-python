for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# Le signe % est appelé "opérateur modulo" en Python. Il est utilisé pour trouver le reste de la division entière de deux nombres.
# Par exemple, l'expression 7 % 3 donne le reste de la division entière de 7 par 3, qui est 1.
# De même, l'expression 10 % 2 donne le reste de la division entière de 10 par 2, qui est 0.

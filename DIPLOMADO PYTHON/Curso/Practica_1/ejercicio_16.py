# Imprimir los números primos del 1 al 50

for numero in range(2, 51):
    if all(numero % divisor != 0 for divisor in range(2, int(numero ** 0.5) + 1)):
        print(numero)

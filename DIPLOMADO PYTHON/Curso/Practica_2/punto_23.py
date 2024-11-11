# Imprimir los números perfectos del 1 al 1000 utilizando un bucle "for"

for num in range(1, 1001):
    suma_divisores = 0
    for i in range(1, num):
        if num % i == 0:
            suma_divisores += i
    if num == suma_divisores:
        print(num)

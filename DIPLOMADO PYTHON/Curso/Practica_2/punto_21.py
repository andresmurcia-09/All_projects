# Imprimir los números primos del 1 al 100 utilizando un bucle `for`

for num in range(2, 101):
    es_primo = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            es_primo = False

    if es_primo:
        print(num)

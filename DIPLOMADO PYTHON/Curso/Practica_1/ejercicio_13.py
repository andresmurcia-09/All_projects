# calcular el promedio de una lista de números

numeros = [10, 20, 30, 40, 50]
suma = 0
cantidad = 0

for num in numeros:
    suma += num
    cantidad += 1

print(suma / cantidad)

# Contar cuántas veces aparece un elemento en una lista

lista = [1, 2, 3, 2, 4, 2, 5, 2]
elemento = 2
contador = 0

for num in lista:
    if num == elemento:
        contador += 1

print(f"El elemento {elemento} aparece {contador} veces en la lista.")

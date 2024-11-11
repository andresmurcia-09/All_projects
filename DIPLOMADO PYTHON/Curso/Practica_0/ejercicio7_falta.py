palabra = input("Ingrese una palabra: ")
palabra = palabra.lower().replace(" ", "")  # Convertir la palabra a minúsculas y eliminar espacios

es_palindromo = True
for i in range(len(palabra) // 2):
    if palabra[i] != palabra[-i - 1]:
        es_palindromo = False
        break

if es_palindromo:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")

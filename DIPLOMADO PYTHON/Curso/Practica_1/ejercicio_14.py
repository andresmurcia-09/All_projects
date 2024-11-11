# Imprimir las letras de una palabra separadas por guiones

palabra = str(input("Ingrese la palabra: "))
almacenar_palabra = ""

for letra in palabra:
    almacenar_palabra += letra + "-"

guion = almacenar_palabra[:-1]
print(guion)

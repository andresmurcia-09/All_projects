# contar cuantas vocales hay en una cadena de texto

texto = str(input("Ingrese el texto: "))
texto = texto.lower()
cantidad_vocales = 0

for caracter in texto:
    if caracter in "aeiouáéíóú":
        cantidad_vocales += 1

print(cantidad_vocales)

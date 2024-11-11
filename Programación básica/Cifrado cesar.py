# Función para cifrar un texto con el cifrado César
def cifrado_cesar(texto, desplazamiento):
    # Definir el alfabeto en mayúsculas para realizar las operaciones de cifrado
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # Inicializar la variable que contendrá el texto cifrado
    texto_cifrado = ""

    # Iterar sobre cada letra del texto original
    for letra in texto:
        # Verificar si la letra (en mayúsculas) está en el alfabeto
        if letra.upper() in alfabeto:
            # Obtener el índice de la letra en el alfabeto
            indice = alfabeto.index(letra.upper())

            # Calcular el nuevo índice aplicando el desplazamiento y aplicando el módulo con la longitud del alfabeto
            # para evitar índices fuera de rango
            nuevo_indice = (indice + desplazamiento) % len(alfabeto)

            # Obtener la letra correspondiente al nuevo índice en el alfabeto
            nueva_letra = alfabeto[nuevo_indice]

            # Verificar si la letra original era minúscula y, si es así, convertir la nueva letra a minúscula
            if letra.islower():
                texto_cifrado += nueva_letra.lower()
            else:
                texto_cifrado += nueva_letra
        else:
            # Si la letra no está en el alfabeto (por Ejemplo, un espacio o signo de puntuación), agregarla sin cambios
            texto_cifrado += letra
    # Devolver el texto cifrado
    return texto_cifrado


# Definir el texto original y el desplazamiento para cifrar
texto_original = "Hola Mundo!"
desplazamiento = 3

# Llamar a la función cifrado_cesar con el texto original y el desplazamiento para obtener el texto cifrado
texto_cifrado = cifrado_cesar(texto_original, desplazamiento)

# Imprimir el texto original y el texto cifrado
print("Texto original:", texto_original)
print("Texto cifrado:", texto_cifrado)

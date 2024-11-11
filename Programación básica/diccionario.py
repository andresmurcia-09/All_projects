# Definimos un diccionario para relacionar las teclas con las letras que contiene cada una
teclado = {
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"],
    "0": [" "],  # El espacio se asocia con la tecla 0
}


# Creamos la función frase_a_teclas que recibe una frase como argumento
def frase_a_teclas(frase):
    # Inicializamos una cadena vacía para almacenar las teclas presionadas
    teclas_presionadas = ""

    # Recorremos cada letra de la frase, convirtiéndola a minúsculas para facilitar la comparación
    for letra in frase.lower():
        # Recorremos el diccionario teclado para encontrar la tecla y las letras asociadas a esa tecla
        for tecla, letras in teclado.items():
            # Si la letra de la frase se encuentra en las letras asociadas a la tecla actual
            if letra in letras:
                # Obtenemos la cantidad de veces que se debe presionar la   tecla
                # Añadimos 1 porque las listas tienen indexación desde 0
                presiones = letras.index(letra) + 1
                # Añadimos la tecla multiplicada por la cantidad de presiones necesarias
                # a la cadena de teclas_presionadas
                teclas_presionadas += tecla * presiones
                break  # Salimos del bucle de teclado.items() para pasar a la siguiente letra de la frase

    # Devolvemos la cadena de teclas_presionadas como resultado
    return teclas_presionadas


# Solicitamos al usuario que ingrese una frase
frase = input("Ingresa la frase que deseas convertir: ")
# Llamamos a la función frase_a_teclas y guardamos el resultado en la variable resultado
resultado = frase_a_teclas(frase)
# Imprimimos el resultado para mostrar las teclas necesarias para escribir la frase
print("Las teclas necesarias para escribir la frase son:", resultado)

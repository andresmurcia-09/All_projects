"""Escriba un programa que le solicite una palabra al usuario y determine
si la palabra ingresada es un palíndromo. Palabra o frase es un palíndromo
si sus letras están dispuestas de tal manera que resulta la misma leída de
izquierda a derecha que de derecha a izquierda; por ejemplo, anilina.
"""


def es_palindromo(palabra):
    """
    Determina si una palabra o frase es un palíndromo.

    Args:
    palabra (str): La palabra o frase a verificar.

    Returns:
    bool: True si es un palíndromo, False en caso contrario.
    """

    # Convertir a minúsculas y eliminar espacios y caracteres no alfabéticos
    palabra_limpia = "".join([letra.lower() for letra in palabra if letra.isalnum()])

    # Comprobar si la palabra es igual a su reverso
    return palabra_limpia == palabra_limpia[::-1]


# Solicitar una palabra al usuario
palabra_ingresada = input("Ingrese una palabra o frase: ")

# Solicitar una palabra al usuario
if es_palindromo(palabra_ingresada):
    print(f"'{palabra_ingresada}' es un palíndromo.")
else:
    print(f"'{palabra_ingresada}' no es un palíndromo.")

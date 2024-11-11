"""Escriba un programa que lea una lista de palabras y encuentre los anagramas
existentes en la lista. Dos palabras son anagramas si contienen las mismas letras,
aunque estén en orden diferente. Ejemplo. 'roma' y 'mora'.
"""

from collections import defaultdict


def encontrar_anagramas(lista_palabras):
    """
    Encuentra todos los grupos de anagramas en una lista de palabras.

    Args:
    lista_palabras (list): Lista de palabras en las que se buscarán los anagramas.

    Returns:
    list: Lista de grupos de anagramas. Cada grupo es una lista de palabras.
    """

    # Diccionario que agrupa las palabras por sus letras ordenadas
    anagramas = defaultdict(list)

    for palabra in lista_palabras:
        # Ordena las letras de la palabra y úsalas como clave
        clave = "".join(sorted(palabra))
        anagramas[clave].append(palabra)

    # Filtrar solo los grupos con más de una palabra (es decir, que son anagramas)
    return [grupo for grupo in anagramas.values() if len(grupo) > 1]


lista_palabras = [
    "roma",
    "mora",
    "amor",
    "trama",
    "marta",
    "ramo",
    "omar",
    "ballena",
    "llenaba",
    "conejo",
    "encojo",
]
grupos_anagramas = encontrar_anagramas(lista_palabras)


for grupo in grupos_anagramas:
    print(grupo)

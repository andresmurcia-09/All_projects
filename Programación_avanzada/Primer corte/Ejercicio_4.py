"""Escriba un programa que determine la suma de los n primeros números
de la serie: 1, 1, 2, 3, 5, 8, 13, 21, .... en la cual cada término,
a partir del tercero, se obtiene sumando los dos términos anteriores.
"""


def suma_serie_fibonacci(n):
    """
    Calcula la suma de los primeros 'n' términos de la serie de Fibonacci.

    Args:
    n (int): El número de términos de la serie de Fibonacci que se desean sumar.

    Returns:
    int: La suma de los primeros 'n' términos de la serie.
    """

    # Si n es 0, la suma es 0
    if n == 0:
        """Si n es 1 o 2, la suma es simplemente 1, 
        ya que los dos primeros términos son 1"""
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2

    # Inicializar los dos primeros términos de la serie
    a, b = 1, 1
    suma = a + b

    # Calcular los siguientes términos y sumarlos
    for _ in range(3, n + 1):
        siguiente = a + b
        suma += siguiente
        a, b = b, siguiente

    return suma

# Solicitar al usuario el número de términos
n = int(
    input("Ingrese el número de términos de la serie de Fibonacci que desea sumar: ")
)

# Calcular y mostrar la suma de los primeros 'n' términos
resultado = suma_serie_fibonacci(n)
print(f"La suma de los primeros {n} términos de la serie de Fibonacci es: {resultado}")

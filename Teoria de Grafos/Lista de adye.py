# Definición de la matriz de adyacencia
matriz_adyacencia = [
    [0, 27.3, 0, 0, 0, 0, 0],
    [0, 0, 5.7, 0, 0, 0, 0],
    [0, 0, 0, 27.7, 0, 0, 0],
    [0, 0, 0, 0, 20.8, 0, 0],
    [0, 0, 0, 0, 0, 31.2, 0],
    [0, 0, 0, 0, 0, 0, 7.8],
    [15.3, 41.8, 0, 0, 0, 0, 0]
]

# Función para generar la lista de adyacencia a partir de la matriz de adyacencia
def generar_lista_adyacencia(matriz):
    lista_adyacencia = {}  # Diccionario para almacenar la lista de adyacencia

    # Iteración a través de las filas de la matriz
    for i, fila in enumerate(matriz):
        adyacentes = []  # Lista para almacenar los vértices adyacentes al vértice actual

        # Iteración a través de los valores de la fila
        for j, peso in enumerate(fila):
            if peso != 0:
                # Si el peso es distinto de cero, se agrega el vértice adyacente y su respectivo peso
                adyacentes.append((f"V{j}", peso))
        
        # Se agrega el vértice actual y su lista de adyacentes al diccionario de lista de adyacencia
        lista_adyacencia[f"V{i}"] = adyacentes
    
    return lista_adyacencia  # Retorna el diccionario con la lista de adyacencia generada

# Llamada a la función para generar la lista de adyacencia a partir de la matriz de adyacencia dada
lista_adyacencia = generar_lista_adyacencia(matriz_adyacencia)

# Impresión de la lista de adyacencia
print("Lista de Adyacencia:")
for vertice, adyacentes in lista_adyacencia.items():
    print(f"{vertice}: {adyacentes}")

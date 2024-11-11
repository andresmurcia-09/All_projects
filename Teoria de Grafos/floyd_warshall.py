# Importamos la biblioteca pandas para crear y manipular DataFrames
import pandas as pd


# Definimos la función floyd_warshall que toma como entrada una matriz de adyacencia que representa el grafo
def floyd_warshall(graph):
    # Obtenemos el número de vértices en el grafo calculando la longitud de la matriz de adyacencia
    n = len(graph)

    # Creamos una copia de la matriz de adyacencia. Esta matriz dist se actualizará para contener las distancias más cortas entre cada par de vértices
    dist = list(map(lambda i: list(map(lambda j: j, i)), graph))

    # Este es el inicio del bucle principal del algoritmo de Floyd-Warshall. Iteramos sobre todos los vértices del grafo
    for k in range(n):
        # Para cada vértice k, iteramos sobre todos los otros vértices i
        for i in range(n):
            # Para cada par de vértices i y k, iteramos sobre todos los otros vértices j
            for j in range(n):
                # Actualizamos la distancia entre los vértices i y j para ser la mínima entre la distancia actual y la distancia de i a k más la distancia de k a j
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    # Devolvemos la matriz de distancias más cortas
    return dist


# Prueba
graph = [
    [0, 5, float("inf"), 10],
    [float("inf"), 0, 3, float("inf")],
    [float("inf"), float("inf"), 0, 1],
    [float("inf"), float("inf"), float("inf"), 0],
]
# Llamamos a la función floyd_warshall con nuestro grafo y obtenemos la matriz de distancias más cortas
distances = floyd_warshall(graph)

# Convertimos la matriz de distancias a un DataFrame para una visualización más bonita
df = pd.DataFrame(distances)
# Imprimimos el DataFrame
print(df)

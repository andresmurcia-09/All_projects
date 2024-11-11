# Definición de la clase Grafo
class Grafo:
    # Constructor de la clase que inicializa el grafo con el número de vértices
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        # Crear una matriz de adyacencia con distancias inicializadas a infinito
        self.matriz_adyacencia = [[float('inf') for _ in range(num_vertices)] for _ in range(num_vertices)]

    # Método para agregar una arista con su respectivo peso al grafo
    def agregar_arista(self, inicio, fin, peso):
        self.matriz_adyacencia[inicio][fin] = peso

    # Método que implementa el algoritmo de Floyd-Warshall para encontrar las distancias mínimas
    def floyd_warshall(self):
        # Crear una matriz de distancias con distancias inicializadas a infinito
        distancias = [[float('inf') for _ in range(self.num_vertices)] for _ in range(self.num_vertices)]

        # Inicializar la matriz de distancias con las distancias conocidas
        for i in range(self.num_vertices):
            for j in range(self.num_vertices):
                distancias[i][j] = self.matriz_adyacencia[i][j]

        # Aplicar el algoritmo de Floyd-Warshall
        for k in range(self.num_vertices):
            for i in range(self.num_vertices):
                for j in range(self.num_vertices):
                    distancias[i][j] = min(distancias[i][j], distancias[i][k] + distancias[k][j])

        # Devolver la matriz de distancias mínimas
        return distancias

# Ejemplo de prueba
# Crear un grafo con 4 ciudades
grafo = Grafo(4)

# Agregar aristas con pesos que representan distancias entre ciudades
grafo.agregar_arista(0, 1, 10)  # Ciudad 0 a Ciudad 1
grafo.agregar_arista(0, 2, 15)  # Ciudad 0 a Ciudad 2
grafo.agregar_arista(1, 2, 5)   # Ciudad 1 a Ciudad 2
grafo.agregar_arista(1, 3, 12)  # Ciudad 1 a Ciudad 3
grafo.agregar_arista(2, 3, 7)   # Ciudad 2 a Ciudad 3

# Aplicar el algoritmo de Floyd-Warshall
resultado = grafo.floyd_warshall()

# Mostrar el resultado
print("Matriz de distancias mínimas:")
for fila in resultado:
    print(fila)

#importar libreria math
import math

class Grafo:
    def __init__(self):
        self.vertices = []  # Lista para almacenar los vértices del grafo
        self.matriz = []    # Matriz de adyacencia para representar las conexiones entre los vértices

    # Verifica si un vértice ya existe en la lista de vértices
    def existeVertice(self, v):
        return v in self.vertices

    # Agrega un nuevo vértice al grafo
    def agregarVertices(self, v):
        if self.existeVertice(v):  # Verifica si el vértice ya está en la lista de vértices
            return False
        self.vertices.append(v)  # Agrega el vértice a la lista de vértices

        # Redimensiona la matriz de adyacencia para incluir el nuevo vértice
        for fila in self.matriz:
            fila.append(None)  # Añade un espacio para la nueva conexión
        self.matriz.append([None] * len(self.vertices))  # Agrega una fila vacía a la matriz

        return True

    # Agrega una arista con un peso entre dos vértices al grafo
    def agregarArista(self, inicio, fin, valor, dirigida):
        if inicio not in self.vertices or fin not in self.vertices:
            return False  # Verifica si los vértices existen en la lista de vértices

        inicio_index = self.vertices.index(inicio)  # Obtiene el índice del vértice de inicio
        fin_index = self.vertices.index(fin)        # Obtiene el índice del vértice de destino

        self.matriz[inicio_index][fin_index] = valor  # Asigna el valor de la conexión a la matriz

        if not dirigida:
            self.matriz[fin_index][inicio_index] = valor  # Si no es dirigida, se asigna el valor en ambas direcciones

    # Imprime la matriz de adyacencia
    def imprimirMatriz(self):
        cadena = "\n\t" + "\t".join(str(v) for v in self.vertices)  # Encabezados de los vértices

        for fila, vertice in zip(self.matriz, self.vertices):
            cadena += f"\n{vertice}\t" + "\t".join(str(valor if valor is not None else 0) for valor in fila)

        print(cadena)  # Muestra la matriz en consola

# Método principal que ejecuta el programa
if __name__ == "__main__":
    g = Grafo()  # Se instancia la clase Grafo

    # Se agregan los vértices al grafo
    g.agregarVertices("V0")
    g.agregarVertices("V1")
    g.agregarVertices("V2")
    g.agregarVertices("V3")
    g.agregarVertices("V4")
    g.agregarVertices("V5")
    g.agregarVertices("V6")

    # Se agregan las aristas con sus respectivos pesos
    g.agregarArista("V0", "V1", 27.3, True)
    g.agregarArista("V1", "V2", 5.7, True)
    g.agregarArista("V2", "V3", 27.7, True)
    g.agregarArista("V3", "V4", 20.8, True)
    g.agregarArista("V4", "V5", 31.2, True)
    g.agregarArista("V5", "V6", 7.8, True)
    g.agregarArista("V6", "V0", 15.3, True)
    g.agregarArista("V6", "V1", 41.8, True)

    print("La matriz de adyacencia del grafo es:")
    g.imprimirMatriz()  # Imprime la matriz de adyacencia del grafo

import numpy as np

# Definir la matriz I - Q
I_minus_Q = np.array(
    [
        [0.08, -0.08, 0, 0],
        [-0.2, 0.6, -0.28, -0.12],
        [-0.06, -0.2, 0.77, -0.32],
        [0, -0.15, -0.32, 0.74],
    ]
)

# Calcular la inversa de I - Q
N = np.linalg.inv(I_minus_Q)
print(N)

# Calcular la suma de cada fila de la matriz N
sumas_filas = N.sum(axis=1)
print(sumas_filas)

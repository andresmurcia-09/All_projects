from functools import reduce
from statistics import mean, StatisticsError


def obtener_datos_ventas():
    # Función que permite ingresar datos de ventas (nombre del producto, cantidad y precio) y los almacena en una lista.
    ventas = []
    while True:
        # Solicita al usuario ingresar el nombre del producto o 'fin' para terminar
        producto = input(
            "Ingrese el nombre del producto (o ingrese 'fin' para terminar): "
        )
        if producto.lower() == "fin":  # Si se ingresa 'fin', se sale del ciclo.
            break
        cantidad = int(
            input(f"Ingrese la cantidad de unidades vendidas del producto {producto}:")
        )  # Solicita la cantidad vendida.
        precio = float(
            input(f"Ingrese el precio unitario en pesos del {producto}:")
        )  # Solicita el precio unitario.
        # Almacena los datos en la lista como una tupla (producto, cantidad, precio)
        ventas.append((producto, cantidad, precio))
    return ventas  # Devuelve la lista de ventas con los datos ingresados.


# Obtener datos de ventas del usuario
ventas = obtener_datos_ventas()

# Paso 1: Calcular las ventas totales por producto
ventas_totales = list(map(lambda x: (x[0], x[1] * x[2]), ventas))

# Paso 2: Filtrar productos con ventas totales superiores a 1000
ventas_superiores = list(filter(lambda x: x[1] > 1000, ventas_totales))

# Paso 3: Calcular el total de ventas de todos los productos
total_ventas = reduce(lambda x, y: x + y[1], ventas_totales, 0)

# Paso 4: Calcular el promedio de ventas por producto
promedio_ventas = 0  # Valor predeterminado si no hay ventas
if ventas_totales:  # Solo calcula el promedio si hay datos
    promedio_ventas = mean([x[1] for x in ventas_totales])

# Paso 5: Encontrar el producto con la mayor venta total
producto_max_venta = (
    reduce(lambda x, y: x if x[1] > y[1] else y, ventas_totales)
    if ventas_totales
    else None
)

# Paso 6: Filtrar productos con ventas totales inferiores a 500
ventas_inferiores = list(filter(lambda x: x[1] < 500, ventas_totales))

# Generar informe detallado
informe = f"""
Informe de Ventas:
-------------------
Ventas totales por producto:
{ventas_totales}
Productos con ventas superiores a 1000:
{ventas_superiores}
Total de ventas: {total_ventas}
Promedio de ventas por producto: {promedio_ventas:.2f}
Producto con la mayor venta total:
{producto_max_venta[0]} con ventas de {producto_max_venta[1]} si hay datos
Productos con ventas inferiores a 500:
{ventas_inferiores}
"""
print(informe)

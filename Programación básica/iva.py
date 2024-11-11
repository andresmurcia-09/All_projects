# Función para calcular el total de la compra sin IVA
def calcular_total(articulos):
    total = sum(articulos.values())  # Suma todos los precios de los artículos
    return total


# Función para calcular el valor del IVA
def calcular_iva(total, tasa_iva):
    # Multiplica el total sin IVA por la tasa del IVA (0.19)
    iva = total * tasa_iva
    return iva


# Función para calcular el total de la compra con IVA
def calcular_total_con_iva(total, iva):
    total_con_iva = total + iva  # Suma el total sin IVA más el IVA calculado
    return total_con_iva


# Función para calcular el cambio a devolver al cliente
def calcular_cambio(valor_pagado, total_con_iva):
    # Resta el valor pagado menos el total con IVA
    cambio = valor_pagado - total_con_iva
    return cambio


# Función principal del programa
def main():
    # Solicita al usuario la cantidad de artículos
    n = int(input("Ingrese la cantidad de artículos: "))
    articulos = {}
    # Solicita al usuario los nombres y precios de los artículos
    for i in range(n):
        articulo = input("Ingrese el nombre del artículo {}: ".format(i + 1))
        precio = float(input("Ingrese el precio del artículo {}: ".format(i + 1)))
        # Guarda el nombre y precio del artículo en un diccionario
        articulos[articulo] = precio
    tasa_iva = 0.19  # Define la tasa de IVA (19%)
    # Llama a las funciones para calcular los valores
    total = calcular_total(articulos)
    iva = calcular_iva(total, tasa_iva)
    total_con_iva = calcular_total_con_iva(total, iva)
    # Solicita al usuario el valor pagado por el cliente
    valor_pagado = float(input("Ingrese el valor pagado por el cliente: "))
    # Calcula el cambio a devolver
    cambio = calcular_cambio(valor_pagado, total_con_iva)
    # Muestra los resultados
    print("\n--- Resumen de la compra ---")
    print("Total sin IVA: ${:.2f}".format(total))
    print("IVA: ${:.2f}".format(iva))
    print("Total con IVA: ${:.2f}".format(total_con_iva))
    print("Valor pagado: ${:.2f}".format(valor_pagado))
    # Verifica si el cambio es mayor o igual a cero (pago suficiente) y muestra el cambio
    if cambio >= 0:
        print("Cambio: ${:.2f}".format(cambio))
    else:  # Si no, muestra que el valor pagado es insuficiente y cuánto falta para completar el pago
        print(
            "El valor pagado es insuficiente. Faltan ${:.2f} para completar el pago.".format(
                abs(cambio)
            )
        )


# Ejecuta la función principal del programa
if __name__ == "__main__":
    main()

print("Valor dentro del rango")
valor_minimo = 0
valor_maximo = 5

valor_ingresado = int(input(f"Ingrese un valor entre {valor_minimo} y {valor_maximo}: "))
valor_dentro_rango = valor_minimo <= valor_ingresado <= valor_maximo

print(f"El valor esta dentro del rango? {valor_dentro_rango}")
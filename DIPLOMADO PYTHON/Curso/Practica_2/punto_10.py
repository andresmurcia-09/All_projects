#  Calcular el factorial de un número ingresado por el usuario usando un bucle `for`

numero_ingresado = input("Ingresa un número para calcular su factorial: ")

if not numero_ingresado.isdigit():
    print("Error: Ingresa un número entero válido.")
else:
    numero = int(numero_ingresado)
    if numero < 0:
        print("El factorial no está definido para números negativos.")
    else:
        factorial = 1
        for i in range(1, numero + 1):
            factorial *= i
        print(f"El factorial de {numero} es: {factorial}")

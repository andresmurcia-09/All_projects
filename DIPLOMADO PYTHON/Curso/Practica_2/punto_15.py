# Calcular el número de dígitos de un número entero ingresado por el usuario usando un bucle `while`

numero_ingresado = input(
    "Ingresa un número entero para calcular su número de dígitos: ")

if not numero_ingresado.isdigit():
    print("Error: Ingresa un número entero válido.")
else:
    numero = int(numero_ingresado)
    if numero == 0:
        print("El número de dígitos es: 1")
    else:
        if numero < 0:
            numero = abs(numero)
        num_digitos = 0
        while numero > 0:
            numero //= 10
            num_digitos += 1
        print(f"El número de dígitos de {numero_ingresado} es: {num_digitos}")

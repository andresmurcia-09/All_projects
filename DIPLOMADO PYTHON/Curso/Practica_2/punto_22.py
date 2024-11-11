# Calcular la suma de los dígitos de un número entero ingresado por el usuario utilizando un bucle `while`.

numero = int(input("Ingresa un número entero: "))

suma_digitos = 0

while numero > 0:

    digito = numero % 10

    suma_digitos += digito

    numero //= 10

print("La suma de los dígitos es:", suma_digitos)

# Sumar los números pares del 1 al 100 utilizando un bucle `while`

numero_actual = 1
suma_pares = 0

while numero_actual <= 100:
    if numero_actual % 2 == 0:
        suma_pares += numero_actual

    numero_actual += 1

print("La suma de los números pares del 1 al 100 es:", suma_pares)

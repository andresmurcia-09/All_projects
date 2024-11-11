# Calcular el promedio de tres números ingresados por el usuario usando `if-elif`

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

dividendo = num1 + num1 + num3
divisor = 3
promedio = dividendo / divisor
print(promedio)

if promedio >= 0.0 and promedio <= 2.9 or promedio >= 0.0 and promedio <= 5.9:
    print(promedio, ":promedio bajo")
elif promedio >= 3.0 and promedio <= 3.9 or promedio >= 6.0 and promedio <= 7.8:
    print(promedio, ":promedio básico")
elif promedio >= 4.0 and promedio <= 4.4 or promedio >= 7.9 and promedio <= 8.8:
    print(promedio, ":promedio alto")
elif promedio >= 4.5 and promedio <= 5.0 or promedio >= 8.9 and promedio <= 10.0:
    print(promedio, ":promedio superior")

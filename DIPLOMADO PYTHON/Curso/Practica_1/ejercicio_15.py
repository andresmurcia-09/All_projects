# Imprimir una tabla de multiplicar del 1 al 10 para un número dado

num = int(input("Ingrese el número: "))

for i in range(1, 11, 1):
    print(num, "x", i, "=", num * i)
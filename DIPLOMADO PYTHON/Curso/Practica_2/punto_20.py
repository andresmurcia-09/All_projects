# Calcular el máximo común divisor (MCD) de dos números ingresados por el 
# usuario utilizando el algoritmo de Euclides y un bucle `while`

num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

while num2 != 0:
    i = num2
    num2 = num1 % num2
    num1 = i

print("El Máximo Común Divisor (MCD) de los números ingresados es:", num1)

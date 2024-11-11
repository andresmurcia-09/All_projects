num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

if num1 > num2 and num1 > num3:
    print(num1, " es el mayor")
elif num2 > num1 and num2 > num3:
    print(num2, " es el mayor")
elif num3 > num1 and num3 > num2:
    print(num3, " es el mayor")
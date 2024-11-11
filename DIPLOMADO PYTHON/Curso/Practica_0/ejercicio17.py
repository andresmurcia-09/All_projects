lado1 = float(input("Ingrese el lado 1: "))
lado2 = float(input("Ingrese el lado 2: "))
lado3 = float(input("Ingrese el lado 3: "))

if lado1 == lado2 == lado3:
    print("Triangulo equilatero")
elif lado1 == lado2  != lado3:
    print("triangulo isósceles")
elif lado1 != lado2 != lado3:
    print("Triangulo escaleno")
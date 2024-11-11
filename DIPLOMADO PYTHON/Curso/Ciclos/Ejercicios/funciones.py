def primer_funcion():
    print("Hello world")

primer_funcion()

print("-----------------------------------")

def suma (num1,num2):
    print(num1 + num2)

suma(2,3)

print("-----------------------------------")

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: No es posible dividir entre cero."
    return a / b

def menu():
    print("Calculadora")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

def calculadora():
    while True:
        menu()
        opcion = input("Seleccione una opción (1/2/3/4/5): ")

        if opcion == '5':
            print("Saliendo de la calculadora.")
            break

        if opcion not in {'1', '2', '3', '4'}:
            print("Opción inválida. Por favor, elija una opción válida (1/2/3/4/5).")
            continue

        num1 = input("Ingrese el primer número: ")
        num2 = input("Ingrese el segundo número: ")

        if not num1.isnumeric() or not num2.isnumeric():
            print("Error: Ingrese números válidos.")
            continue

        num1 = float(num1)
        num2 = float(num2)

        if opcion == '1':
            print("Resultado:", suma(num1, num2))
        elif opcion == '2':
            print("Resultado:", resta(num1, num2))
        elif opcion == '3':
            print("Resultado:", multiplicacion(num1, num2))
        elif opcion == '4':
            print("Resultado:", division(num1, num2))

calculadora()

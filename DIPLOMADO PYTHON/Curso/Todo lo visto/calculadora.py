while True:
    print("INGRESE LOS DOS NÚMEROS A CALCULAR")
    num1, num2 = int(input("Ingrese el primer número: ")), int(input("Ingrese el segundo número: "))
    suma,Resta,Multiplicación = num1 + num2, num1 - num2, num1 * num2
    print("Que operación desea realizar:\n1. Suma\n2. Resta\n3. Multiplicación\n4. División\n5. Cancelar y Salir")
    
    user = int(input("---- "))
    if user == 1:
        print(suma)
    elif user == 2:
        print(Resta)
    elif user == 3:
        print(Multiplicación)
    elif num2 == 0:
        print("ERROR, no se puede dividir entre 0 \nvuelve a intentarlo\n----- ")
    elif user == 4:
        print(num1 / num2)
    elif user == 5:
        break
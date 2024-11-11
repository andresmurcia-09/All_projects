# Determinar si un número ingresado por el usuario es primo utilizando un bucle `for`

numero_ingresado = int(input("Ingrese un número entero mayor o igual que 2: "))

if numero_ingresado < 2:
    print(f"{numero_ingresado} NO es un número primo.")
else:
    es_primo = True
    for i in range(2, int(numero_ingresado**0.5) + 1):
        if numero_ingresado % i == 0:
            es_primo = False

    if es_primo:
        print(f"{numero_ingresado} es un número primo.")
    else:
        print(f"{numero_ingresado} no es un número primo.")

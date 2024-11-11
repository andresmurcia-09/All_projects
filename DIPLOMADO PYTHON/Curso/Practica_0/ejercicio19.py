numero = int(input("Ingrese un número: "))

suma_divisores = 0
for i in range(1, numero):
    if numero % i == 0:
        suma_divisores += i

if suma_divisores == numero:
    print("Es un número perfecto")
else:
    print("No es un número perfecto")

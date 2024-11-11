# calcular la suma de los dígitos de un número

numero = int(input("Ingrese el número: "))
numero_str = str(numero)
suma_digitos = 0

for digito in numero_str:
    suma_digitos += int(digito)

print(suma_digitos)

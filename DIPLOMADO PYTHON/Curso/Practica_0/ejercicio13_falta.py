numero = int(input("Ingrese un número: "))

es_primo = False
if numero == 2:
    es_primo = True
elif numero > 2 and numero % 2 != 0:
    raiz = int(numero ** 0.5)
    es_primo = (2 ** (raiz + 1)) % numero == 1

if es_primo:
    print("Es primo")
else:
    print("No es primo")

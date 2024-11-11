cadena = input("Ingrese una cadena: ")

try:
    entero = int(cadena)
    print("Es un número entero")
except ValueError:
    print("No es un número entero")

año_actual = int(input("Ingrese el año actual: "))
año = int(input("Ingrese el año de nacimiento: "))

if año >= 1900 and año <= año_actual:
    print("Año de nacimiento válido")
else:
    print("Año de nacimiento inválido")
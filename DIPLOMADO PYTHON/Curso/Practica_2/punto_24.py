# Determinar si un año ingresado por el usuario es bisiesto utilizando `if-else`

año = int(input("Ingresa un año: "))

if (año % 4 == 0 and año % 100 != 0) or año % 400 == 0:
    print(año, "es un año bisiesto.")
else:
    print(año, "no es un año bisiesto.")

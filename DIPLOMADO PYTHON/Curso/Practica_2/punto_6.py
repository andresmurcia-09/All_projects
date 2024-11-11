# Imprimir "Aprobado" si la calificación ingresada por el usuario es mayor o igual a 
# 60, de lo contrario, imprimir "Reprobado" usando `if-else`

calificación = float(input("Ingrese su calificación: "))

if calificación >= 60:
    print("Aprobado")
else:
    print("Reprobado")
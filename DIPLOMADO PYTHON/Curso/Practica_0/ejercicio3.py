edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("Es mayor de edad")
elif edad < 18 and edad > 0:
    print("Es menor de edad")
else:
    print("La edad no existe")

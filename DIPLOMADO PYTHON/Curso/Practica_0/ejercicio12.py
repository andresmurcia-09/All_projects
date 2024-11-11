edad = int(input("Ingrese su edad: "))

print("1. Colombia") #Puede votar despues de los 18
print("2. Francia") #Puede votar después de los 16
print("3. Japon") #Puede votar después de los 20
print("4. Argentina") #Puede votar despues de los 18
print("5. México") #Puede votar despues de los 19

nacionalidad = int(input("Ingrese su nacionalidad: "))

if edad >= 18 and nacionalidad == 1:
    print("Puede votar")
elif edad < 18 and edad > 0 and nacionalidad == 1:
    print("No puede votar")
elif edad >= 16 and nacionalidad == 2:
    print("Puede votar")
elif edad < 16 and edad > 0 and nacionalidad == 2:
    print("No puede votar")
elif edad >= 20 and nacionalidad == 3:
    print("Puede votar")
elif edad < 20 and edad > 0 and nacionalidad == 3:
    print("No puede votar")
elif edad >= 18 and nacionalidad == 4:
    print("Puede votar")
elif edad < 18 and edad > 0 and nacionalidad == 4:
    print("No puede votar")
elif edad >= 19 and nacionalidad == 5:
    print("Puede votar")
elif edad < 19 and edad > 0 and nacionalidad == 5:
    print("No puede votar")
else:
    print("Seleccione un país")
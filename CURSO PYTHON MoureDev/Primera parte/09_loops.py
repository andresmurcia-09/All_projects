### Loops ###

# While
my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
else:  # Es opcional
    print("Mi condición es mayor o igual que 10")

print("La ejecución continúa")

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Se detiene la ejecución")
        break

    print(my_condition)

# For
for number in range(1, 101):
    print(number)

my_list = [35, 24, 62, 52, 30, 30, 17]
for element in my_list:
    print(element)

my_tuple = (19, 1.77, "Andrés", "Murcia", "Stiven")
for element in my_tuple:
    print(element)

my_set = {"Andrés", "Murcia", 19}
for element in my_set:
    print(element)

my_dict = {"Nombre": "Andrés", "Apellido": "Murcia", "Edad": 19, 1: "Python"}
for element in my_dict:
    print(element)
    if element == "Edad":
        break
else:
    print("El bucle for para mi diccionario ha finalizado")

print("La ejecución continúa")

for element in my_dict:
    print(element)
    if element == "Edad":
        continue
    print("Se ejecuta")
else:
    print("El bluce for para diccionario ha finalizado")

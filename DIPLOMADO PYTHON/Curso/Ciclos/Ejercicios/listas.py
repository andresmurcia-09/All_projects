my_list = [19, 1.77, "Andrés", "Murcia", "Torres", True, "Andrés"]
print(my_list)
print(my_list[0])

my_list.append("Perro")  # Añadir un nuevo elemento a la lista siempre al final
print(my_list)

my_list.pop()
print(my_list)

my_list.remove(True)
print(my_list)

print(len(my_list))

print(my_list.count("Andrés"))

print("----------------------------------------------------------")

my_list1 = [35, 24, 62, 52, 30, 30, 17]
print(my_list1)

my_list1.reverse()
print(my_list1)

my_list1.sort()
print(my_list1)

print(max(my_list1))
print(min(my_list1))

print(sum(my_list1))

print("----------------------------------------------------------")

my_list2 = ["Andrés", "Stiven", "Murcia", "Torres"]
print(my_list2)

my_list2.insert(1, "Micro")  # Inserta un elemento en la posición que queramos
print(my_list2)

del my_list2[1] # Elimina un elemento que le digamos por indice o toda la lista si no le decimos nada
print(my_list2)

print("Murcia" in my_list2)

print("----------------------------------------------------------")

v = ["r", "p", "q", "1", "P"]
print(v)

v.sort()
print(v)

v.clear()
print(v)
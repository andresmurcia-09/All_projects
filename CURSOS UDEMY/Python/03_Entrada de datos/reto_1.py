from random import randint

print("Sistema de ID")

nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
año_nacimiento = input("Ingresa tu año de nacimiento: ")

print("--------------------")

nombre = nombre[0:2].upper().strip()
apellido = apellido[0:2].upper().strip()
año_nacimiento = año_nacimiento[2:4].strip()
codigo_random = randint(0000, 9999)
id_unico = f"Su id es: {nombre}{apellido}{año_nacimiento}{codigo_random}"
print(id_unico)

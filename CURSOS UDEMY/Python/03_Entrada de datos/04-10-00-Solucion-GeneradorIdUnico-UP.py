from random import randint

print("*** Sistema Generador de ID Único ***")

nombre = input("Cual es tu nombre? ")
apellido = input("Cual es tu apellido? ")
anio_nacimiento = input("Cual es tu año de nacimiento (YYYY)? ")  # Y - year

# Normalizar los valores
nombre_2 = nombre.strip().upper()[0:2]
apellido_2 = apellido.strip().upper()[0:2]
anio_nacimiento_2 = anio_nacimiento.strip()[2:]  # Tambien puede ser [2:4]

# Generar el valor aleatorio
aleatorio = randint(1000, 9999)

# Generamos el valor de id unico
id_unico = f"{nombre_2}{apellido_2}{anio_nacimiento_2}{aleatorio}"

print(
    f"""\nHola {nombre},
    Tu nuevo número de identificación (ID) generado por el sistema es:
    {id_unico}
    Felicidades!"""
)

### Conditionals ###

# if-elif-else
my_condition = False

if my_condition:
    print("Se ejecuta la condición del if")  # Es lo mismo que if my_condition == True:
else:
    print("No se ejecuta la condición del if")

my_condition = 5 * 5

if my_condition != 10:
    print("Es diferente de 10")

if my_condition > 10 and my_condition < 20:
    print("Es mayor que 10 y menor que 20")
elif my_condition == 25:
    print("Es igual a 25")
else:
    print("Es menor o igual que 10 o mayor o igual que 20 o distinto de 25")

print("La ejecución continúa")

my_string = ""

if not my_string:
    print("Mi cadena de texto es vacia")

if my_string == "Mi cadena de texto":
    print("Si es igual")
else:
    print("No es igual")

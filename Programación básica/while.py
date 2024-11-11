# Ejemplo 1
contador = 0
# Mientras el contador sea menor a 5
while contador < 5:
    # Imprime el valor del contador
    print(contador)
    # Incrementa el contador en 1
    contador += 1

# Ejemplo 2
numero = 10
# Mientras el número sea mayor a 0
while numero > 0:
    # Imprime el valor del número
    print(numero)
    # Decrementa el número en 1
    numero -= 1

# Ejemplo 3
intentos = 3
# Mientras haya intentos disponibles
while intentos > 0:
    # Pide al usuario que ingrese la contraseña
    contraseña = input("Introduce la contraseña: ")
    # Verifica si la contraseña ingresada es correcta
    if contraseña == "Usta2023":
        # Si la contraseña es correcta, imprime el mensaje y termina el bucle
        print("Acceso concedido.")
        break
    else:
        # Si la contraseña es incorrecta, reduce el número de intentos
        intentos -= 1
        # Imprime un mensaje indicando los intentos restantes
        print(f"Contraseña incorrecta. Te quedan {intentos} intentos.")

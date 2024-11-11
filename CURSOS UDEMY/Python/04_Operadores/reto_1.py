print("Sistema de autenticación")

usuario = input("Ingrese el nombre de usuario: ").strip()
password = int(input("Ingrese el pin: "))

resultado = usuario == "admin" and password == 1234
print(f"El usuario es: {resultado}")
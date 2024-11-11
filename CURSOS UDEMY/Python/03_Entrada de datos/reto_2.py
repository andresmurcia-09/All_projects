print("Generador de email")
nombre_usuario = input("Ingrese su nombre: ")
apellidos_usuario = input("Ingrese sus apellidos: ")
nombre_empresa = input("Ingrese el nombre de la empresa: ")
dominio = input("Ingrese el dominido de la empresa(.com.co): ")

nombre_usuario = nombre_usuario.lower().strip().replace(" ", ".")
apellidos_usuario = apellidos_usuario.lower().strip().replace(" ", ".")
nombre_apellidos = f"{nombre_usuario}{apellidos_usuario}"
nombre_empresa = nombre_empresa.lower().strip().replace(" ", "")

resultado = f"El correo final es: {nombre_usuario}.{apellidos_usuario}@{nombre_empresa}{dominio}"
print(resultado)
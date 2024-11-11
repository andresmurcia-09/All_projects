print("Generador de email")
nombre_usuario = "Ubaldo Acosta Soto"
nombre_usuario = nombre_usuario.lower().strip()
nombre_usuario = nombre_usuario.replace(" ", ".")

nombre_empresa = "Global Mentoring"
extension = ".com.mx"
nombre_empresa = nombre_empresa.lower().strip()
nombre_empresa = f"@{nombre_empresa.replace(" ", "")}"

resultado = f"El correo final es: {nombre_usuario}{nombre_empresa}{extension}"
print(resultado)
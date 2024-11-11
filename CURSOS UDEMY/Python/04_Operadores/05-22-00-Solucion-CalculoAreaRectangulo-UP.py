print("*** Cáculo Área y Perímetro de un Rectángulo ***")

base = float(input("Ingresa la base del rectángulo: "))
altura = float(input("Ingresa la altura del rectángulo: "))

# Realizamos los cálculos
area = base * altura
perimetro = 2 * (base + altura)  # Aplicado la precedencia de operadores

print(f"El área del rectángulo es: {area}")
print(f"El perímetro del rectángulo es: {perimetro}")

print("S: soltero")
print("C: Casado")
print("D: Divorciado")

letra = str(input("Ingrese su estado civil: "))

if letra == "S" or letra == "s":
    print("Soltero/a")
elif letra == "C" or letra == "c":
    print("Casado/a")
elif letra == "D" or letra == "d":
    print("Divorciado/a")
else:
    print("Ingresó un dato erroneo")
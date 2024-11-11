peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en m: "))
imc = peso / (altura ** 2)

if imc < 18.5:
    print(imc,": Bajo peso")
elif imc >= 18.5 and imc < 25:
    print(imc,(": Peso normal"))
elif imc >= 25 and imc < 30:
    print(imc,(": Sobrepeso"))
elif imc >= 30:
    print(imc,": Está en obesidad")

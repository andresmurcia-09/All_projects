print("--------------------TEMPERATURA--------------------------")

def celsius_a_fahrenheit(temp1):
    fahren = 9/5*temp1+32
    print(fahren)

celsius_a_fahrenheit(int(input("Ingrese los °C: ")))
        
print("--------------------AREA-TRIANGULO--------------------------")

def area_triangulo(base,altura):
    area = base*altura/2
    print(area)

area_triangulo(int(input("Ingrese la base: ")), int(input("Ingrese la altura: ")))

print("--------------------PRIMO--------------------------")

def es_primo(num):
    if (num % divisor != 0 for divisor in range(2, int(num ** 0.5) + 1)):
        print(num, "es primo")
    else:
        print(num, "no es primo")

es_primo(int(input("Ingrese el número: ")))

print("--------------------FACTORIAL--------------------------")

def factorial(num):
    if not num.isdigit():
        print("Error: Ingresa un número entero válido.")
    else:
        numero = int(num)
        if numero < 0:
            print("El factorial no está definido para números negativos.")
        else:
            factorial = 1
        for i in range(1, numero + 1):
            factorial *= i
        print("El factorial de",num, "es",factorial)

factorial(input("Ingrese el número: "))
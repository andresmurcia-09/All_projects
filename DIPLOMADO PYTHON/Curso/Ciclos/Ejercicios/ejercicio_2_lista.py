numero = [2, 3, 8, 1, 3, 7, 7]
# Agregar los numeros pares en una lista y los impares en otra
# Mostar la lista de los pares con su suma y de los impares con su suma

num1 = []
num2 = []

for v in numero:
    if v % 2 == 0:
        num1.append(v)
    else:
        num2.append(v)
print(num1)
print(sum(num1))
print(num2)
print(sum(num2))

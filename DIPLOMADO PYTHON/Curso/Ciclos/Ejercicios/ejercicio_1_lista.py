lista = []

for i in range(3):
    x = int(input("Ingrese los datos: "))
    lista.append(x)

print(lista)
print(sum(lista))
# ------------------------------------------------
lista2 = []

x = int(input(": "))
y = int(input(": "))
z = int(input(": "))
lista2.append(x)
lista2.append(y)
lista2.append(z)
print(lista2, "= ", sum(lista2))
# ------------------------------------------------
lista = []
for i in range(5):
    i += 1
    x = int(input("Ingrese las calificaciones: "))
    lista.append(x)

print(lista)
print(sum(lista))
print(sum(lista) / i)
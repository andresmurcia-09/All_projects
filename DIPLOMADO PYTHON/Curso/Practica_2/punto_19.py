# Imprimir los primeros 10 números de la serie de Fibonacci utilizando un bucle `while`

a = 0
b = 1
count = 0

while count < 10:
    print(a)
    temp = a
    a = b
    b = temp + b
    count += 1

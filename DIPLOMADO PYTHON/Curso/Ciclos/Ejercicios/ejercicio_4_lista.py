lista = []
while True:
    for i in range(10):
        x = input("Ingrese los datos: ")
        if x == "1":
            print("Se acabo el programa")
            break
        else:
            lista.append(x)

    print(lista)
    break

capital = int(input("Digite el capital que desea invertir: "))
meses = int(input("Por cuantos meses desea invertir ese dinero: "))
if meses >= 1:
    print((capital * 0.02 * meses) + capital)
elif meses <= 0:
    print("No tuvo ganancias, está es perdiendo")

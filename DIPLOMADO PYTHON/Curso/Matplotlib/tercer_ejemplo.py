import matplotlib.pyplot as plt


meses = ["Enero","Febrero","Marzo","Abril","Mayo"]
ventas = [10, 25, 8, 16, 30]

plt.plot(meses, ventas, marker='o')
plt.xlabel("Meses")
plt.ylabel("Ventas")
plt.title("Gráfico de lineas")
plt.grid(True)
plt.show()
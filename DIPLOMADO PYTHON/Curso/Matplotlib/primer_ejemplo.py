import matplotlib.pyplot as plt


nombres = ["Juan", "Pedro", "Andrés", "Nancy", "Brayan", "Eric", "Jorge"]
edad = [25, 70, 19, 43, 18, 6, 44]

plt.bar(nombres, edad)
plt.xlabel("Nombres")
plt.ylabel("Edad")
plt.title("Gráfico")
plt.show()

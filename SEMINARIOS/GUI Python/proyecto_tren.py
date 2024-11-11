import tkinter as tk

# Crear la ventana principal
root = tk.Tk()
root.title("Construcción de un tren")

# Crear un lienzo (canvas) donde dibujar las figuras geométricas
canvas = tk.Canvas(root, width=1000, height=600)
canvas.pack()


# Funciones para dibujar cada parte del tren
def dibujar_base_rieles():
    # Rieles (rectángulos horizontales y líneas verticales)
    canvas.create_rectangle(50, 500, 950, 520, fill="gray", outline="black")
    for i in range(50, 950, 50):
        canvas.create_line(i, 500, i, 520, fill="black", width=2)
    # Riel inferior
    canvas.create_line(50, 530, 950, 530, fill="black", width=3)


def dibujar_locomotora():
    # Parte principal de la locomotora (rectángulo grande)
    canvas.create_rectangle(100, 300, 250, 450, fill="blue", outline="black", width=3)

    # Cabina de conducción (rectángulo pequeño)
    canvas.create_rectangle(
        150, 250, 230, 300, fill="darkblue", outline="black", width=3
    )

    # Ventanas (cuadrados)
    canvas.create_rectangle(160, 260, 180, 280, fill="white", outline="black")
    canvas.create_rectangle(200, 260, 220, 280, fill="white", outline="black")

    # Chimenea (rectángulo y círculo)
    canvas.create_rectangle(160, 210, 185, 250, fill="gray", outline="black")
    canvas.create_oval(160, 180, 185, 210, fill="black")

    # Detalle en la parte delantera (rombo)
    canvas.create_polygon(
        100, 400, 120, 450, 140, 400, 120, 350, fill="yellow", outline="black", width=2
    )

    # Llanta delantera (círculo)
    canvas.create_oval(100, 450, 150, 500, fill="black", outline="gray")

    # Conexiones con vagón (líneas)
    canvas.create_line(250, 400, 300, 400, fill="black", width=3)


def dibujar_vagon_1():
    # Cuerpo principal del vagón (rectángulo grande)
    canvas.create_rectangle(300, 320, 450, 450, fill="red", outline="black", width=3)

    # Ventanas del vagón (rectángulos pequeños)
    for i in range(300, 430, 30):
        canvas.create_rectangle(i, 340, i + 30, 380, fill="white", outline="black")

    # Ruedas del vagón (círculos)
    canvas.create_oval(320, 450, 370, 500, fill="black", outline="gray")
    canvas.create_oval(380, 450, 430, 500, fill="black", outline="gray")

    # Conexiones con vagones (líneas)
    canvas.create_line(450, 400, 500, 400, fill="black", width=3)


def dibujar_vagon_2():
    # Cuerpo principal del vagón (rectángulo grande)
    canvas.create_rectangle(500, 320, 650, 450, fill="green", outline="black", width=3)

    # Ventanas del vagón (rectángulos pequeños)
    for i in range(500, 630, 30):
        canvas.create_rectangle(i, 340, i + 30, 380, fill="white", outline="black")

    # Ruedas del vagón (círculos)
    canvas.create_oval(520, 450, 570, 500, fill="black", outline="gray")
    canvas.create_oval(580, 450, 630, 500, fill="black", outline="gray")

    # Conexiones con vagones (líneas)
    canvas.create_line(650, 400, 700, 400, fill="black", width=3)


def dibujar_vagon_3():
    # Cuerpo principal del vagón (rectángulo grande)
    canvas.create_rectangle(700, 320, 850, 450, fill="purple", outline="black", width=3)

    # Ventanas del vagón (rectángulos pequeños)
    for i in range(700, 830, 30):
        canvas.create_rectangle(i, 340, i + 30, 380, fill="white", outline="black")

    # Ruedas del vagón (círculos)
    canvas.create_oval(720, 450, 770, 500, fill="black", outline="gray")
    canvas.create_oval(780, 450, 830, 500, fill="black", outline="gray")


# Botones para construir el tren poco a poco
boton_rieles = tk.Button(root, text="Rieles", command=dibujar_base_rieles)
boton_rieles.pack()

boton_locomotora = tk.Button(root, text="Locomotora", command=dibujar_locomotora)
boton_locomotora.pack()

boton_vagon_1 = tk.Button(root, text="Vagón 1", command=dibujar_vagon_1)
boton_vagon_1.pack()

boton_vagon_2 = tk.Button(root, text="Vagón 2", command=dibujar_vagon_2)
boton_vagon_2.pack()

boton_vagon_3 = tk.Button(root, text="Vagón 3", command=dibujar_vagon_3)
boton_vagon_3.pack()

# Mostrar el lienzo
root.mainloop()

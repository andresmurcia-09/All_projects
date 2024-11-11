import tkinter as tk
import turtle
import sys

# Jorge Douglas Doncel Avila, PROGRAMACION AVANZADA, USTA, 1 2024
ventana = tk.Tk()
ventana.title("Generador de Figuras")
ventana.geometry("400x300")


def dibujar_triangulo():
    # Código para dibujar un triángulo

    tortuga = turtle.Turtle()
    tortuga.speed(0)

    for _ in range(3):
        tortuga.forward(100)
        tortuga.left(120)

    tortuga.hideturtle()
    pass


def dibujar_cuadrado():
    # Código para dibujar un cuadrado

    tortuga = turtle.Turtle()
    tortuga.speed(0)

    for _ in range(4):
        tortuga.forward(100)
        tortuga.left(90)

    tortuga.hideturtle()
    pass


def dibujar_octagono():
    # Código para dibujar un octógono

    tortuga = turtle.Turtle()
    tortuga.speed(0)

    for _ in range(8):
        tortuga.forward(50)
        tortuga.left(45)

    tortuga.hideturtle()
    pass


def borrar_figura():
    # Borrar la pantalla de la tortuga
    screen = turtle.Screen()
    screen.clear()

    # Ocultar la tortuga
    tortuga = turtle.Turtle()
    tortuga.hideturtle()


def detener_programa():
    sys.exit()


# Crear y configurar el botón de "Limpiar"
boton_limpiar = tk.Button(ventana, text="Limpiar", command=borrar_figura)
boton_limpiar.pack(pady=10)

# Crear y configurar el botón de "Detener"
boton_detener = tk.Button(ventana, text="Detener", command=detener_programa)
boton_detener.pack(pady=20)

menu = tk.Menu(ventana)
menu.add_command(label="Triángulo", command=dibujar_triangulo)
menu.add_command(label="Cuadrado", command=dibujar_cuadrado)
menu.add_command(label="Octógono", command=dibujar_octagono)

# Configurar el menú en la barra de menús
barra_menu = tk.Menu(ventana, tearoff=0)
barra_menu.add_cascade(label="Figuras", menu=menu)
ventana.config(menu=barra_menu)

ventana.mainloop()

sys.exit

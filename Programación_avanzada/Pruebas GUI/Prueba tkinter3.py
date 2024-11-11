import tkinter as tk
import turtle


def dibujar_triangulo():
    ventana_dibujo = turtle.Screen()
    tortuga = turtle.Turtle()
    tortuga.pendown()
    for _ in range(3):
        tortuga.forward(100)
        tortuga.left(120)
    ventana_dibujo.exitonclick()


def dibujar_cuadrado():
    ventana_dibujo = turtle.Screen()
    tortuga = turtle.Turtle()
    tortuga.pendown()
    for _ in range(4):
        tortuga.forward(100)
        tortuga.left(90)
    ventana_dibujo.exitonclick()


def dibujar_octogono():
    ventana_dibujo = turtle.Screen()
    tortuga = turtle.Turtle()
    tortuga.pendown()
    for _ in range(8):
        tortuga.forward(100)
        tortuga.left(45)
    ventana_dibujo.exitonclick()


root = tk.Tk()
root.title("Dibujo de Figuras Geométricas")

menu_bar = tk.Menu(root)
menu_figuras = tk.Menu(menu_bar)
menu_figuras.add_command(label="Triángulo", command=dibujar_triangulo)
menu_figuras.add_command(label="Cuadrado", command=dibujar_cuadrado)
menu_figuras.add_command(label="Octógono", command=dibujar_octogono)
menu_bar.add_cascade(label="Figuras", menu=menu_figuras)

root.config(menu=menu_bar)
root.mainloop()

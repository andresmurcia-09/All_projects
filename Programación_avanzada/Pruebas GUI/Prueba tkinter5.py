import tkinter as tk
from turtle import RawTurtle, TurtleScreen, TurtleGraphicsError


# Funciones para dibujar figuras
def draw_square(t):
    t.begin_fill()
    for _ in range(4):
        t.forward(100)
        t.right(90)
    t.end_fill()


def draw_triangle(t):
    t.begin_fill()
    for _ in range(3):
        t.forward(100)
        t.right(120)
    t.end_fill()


def draw_octagon(t):
    t.begin_fill()
    for _ in range(8):
        t.forward(50)
        t.right(45)
    t.end_fill()


def draw_circle(t):
    t.begin_fill()
    t.circle(50)
    t.end_fill()


def draw_rhombus(t):
    t.begin_fill()
    for _ in range(2):
        t.forward(100)
        t.right(60)
        t.forward(100)
        t.right(120)
    t.end_fill()


def draw_rectangle(t):
    t.begin_fill()
    for _ in range(2):
        t.forward(150)
        t.right(90)
        t.forward(100)
        t.right(90)
    t.end_fill()


def draw_pentagon(t):
    t.begin_fill()
    for _ in range(5):
        t.forward(100)
        t.right(72)
    t.end_fill()


def draw_hexagon(t):
    t.begin_fill()
    for _ in range(6):
        t.forward(80)
        t.right(60)
    t.end_fill()


# Función para actualizar el dibujo según la opción seleccionada
def update_drawing():
    shape = shape_var.get()
    color = color_var.get()
    t.clear()
    try:
        t.color(color)
    except TurtleGraphicsError:
        t.color("black")
    if shape == "Cuadrado":
        draw_square(t)
    elif shape == "Triángulo":
        draw_triangle(t)
    elif shape == "Octágono":
        draw_octagon(t)
    elif shape == "Círculo":
        draw_circle(t)
    elif shape == "Rombo":
        draw_rhombus(t)
    elif shape == "Rectángulo":
        draw_rectangle(t)
    elif shape == "Pentágono":
        draw_pentagon(t)
    elif shape == "Hexágono":
        draw_hexagon(t)


# Crear la ventana principal
root = tk.Tk()
root.title("Generador de Figuras Geométricas")

# Crear un lienzo de turtle en la ventana principal
canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

screen = TurtleScreen(canvas)
t = RawTurtle(screen)

# Crear un menú desplegable para seleccionar la figura
shape_var = tk.StringVar(value="Cuadrado")
shape_menu = tk.OptionMenu(
    root,
    shape_var,
    "Cuadrado",
    "Triángulo",
    "Octágono",
    "Círculo",
    "Rombo",
    "Rectángulo",
    "Pentágono",
    "Hexágono",
)
shape_menu.pack()

# Crear un menú desplegable para seleccionar el color
color_var = tk.StringVar(value="Black")
color_menu = tk.OptionMenu(
    root, color_var, "Black", "Red", "Green", "Blue", "Yellow", "Pink", "Purple"
)
color_menu.pack()

# Botón para actualizar el dibujo
draw_button = tk.Button(root, text="Dibujar", command=update_drawing)
draw_button.pack()

# Ejecutar la aplicación
root.mainloop()

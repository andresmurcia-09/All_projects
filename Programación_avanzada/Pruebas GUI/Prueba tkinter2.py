from tkinter import *
import tkinter as tk
from tkinter import messagebox, simpledialog


# Adriana Roció Otálora Robayo,PROGRAMACION AVANZADA, USTA, 2024
def TrianguloEquilatero_nuevo_presionado(event=None):
    root = tk.Toplevel()
    root.title("Triangulo Equilatero")
    canvas = tk.Canvas(root, width=300, height=300, bg="white")
    canvas.pack()
    canvas.create_polygon(100, 100, 50, 200, 150, 200, fill="blue")


def Triangulorectangulo_nuevo_presionado(event=None):
    root1 = tk.Toplevel()
    root1.title("Triangulo Rectangulo")
    canvas = tk.Canvas(root1, width=300, height=300, bg="white")
    canvas.pack()
    canvas.create_polygon(100, 100, 100, 200, 200, 200, fill="indian red")


def Cuadradocuad_nuevo_presionado(event=None):
    root2 = tk.Toplevel()
    root2.title("Cuadrado")
    canvas = tk.Canvas(root2, width=300, height=300, bg="white")
    canvas.pack()
    canvas.create_rectangle(100, 100, 200, 200, fill="red")


def Cuadradorectangulo_nuevo_presionado(event=None):
    root3 = tk.Toplevel()
    root3.title("Rectangulo")
    canvas = tk.Canvas(root3, width=300, height=300, bg="white")
    canvas.pack()
    canvas.create_rectangle(50, 50, 250, 130, fill="yellow")


def Octogonoregular_nuevo_presionado(event=None):
    root4 = tk.Toplevel()
    root4.title("Octogono Regular")
    canvas = tk.Canvas(root4, width=300, height=300, bg="white")
    canvas.pack()
    canvas.create_polygon(
        50,
        130,
        50,
        180,
        80,
        200,
        130,
        200,
        160,
        180,
        160,
        130,
        130,
        110,
        80,
        110,
        fill="lime green",
    )


def Octogonoirregular_nuevo_presionado(event=None):
    root5 = tk.Toplevel()
    root5.title("Octogono Irregular")
    canvas = tk.Canvas(root5, width=300, height=300, bg="white")
    canvas.pack()
    canvas.create_polygon(
        70,
        90,
        70,
        140,
        90,
        180,
        130,
        180,
        170,
        140,
        170,
        95,
        135,
        60,
        110,
        100,
        fill="cyan",
    )


ventana = tk.Tk()
ventana.geometry("400x400+0+0")
ventana.title("Figuras Geometricas")

barra_Menu = tk.Menu(ventana)
menu_Triangulos = tk.Menu(barra_Menu, tearoff=0)
menu_Triangulos.add_command(
    label="Equilátero", command=TrianguloEquilatero_nuevo_presionado, compound=tk.LEFT
)
menu_Triangulos.add_command(
    label="Rectángulo", command=Triangulorectangulo_nuevo_presionado, compound=tk.LEFT
)
menu_Cuadrado = tk.Menu(barra_Menu, tearoff=0)
menu_Cuadrado.add_command(
    label="Cuadrado", command=Cuadradocuad_nuevo_presionado, compound=tk.LEFT
)
menu_Cuadrado.add_command(
    label="Rectángulo", command=Cuadradorectangulo_nuevo_presionado, compound=tk.LEFT
)
menu_Octogonos = tk.Menu(barra_Menu, tearoff=0)
menu_Octogonos.add_command(
    label="Irregular", command=Octogonoirregular_nuevo_presionado, compound=tk.LEFT
)
menu_Octogonos.add_command(
    label="Regular", command=Octogonoregular_nuevo_presionado, compound=tk.LEFT
)


barra_Menu.add_cascade(menu=menu_Triangulos, label="Triangulos")
barra_Menu.add_cascade(menu=menu_Cuadrado, label="Cuadrados")
barra_Menu.add_cascade(menu=menu_Octogonos, label="Octogonos")

ventana.config(menu=barra_Menu)

ventana.mainloop()

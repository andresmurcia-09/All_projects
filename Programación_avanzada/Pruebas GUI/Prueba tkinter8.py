# Figuras Geométricas con colores
# Wilson Cano Arenas, PROGRAMACION AVANZADA, USTA, 1 2024
import tkinter as tk
from tkinter import ttk, Canvas
import math


def draw_square(canvas, color, size):
    canvas.delete("all")
    canvas.create_rectangle(
        150 - size, 150 - size, 150 + size, 150 + size, outline="black", fill=color
    )


def draw_rectangle(canvas, color, size):
    canvas.delete("all")
    width = size * 2.2
    height = size
    canvas.create_rectangle(
        150 - width / 2,
        150 - height / 2,
        150 + width / 2,
        150 + height / 2,
        outline="black",
        fill=color,
    )


def draw_octagon(canvas, color, size):
    canvas.delete("all")
    center_x, center_y = 150, 150
    points = []
    for i in range(8):
        angle = math.radians(45 * i)
        x = center_x + size * math.cos(angle)
        y = center_y + size * math.sin(angle)
        points.extend([x, y])
    canvas.create_polygon(points, outline="black", fill=color)


def draw_circle(canvas, color, size):
    canvas.delete("all")
    canvas.create_oval(
        150 - size, 150 - size, 150 + size, 150 + size, outline="black", fill=color
    )


def draw_equilateral_triangle(canvas, color, size):
    canvas.delete("all")
    h = size * math.sqrt(3) / 2
    points = [150, 150 - h, 150 - size, 150 + h / 2, 150 + size, 150 + h / 2]
    canvas.create_polygon(points, outline="black", fill=color)


def draw_scalene_triangle(canvas, color, size):
    canvas.delete("all")
    points = [150 - size, 150 + size, 150 + size, 150 + size, 150, 150 - size]
    canvas.create_polygon(points, outline="black", fill=color)


def draw_right_triangle(canvas, color, size):
    canvas.delete("all")
    points = [150, 150, 150 + size, 150, 150, 150 - size]
    canvas.create_polygon(points, outline="black", fill=color)


def on_select(event):
    selected_figure = figure_menu.get()
    selected_color = color_menu.get()
    size = size_scale.get()
    if selected_figure == "Cuadrado":
        draw_square(canvas, selected_color, size)
    elif selected_figure == "Rectángulo":
        draw_rectangle(canvas, selected_color, size)
    elif selected_figure == "Triángulo Equilátero":
        draw_equilateral_triangle(canvas, selected_color, size)
    elif selected_figure == "Triángulo Escaleno":
        draw_scalene_triangle(canvas, selected_color, size)
    elif selected_figure == "Triángulo Rectángulo":
        draw_right_triangle(canvas, selected_color, size)
    elif selected_figure == "Octágono":
        draw_octagon(canvas, selected_color, size)
    elif selected_figure == "Círculo":
        draw_circle(canvas, selected_color, size)


root = tk.Tk()
root.title("Actividad 1 - Generar Figuras Geométricas - PA_55RH1")
root.geometry("600x550")

figure_label = ttk.Label(root, text="Seleccione una figura")
figure_label.pack(pady=2)
figures = [
    "Cuadrado",
    "Rectángulo",
    "Triángulo Equilátero",
    "Triángulo Escaleno",
    "Triángulo Rectángulo",
    "Octágono",
    "Círculo",
]
selected_figure = tk.StringVar()
figure_menu = ttk.Combobox(root, textvariable=selected_figure)
figure_menu["values"] = figures
figure_menu.bind("<<ComboboxSelected>>", on_select)
figure_menu.pack(pady=10)

figure_label = ttk.Label(root, text="Si desea, puede escoger un color:")
figure_label.pack(pady=2)
colors = ["Blue", "Red", "Green", "Yellow", "Purple", "Orange"]
selected_color = tk.StringVar()
color_menu = ttk.Combobox(root, textvariable=selected_color)
color_menu["values"] = colors
color_menu.bind("<<ComboboxSelected>>", on_select)
color_menu.pack(pady=10)

figure_label = ttk.Label(root, text="Deslice para aumentar o disminuir su tamaño")
figure_label.pack(pady=2)
size_scale = ttk.Scale(root, from_=10, to_=90, orient="horizontal", length=200)
size_scale.set(75)
size_scale.pack(pady=10)
size_scale.bind("<Motion>", on_select)

canvas = Canvas(root, width=300, height=300, bg="white")
canvas.pack()

root.mainloop()

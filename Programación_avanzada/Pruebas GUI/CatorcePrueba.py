import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=300)
canvas.pack()
# Dibujar un poligono
canvas.create_polygon(
    200,
    50,
    150,
    100,
    150,
    150,
    200,
    200,
    300,
    200,
    350,
    150,
    350,
    100,
    300,
    50,
    fill="green",
)
root.mainloop()

import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=200, height=200)
canvas.pack()
# Dibujar un rectángulo
canvas.create_rectangle(20, 20, 120, 80, fill="red")
root.mainloop()

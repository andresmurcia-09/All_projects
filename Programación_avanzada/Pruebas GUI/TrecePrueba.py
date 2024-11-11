import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=200, height=200)
canvas.pack()
# Dibujar un círculo
canvas.create_oval(50, 50, 150, 150, fill="blue")
root.mainloop()

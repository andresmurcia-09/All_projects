from tkinter import *

ventana = Tk()
frames = Frame()  # Creacion del Frame
frames.pack()  # Empaquetamiento del Frame
frames.config(bg="blue")  # cambiar color de fondo
frames.config(width="400", height="200")  # cambiar tamaño
frames.config(bd=24)  # cambiar el grosor del borde
frames.config(relief="sunken")  # cambiar el tipo de borde
frames.config(cursor="heart")  # cambiar el tipo de cursor
ventana.mainloop()

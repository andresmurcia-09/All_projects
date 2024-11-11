from tkinter import *

ventana = Tk()
frame = Frame()
frame.place(relwidth=1, relheight=1)
boton = Button(frame, text="Hola, mundo!")
boton.place(x=60, y=40)
ventana.mainloop()

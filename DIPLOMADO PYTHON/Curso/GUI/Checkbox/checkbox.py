from tkinter import *

root = Tk()
root.title("Checkbox")

playa = IntVar()
montaña = IntVar()
rural = IntVar()

def opcion_viaje():
    opcion_elegida = ""
    if playa.get() == 1:
        opcion_elegida += "playa "
    if montaña.get() == 1:
        opcion_elegida += "montaña "
    if rural.get() == 1:
        opcion_elegida += "rural "
    texto_final.config(text=opcion_elegida)

frame = Frame(root)
frame.pack()
Label(frame, text="Elige una opción: ", width=50, font=("Arial", 25), fg="green").pack()

Checkbutton(root, text="playa", variable=playa, onvalue=1, offvalue=0, command=opcion_viaje).pack()
Checkbutton(root, text="montaña", variable=montaña, onvalue=1, offvalue=0, command=opcion_viaje).pack()
Checkbutton(root, text="rural", variable=rural, onvalue=1, offvalue=0, command=opcion_viaje).pack()

texto_final = Label(frame)
texto_final.pack()

root.mainloop()

#--------------------------------------------------------------------------------------------------------

from tkinter import *

root = Tk()
root.title("Checkbox")

playa = IntVar()
montaña = IntVar()
rural = IntVar()

def opcion_viaje():
    opciones_elegidas = []
    if playa.get() == 1:
        opciones_elegidas.append("playa")
    if montaña.get() == 1:
        opciones_elegidas.append("montaña")
    if rural.get() == 1:
        opciones_elegidas.append("rural")
    texto_final.config(text="Opciones elegidas: " + ", ".join(opciones_elegidas))

frame = Frame(root)
frame.pack()
Label(frame, text="Elige una opción: ", fg="blue", width=50, font=("Arial", 25)).pack()

Checkbutton(frame, text="Playa", variable=playa, onvalue=1, offvalue=0, command=opcion_viaje).pack()
Checkbutton(frame, text="Montaña", variable=montaña, onvalue=1, offvalue=0, command=opcion_viaje).pack()
Checkbutton(frame, text="Rural", variable=rural, onvalue=1, offvalue=0, command=opcion_viaje).pack()

texto_final = Label(frame, text="Opciones elegidas: ")
texto_final.pack()

root.mainloop()
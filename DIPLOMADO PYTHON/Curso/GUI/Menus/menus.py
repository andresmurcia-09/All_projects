from tkinter import *
from tkinter import messagebox


def accion_salir():
    respuesta = messagebox.askquestion("Desea salir", "¿Elige?")
    if respuesta == "yes":
        ventana.destroy()
    else:
        messagebox.showinfo("No saliste")


ventana = Tk()
ventana.title("Menus")

barra_menu = Menu(ventana)
ventana.config(menu=barra_menu, width=300, height=300)

archivo_menu_1 = Menu(barra_menu, tearoff=0)
archivo_menu_1.add_command(label="nuevo")
archivo_menu_1.add_command(label="Edición")

archivo_menu_2 = Menu(barra_menu, tearoff=0)
archivo_menu_2.add_command(label="Ejemplo")
archivo_menu_2.add_command(label="Versión")

archivo_menu_3 = Menu(barra_menu, tearoff=0)
archivo_menu_3.add_command(label="Salir", command=accion_salir)

barra_menu.add_cascade(label="Archivo", menu=archivo_menu_1)
barra_menu.add_cascade(label="Otro", menu=archivo_menu_2)
barra_menu.add_cascade(label="Ayuda", menu=archivo_menu_3)


ventana.mainloop()

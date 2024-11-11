from tkinter import *
from tkinter import messagebox

# Configuración de la ventana principal
root = Tk()
root.title("GUI_Tkinder")
root.geometry("500x300")
# root.iconbitmap("gui.ico")
root.resizable(0, 0)
root.config(bg="grey", cursor="mouse")


# Funciones CRUD
def Crear():
    messagebox.showinfo("Registro creado con éxito")
    limpiar_entradas()


def Leer():
    messagebox.showinfo("Leer", "Mostrando registros")
    limpiar_entradas()


def Actualizar():
    messagebox.showinfo("Registro actualizado con éxito")
    limpiar_entradas()


def Eliminar():
    messagebox.showinfo("Registro eliminado con éxito")
    limpiar_entradas()


def limpiar_entradas():
    entry_id.delete(0, END)
    entry_nombre.delete(0, END)
    entry_categoria.delete(0, END)
    entry_cantidad.delete(0, END)
    entry_precio.delete(0, END)


# Interfaz de Usuario
frame = Frame(root, bg="lightgrey")
frame.pack(pady=20)

Label(frame, text="ID", bg="lightgrey").grid(row=0, column=0, padx=10, pady=10)
entry_id = Entry(frame)
entry_id.grid(row=0, column=1, padx=10, pady=10)

Label(frame, text="Nombre", bg="lightgrey").grid(row=1, column=0, padx=10, pady=10)
entry_nombre = Entry(frame)
entry_nombre.grid(row=1, column=1, padx=10, pady=10)

Label(frame, text="Categoría", bg="lightgrey").grid(row=2, column=0, padx=10, pady=10)
entry_categoria = Entry(frame)
entry_categoria.grid(row=2, column=1, padx=10, pady=10)

Label(frame, text="Cantidad", bg="lightgrey").grid(row=3, column=0, padx=10, pady=10)
entry_cantidad = Entry(frame)
entry_cantidad.grid(row=3, column=1, padx=10, pady=10)

Label(frame, text="Precio", bg="lightgrey").grid(row=4, column=0, padx=10, pady=10)
entry_precio = Entry(frame)
entry_precio.grid(row=4, column=1, padx=10, pady=10)

Button(frame, text="Crear", command=Crear).grid(row=5, column=0, padx=10, pady=10)
Button(frame, text="Leer", command=Leer).grid(row=5, column=1, padx=10, pady=10)
Button(frame, text="Actualizar", command=Actualizar).grid(
    row=5, column=2, padx=10, pady=10
)
Button(frame, text="Eliminar", command=Eliminar).grid(row=5, column=3, padx=10, pady=10)

root.mainloop()

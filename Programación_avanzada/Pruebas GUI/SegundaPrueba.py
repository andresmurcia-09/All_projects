from tkinter import *

ventana = Tk()  # Se inicia la ventana
ventana.title("Empezando en Tkinter...")  # Se coloca título a la ventana
ventana.config(bg="black")  # Le da color al fondo
ventana.geometry("500x500")  # Cambia el tamaño de la ventana
ventana.protocol(
    "WM_DELETE_WINDOW", "onexit"
)  # Elimina la opción de salir ventana.resizable(0,0) # Evita que la ventana se pueda cambiar de tamaño
cuadro = Frame(ventana)  # Se crea un Frame dentro de la ventana creada
cuadro.pack()  # Se sitúa el frame en la ventana
v1 = Toplevel(ventana)  # Crea una ventana hija
ventana.mainloop()

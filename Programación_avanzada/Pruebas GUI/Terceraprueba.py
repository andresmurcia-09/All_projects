from tkinter import *

ventana = Tk()
ventana.config(bg="black")  # Le da color al fondo
ventana.geometry("500x500")  # Cambia el tamaño de la ventana
v = IntVar()


def funcion():  # Se ejecuta al tocar los RadioButton
    if v.get() == 1:
        print("H")
    elif v.get() == 2:
        print("Manual")
    elif v.get() == 3:
        print("L")
    seleccion = "Usted selecciono " + str(v.get())
    label2.config(text=seleccion)


c2 = Radiobutton(
    ventana, text="H", variable=v, value=1, command=funcion
)  # Ahora un RadioButton
c3 = Radiobutton(ventana, text="Manual", variable=v, value=2, command=funcion)
c4 = Radiobutton(ventana, text="L", variable=v, value=3, command=funcion)
c2.grid(row=2, column=0)
c3.grid(row=2, column=1)
c4.grid(row=2, column=2)
label2 = Label(ventana)  # Creamos una etiqueta donde imprimir la seleccion
label2.grid(row=3, column=1)
ventana.mainloop()

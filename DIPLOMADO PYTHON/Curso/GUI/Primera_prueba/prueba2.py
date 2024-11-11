from tkinter import *

root = Tk()

etiqueta = Label(root, text="Hola mundo", fg="Orange", font=("Comic Sans MS",40))
etiqueta.place(x=100, y=100)

root.title("PYTHON")
root.config(bg="black")
root.iconbitmap("aguila.ico")
root.geometry("1000x1000")

marco_principal = Frame()
marco_principal.pack(side="bottom")
marco_principal.config(bg="#194A06")
marco_principal.config(width="400", height="400")
marco_principal.config(bd=100)
marco_principal.config(relief="groove")
marco_principal.config(cursor="hand2")
hola = Label(marco_principal, text="FRAME", fg="#15064A", font=("Comic Sans MS",25))
hola.place(x=100, y=100)

root.mainloop()

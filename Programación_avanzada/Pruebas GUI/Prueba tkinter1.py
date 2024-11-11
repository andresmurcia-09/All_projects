#Johan Sebastián Peña Garzón, Programación Avanzada, USTA, 2024
import tkinter as tk
def dibuja_figura(figura_geometrica):
    canvas.delete("all")
    if figura_geometrica == "Triángulo":
        canvas.create_polygon(100, 100, 50, 200, 150, 200, fill="gold",outline="black", width=2)
    elif figura_geometrica == "Cuadrado":
        canvas.create_rectangle(20, 20, 120, 120, fill="dodgerblue",outline="black", width=2)
    elif figura_geometrica == "Rectángulo":
            canvas.create_rectangle(20, 20, 120, 80, fill="springgreen",outline="black", width=2)
    elif figura_geometrica == "Hexágono":
                canvas.create_polygon(50, 175, 100, 250, 200, 250, 250, 175, 200, 100,100, 100, fill="lawngreen", outline="black", width=2)
    elif figura_geometrica == "Octágono":
                    canvas.create_polygon(50, 20, 90, 20, 120, 50, 120, 90, 90, 120, 50, 120,20, 90, 20, 50, fill="deepskyblue", outline="black", width=2)
    elif figura_geometrica == "Círculo":
                    canvas.create_oval(50, 50, 150, 150, fill="dodgerblue2", outline="black",width=2)
ventana = tk.Tk()
ventana.title('Menú de Figuras Geométricas')
canvas = tk.Canvas(ventana, width=350, height=300)
canvas.pack()

def crear_boton_figura(figura, color):
    return tk.Button(ventana, text=figura, bg=color, command=lambda:dibuja_figura(figura))
    
boton_triangulo = crear_boton_figura("Triángulo","deepskyblue")
boton_triangulo.pack(side="left")

boton_cuadrado = crear_boton_figura("Cuadrado", "deepskyblue")
boton_cuadrado.pack(side="left")

boton_rectangulo = crear_boton_figura("Rectángulo", "deepskyblue")
boton_rectangulo.pack(side="left")

boton_hexagono = crear_boton_figura("Hexágono", "lawngreen")
boton_hexagono.pack(side="left")

boton_octogono = crear_boton_figura("Octágono", "lawngreen")
boton_octogono.pack(side="left")

boton_circulo = crear_boton_figura("Círculo", "lawngreen")
boton_circulo.pack(side="left")

canvas.pack()



ventana.mainloop()





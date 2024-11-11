print("*** Sistema de Reserva de Hotel ***")

# Variables del hotel
tarifa_diaria_sin_vista_mar = 150.50
tarifa_diaria_con_vista_mar = 190.50

# Pedimos la informacion al usuario
nombre_cliente = input("Nombre del Cliente: ")
dias_estadia = int(input("Días de estadía: "))
vista_al_mar_txt = input("Con vista al mar (Si/No)? ")
vista_al_mar = vista_al_mar_txt.strip().lower() == "si"

# Cálculo del costo total de la estancia
if vista_al_mar:
    costo_total = dias_estadia * tarifa_diaria_con_vista_mar
else:
    costo_total = dias_estadia * tarifa_diaria_sin_vista_mar

# Mostramos los detalles de la reserva
print("\n--------- Detalles de la Reservación ------------")
print(f"Cliente: {nombre_cliente}")
print(f"Días de estadía: {dias_estadia}")
print(f"Costo total: ${costo_total:.2f}")
print(f"Habitación con vista al mar: {'Sí' if vista_al_mar else 'No'}")

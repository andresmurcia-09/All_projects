print("*** Sistema Descuentos VIP ***")

NO_PRODUCTOS_DESCUENTO = 10
cantidad_productos = int(input("Cuantos productos compraste hoy? "))
tiene_membresia = input("Tienes la membresía de la tienda (Si/No)? ")

es_elegible_descuento = (
    cantidad_productos >= NO_PRODUCTOS_DESCUENTO
    and tiene_membresia.strip().lower() == "si"
)

print(f"Tienes acceso al descuento VIP? {es_elegible_descuento}")

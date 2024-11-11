print("*** Valor Dentro de Rango ***")

MINIMO = 0
MAXIMO = 5

# Solicitamos un valor entre 0 y 5
dato = int(input(f"Proporciona un dato entre {MINIMO} y {MAXIMO}: "))

# Verificamos si el dato se encuentra dentro de rango
# esta_dentro_rango = dato >= MINIMO and dato <= MAXIMO
esta_dentro_rango = MINIMO <= dato <= MAXIMO
print(f"Valor está dentro de rango? {esta_dentro_rango}")

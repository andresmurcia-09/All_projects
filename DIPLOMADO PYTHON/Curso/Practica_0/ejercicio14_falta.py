fecha = input("Ingrese una fecha en formato DD/MM/AAAA: ")

dia, mes, año = fecha.split("/")

dia = int(dia)
mes = int(mes)
año = int(año)

es_valida = True

if año < 1:
    es_valida = False

if mes < 1 or mes > 12:
    es_valida = False

dias_por_mes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):

    dias_por_mes[2] = 29

if dia < 1 or dia > dias_por_mes[mes]:
    es_valida = False

if es_valida:
    print("La fecha es válida")
else:
    print("La fecha no es válida")

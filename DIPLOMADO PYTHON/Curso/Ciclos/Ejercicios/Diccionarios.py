dic = {
    "Nombre" : "Andrés",
    "Apellido" : "Murcia",
    "Edad" : 19
}
print(dic)
print(dic["Apellido"])
print(len(dic))
print(dic.items())

dic["Apellido"] = "Torres"
print(dic)

dic["Altura"] = 1.77
dic["Casado"] = False
print(dic)
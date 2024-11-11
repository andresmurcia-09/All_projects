### Classes ###


class MyEmptyPerson:
    pass  # Para poder dejar la clase vacía


print(MyEmptyPerson)
print(MyEmptyPerson())

# Clase con constructor, funciones y popiedades privadas y públicas


class Person:
    def __init__(self, name, surname, alias="sin alias"):
        self.full_name = f"{name} {surname} ({alias})"  # Propiedad pública
        self.__name = name  # Propiedad privada

    def get_name(self):
        return self.__name

    def walk(self):
        print(f"{self.full_name} está caminando")


my_person = Person(
    "Andrés",
    "Murcia",
)
print(my_person.full_name)
print(my_person.get_name())
my_person.walk()

my_other_person = Person("Stiven", "Torres", "Capi")
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "Valentín"
print(my_other_person.full_name)

my_other_person.full_name = 666
print(my_other_person.full_name)

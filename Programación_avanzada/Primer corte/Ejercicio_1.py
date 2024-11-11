"""Escriba un programa que use clases, atributos, métodos y herencia, documéntelo."""


class Persona:

    def __init__(self, nombre, edad):
        """
        Inicializa los atributos de una persona.
        nombre (str): Nombre de la persona.
        edad (int): Edad de la persona.
        """
        self.nombre = nombre
        self.edad = edad

    def obtener_informacion(self):
        """
        Devuelve la información básica de la persona.

        Returns:
        str: Información de la persona.
        """
        return f"Nombre: {self.nombre}, Edad: {self.edad}"


def solicitar_dato(mensaje, tipo=str):
    """
    Solicita un dato al usuario y lo convierte al tipo especificado.

    mensaje (str(cadena de texto)): Mensaje a mostrar al usuario.
    tipo (type): Tipo al que se convertirá el dato ingresado (por defecto es str).

    Returns:
    tipo: El dato ingresado convertido al tipo especificado.
    """
    while True:
        try:
            dato = tipo(input(mensaje))
            return dato
        except ValueError:
            print(
                f"Entrada no válida. Por favor, ingrese un valor de tipo {tipo.__name__}."
            )


def ingresar_persona():
    """
    Solicita al usuario los datos para crear una Persona.
    """
    nombre = input("Nombre de la persona: ")
    edad = solicitar_dato("Ingrese la edad de la persona: ", int)
    return Persona(nombre, edad)


def main():
    """
    Función principal que permite al usuario ingresar datos para una persona y muestra la información.
    """
    print("Ingrese los datos de la persona:")
    persona = ingresar_persona()
    print("\nInformación de la persona:")
    print(persona.obtener_informacion())


# Ejecutar la función principal
if __name__ == "__main__":
    main()

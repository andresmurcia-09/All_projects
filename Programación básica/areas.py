import math


class Areas:
    def __init__(self):
        pass

    def cuadrado(self, lado):
        return lado * lado

    def triangulo(self, base, altura):
        return (base * altura) / 2

    def circulo(self, radio):
        return math.pi * radio * radio

    def pentagono(self, lado, apotema):
        perimetro = 5 * lado
        return (perimetro * apotema) / 2

    def hexagono(self, lado, apotema):
        perimetro = 6 * lado
        return (perimetro * apotema) / 2

    def cilindro(self, radio, altura):
        area_base = self.circulo(radio)
        return area_base * altura

    def cono(self, radio, altura):
        area_base = self.circulo(radio)
        area_lateral = math.pi * radio * math.sqrt(radio**2 + altura**2)
        return area_base + area_lateral


def main():
    areas = Areas()
    print("Área del cuadrado:", areas.cuadrado(4))
    print("Área del triángulo:", areas.triangulo(3, 5))
    print("Área del círculo:", areas.circulo(2))
    print("Área del pentágono:", areas.pentagono(3, 2.5))
    print("Área del hexágono:", areas.hexagono(4, 3.5))
    print("Área del cilindro:", areas.cilindro(2, 6))
    print("Área del cono:", areas.cono(2, 5))


if __name__ == "__main__":
    main()

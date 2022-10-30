import math

class Circulo:
    def __init__(self,radio,area,perimetro) -> None:
        self.radio = radio
        self.area = area
        self.perimetro = perimetro

    def Area(self):
        area = math.pi * self.radio**2
        self.area = area

    def Perimetro(self):
        perimetro = 2 * math.pi * self.radio
        self.perimetro = perimetro

radio = float(input("ingrese el radio de un circulo..."))

circulo = Circulo(radio,0,0)
Circulo.Area(circulo)
Circulo.Perimetro(circulo)

print(circulo.radio)
print(circulo.area)
print(circulo.perimetro)
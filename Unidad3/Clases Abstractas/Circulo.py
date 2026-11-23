from Figura import figura
import math

class Circulo(figura):

    def __init__(self, radio = 5, diametro = 10, circunferencia = 30):

        if radio < 0 or diametro < 0 or circunferencia < 0:

            raise ValueError("Algun parametro es negativo")

        self.radio = radio
        self.diametro = diametro
        self.circunferencia = circunferencia

    def area (self):

        return math.pi * self.radio ** 2

    def perimetro (self):

        return 2 * math.pi * self.radio

    def __str__ (self):

        return f"Circulo [Radio = {self.radio} | Diametro = {self.diametro}]"


c = Circulo()
print(c.perimetro())
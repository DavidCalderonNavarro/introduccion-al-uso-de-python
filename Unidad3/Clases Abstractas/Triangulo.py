from Figura import figura

class Triangulo(figura):

    def __init__ (self, base = 1, altura = 1):

        if base <= 0 or altura <= 0:
        
            raise ValueError("La base y la altura deben ser mayor que 0")

        self.base = base
        self.altura = altura

    def area (self):

        return self.base * self.altura

    def perimetro (self):
    
        return self.base *2 + self.altura * 2

    
        
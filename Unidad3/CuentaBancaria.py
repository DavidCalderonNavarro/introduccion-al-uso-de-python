class CuentaBancaria:
    def __init__ (self, nombre: str = "", saldo: float = 0):

        if saldo < 0:

            raise ValueError("El saldo no puede ser negativo")

        self.nombre = nombre
        self.saldo = saldo

    def ingresar (self, cantidad: float):

        if cantidad < 0:
            raise ValueError("Lan cantidad no puede ser negativa")

        self.saldo += cantidad

    def retirar (self, cantidad: float):

        if cantidad > self.saldo or cantidad < 0:

            raise ValueError("La cantidad no puede ser negativo o mayor al saldo")

        self.saldo -= cantidad

    def __str__ (self):

        return f"Cuenta Bancaria [Nombre = {self.nombre}] | Saldo = {self.saldo}]"

cuenta1 = CuentaBancaria("David")
cuenta2 = CuentaBancaria("Pepito", 1000)

print(cuenta1)
print(cuenta2)

print("Despues del cambio: ")

cuenta2.retirar(200)
print(cuenta2)
cuenta1.ingresar(500)
print(cuenta1)


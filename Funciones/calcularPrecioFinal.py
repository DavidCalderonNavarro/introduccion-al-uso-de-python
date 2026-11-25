def calcularPrecioFinal(precio: float, descuento: int) -> float:

    if descuento < 0 or descuento > 100:

        return -1

    descuentoFinal = (precio * descuento) / 100

    resultado = precio - descuentoFinal

    return round(resultado, 2)

print(calcularPrecioFinal(100, 20))  # 80.00
print(calcularPrecioFinal(50, 10))   # 45.00
print(calcularPrecioFinal(30, 100))  # 0.00
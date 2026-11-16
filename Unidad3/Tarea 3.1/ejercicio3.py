import math

def calcularValorBruto(valor_neto: float, tipo_iva: str) -> float:

    """Calcula el valor bruto de un producto en base a su valor neto y el tipo de IVA aplicado

    Args:
        valor_neto(Float): El valor neto del producto, eneuros
        tipo_iva(String): El tipo de IVA aplicable, que lleva asociado el porcentaje que aplica

    Returns:
        float: El valor bruto del producto tras aplicar el IVA
    
    """

    bruto = 0

    tipo_iva = tipo_iva.upper()

    if tipo_iva not in ["GENERAL", "REDUCIDO", "SUPERREDUCIDO"]:

        raise ValueError("El tipo de IVA solo puede ser General, Reducido o Superreducido")

    if valor_neto < 0:

        raise ValueError("El valor neto no puede ser negativo")

    if tipo_iva == "GENERAL":

        valor_bruto = valor_neto * 1.21

    elif tipo_iva == "REDUCIDO":

        valor_bruto = valor_neto * 1.10

    elif tipo_iva == "SUPERREDUCIDO":

        valor_bruto = valor_neto * 1.04

    return math.ceil(valor_bruto)

print(calcularValorBruto(10, "SupErReduCIdo"))
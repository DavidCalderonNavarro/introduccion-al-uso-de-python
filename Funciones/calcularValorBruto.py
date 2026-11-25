def calcularValorBruto(precioNeto: float, tipo_iva: str):

    GENERAL = 21
    REDUCIDO = 10
    SUPERREDUCIDO = 4

    resultado = -1

    if tipo_iva == "GENERAL":

        ivaFinal = (precioNeto * GENERAL) / 100

        resultado = precioNeto + ivaFinal

    elif tipo_iva == "REDUCIDO":

        ivaFinal = (precioNeto * REDUCIDO) / 100

        resultado = precioNeto + ivaFinal

    elif tipo_iva == "SUPERREDUCIDO":

        ivaFinal = (precioNeto * SUPERREDUCIDO) / 100

        resultado = precioNeto + ivaFinal

    return round(resultado, 2)

print(calcularValorBruto(100, "GENERAL"))
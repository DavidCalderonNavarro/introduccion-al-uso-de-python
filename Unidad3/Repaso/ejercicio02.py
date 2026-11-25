def convertir_acciones(compania, numero_acciones, moneda):

    compania = compania.upper()
    moneda = moneda.lower()

    # Comprobamos la compañía
    if compania == "NVDA":
        valor_accion = 156.20
    elif compania == "SONY":
        valor_accion = 24.16
    elif compania == "BMW":
        valor_accion = 58.12
    else:
        return 0

    # Comprobamos la moneda
    if moneda == "euro":
        cambio = 1
    elif moneda == "dolar":
        cambio = 1.10
    elif moneda == "libra":
        cambio = 0.83
    else:
        return 0

    # Calculamos el resultado
    resultado = valor_accion * numero_acciones * cambio

    return round(resultado, 2)


# Ejemplos
print(convertir_acciones("NVDA", 10, "Euro"))
print(convertir_acciones("SONY", 5, "dolar"))
print(convertir_acciones("BMW", 20, "libra"))

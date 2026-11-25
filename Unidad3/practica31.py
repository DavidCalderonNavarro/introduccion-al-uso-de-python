def convertir_acciones(compania: str, n_acciones: int, moneda: str) -> float:

    compania = compania.upper()
    moneda = moneda.lower()
    resultado = 0
    valor_acciones = 0
    cambio = 0

    if compania == "NVDA":

        valor_acciones = 156.20

    elif compania == "SONY":

        valor_acciones = 24.16

    elif compania == "BMW":

        valor_acciones = 58.12

    if moneda == "euro":

        cambio = 1

    elif moneda == "dolar":

        cambio = 1.10

    elif moneda == "libra":

        cambio = 0.83

    resultado = valor_acciones * n_acciones * cambio

    return round(resultado, 2)

print(convertir_acciones("NVDA", 10, "euro"))
print(convertir_acciones("SONY", 5, "dOlar"))
print(convertir_acciones("BMW", 20, "Libra"))
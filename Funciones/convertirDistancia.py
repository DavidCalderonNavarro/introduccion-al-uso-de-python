def convertirDistancia(numero: float, unidad1: str, unidad2: str) -> float:

    unidad1 = unidad1.upper()
    unidad2 = unidad2.upper()
    resultado = numero

    if unidad1 not in ["KM", "M", "CM"] or unidad2 not in ["KM", "M", "CM"]:

        raise ValueError("La unidad de medida es incorrecta")

    if unidad1 == "KM":

        if unidad2 == "M":

            resultado = numero * 1000

        elif unidad2 == "CM":

            resultado = numero * 100000

    if unidad1 == "M":

        if unidad2 == "KM":

            resultado = numero / 1000

        elif unidad2 == "CM":

            resultado = numero * 100

    if unidad1 == "CM":

        if unidad2 == "KM":

            resultado = numero / 100000

        elif unidad2 == "M":

            resultado = numero / 100

    return round(resultado,2)

print(convertirDistancia(2, "KM", "M"))    # 2000.00
print(convertirDistancia(150, "CM", "M"))  # 1.50
print(convertirDistancia(5, "M", "KM"))    # 0.01
print(f"{convertirDistancia(2, 'KM', 'M'):.2f}")
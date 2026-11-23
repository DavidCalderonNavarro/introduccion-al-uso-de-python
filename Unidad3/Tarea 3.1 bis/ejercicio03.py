def cambiar_divisa(cantidad_dinero: float, divisa: str, otra_divisa:str) -> float:

    resultado = cantidad_dinero
    divisa = divisa.upper()
    otra_divisa = otra_divisa.upper()

    if divisa not in ["EURO", "DOLAR", "YEN"] or otra_divisa not in ["EURO", "DOLAR", "YEN"]:

        raise ValueError("La unicas divisas validas son euro, dolar y yen")

    if divisa == "EURO":

        if otra_divisa == "DOLAR":

            resultado = cantidad_dinero * 1.09

        elif otra_divisa == "YENES":

            resultado = cantidad_dinero * 163.38

    elif divisa == "DOLAR":

        if otra_divisa == "EURO":

            resultado = cantidad_dinero * 0.92

        elif otra_divisa == "YENES":

            resultado = cantidad_dinero * 149.67

    elif divisa == "YENES":

        if otra_divisa == "EURO":

            resultado = cantidad_dinero * 0.0061

        elif otra_divisa == "DOLAR":

            resultado = cantidad_dinero * 0.0067

    return resultado

resultado2 = cambiar_divisa(23.30, "dolar", "eUro")

print(round(resultado2, 3))



animales = [
    ["Lobo ibérico", "Mamífero", 2500],
    ["Lince ibérico", "Mamífero", 1668],
    ["Quebrantahuesos", "Ave", 2000],
    ["Oso pardo", "Mamífero", 500]
]

def comprobar_estado(nombre_especie: str) -> str:

    nivel_de_amenaza = ""
    num_ejemplares = 0

    if nombre_especie.upper() == "LOBO IBÉRICO":

        num_ejemplares = animales[0][2]
            
    elif nombre_especie.upper() == "LINCE IBÉRICO":

        num_ejemplares = animales[1][2]

    elif nombre_especie.upper() == "QUEBRANTAHUESOS":

        num_ejemplares = animales[2][2]

    elif nombre_especie.upper() == "OSO PARDO":

        num_ejemplares = animales[3][2]

    if num_ejemplares == 0:
        nivel_de_amenaza = "Exinto"

    elif num_ejemplares > 0 and num_ejemplares <= 500:

        nivel_de_amenaza = "En peligro crítico"

    elif num_ejemplares > 500 and num_ejemplares <= 2000:

        nivel_de_amenaza = "En peligro"

    elif num_ejemplares > 2000:

        nivel_de_amenaza = "Amenazado"

    return nivel_de_amenaza

print(comprobar_estado("QueBRantAHuesOS"))
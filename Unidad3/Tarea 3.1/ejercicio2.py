def convertirTemperatura(temperatura_inicial: float, unidad_inicial: str, unidad_final: str) -> float:
    """Convierte una temperatura de la unidad inicial especificada a la unidad final especificada
    
    Args:
        temperatura_inicial(Float): La temperatura inical introducida por el usuario
        temperatura_final(Float): La temperatura final calculada mediante los parametros metidos
        unidad_inicial(String): La unidad de temperatura inicial
        unidad_final(String): La unidad de temperatura final

    Returns:
        float: La temperatura en la unidad final indicada
    
    """

    unidad_inicial = unidad_inicial.upper()
    unidad_final = unidad_final.upper()

    if unidad_inicial not in ["C", "K", "F"]:
        raise ValueError("La unidad inicial debe ser C, K o F")

    if unidad_final not in ["C", "K", "F"]:
            raise ValueError("La unidad inicial debe ser C, K o F")

    temperatura_final = 0

    if unidad_inicial == "C":
        if unidad_final == "F":
            temperatura_final = temperatura_inicial * (9/5) + 32
        elif unidad_inicial == "K":
            temperatura_final = temperatura_inicial - 273.15
    elif unidad_inicial == "F":
        if unidad_final == "C":
            temperatura_final = (temperatura_inicial - 32) * (5/9)
        elif unidad_final == "K":
            temperatura_final = ((temperatura_inicial -32) * (5/9)) + 273
    elif unidad_inicial == "K":
        if temperatura_inicial < 0:
            raise ValueError("La temperatura no puede ser menor a 0")
        if unidad_final == "F":
            temperatura_final = (temperatura_inicial - 275.15) * (9/5)
        elif unidad_final == "C":
            temperatura_final = temperatura_inicial + 273.15

    return round(temperatura_final, 2)

print(convertirTemperatura(100, "F", "C"))
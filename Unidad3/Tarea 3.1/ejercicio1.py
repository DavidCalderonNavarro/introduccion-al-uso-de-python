def comprobarLetraDNI(dni: str) -> bool:

    """Comprueba que el dni introducido sea correcto
    
    Args:
        dni(String): El parametro introducido por el usuario

    Returns:
        bool: Devuelve si la letra del dni introducido es correcta o no
    """

    letras = "TRWAGMYFPDXBNJZSQVHLCKE"
    
    if len(dni) != 9:
        return False

    if not dni[:8].isdigit():
        return False

    if not dni[8].isalpha():
        return False

    numero = int(dni[:8])
    letra_correcta = letras[numero % 23]

    return dni[8].upper() == letra_correcta

print(comprobarLetraDNI("08114685D"))
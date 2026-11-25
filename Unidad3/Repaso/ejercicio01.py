def convertir_acciones(compania, numero_acciones, moneda):
    # Valor de una accion expresado en euros
    valores_acciones = {
        "NVDA": 156.20,
        "SONY": 24.16,
        "BMW": 58.12
    }

    # Equivalencia de un euro en cada moneda
    tipos_cambio = {
        "euro": 1.0,
        "dolar": 1.10,
        "libra": 0.83
    }

    # Pasamos los textos a minusculas para aceptar cualquier combinacion
    compania = compania.upper()
    moneda = moneda.lower()

    # Comprobamos que la compania y la moneda sean validas
    if compania not in valores_acciones or moneda not in tipos_cambio:
        return 0

    # Calculamos el valor total de las acciones en euros
    total_euros = valores_acciones[compania] * numero_acciones

    # Convertimos el total a la moneda elegida
    resultado = total_euros * tipos_cambio[moneda]

    # Redondeamos a dos decimales
    return round(resultado, 2)


# Ejemplos de la practica
print(convertir_acciones("NVDA", 10, "euro"))   # 1562.0
print(convertir_acciones("SONY", 5, "dolar"))   # 132.88
print(convertir_acciones("BMW", 20, "libra"))   # 964.79
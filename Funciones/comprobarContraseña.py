def comprobarContraseña(contrasena: str) -> bool:

    tieneMayuscula = False
    tieneMinuscula = False
    tieneNumero = False

    for letra in contrasena:

        if letra.isupper():
            tieneMayuscula = True

        elif letra.islower():
            tieneMinuscula = True

        elif letra.isdigit():
            tieneNumero = True

        if tieneMayuscula and tieneMinuscula and tieneNumero:
            break

    return len(contrasena) >= 8 and tieneNumero and tieneMayuscula and tieneMinuscula

print(comprobarContraseña("HolaMundo11@"))
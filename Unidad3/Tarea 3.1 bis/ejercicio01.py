def sumatorio(numero: int) -> int:

    sumar = 0

    for i in range(1, numero + 1):

        sumar += i

    return sumar

def factorial(numero: int) -> int:

    multi = 1

    if numero < 1:

        raise ValueError("El numero tiene que ser mayor o igual a 1")

    else:

        for i in range(1, numero + 1):

            multi *= i

    return multi


def aplicar_funcion(num: int, modo: str):

    if num < 1 and modo == "factorial":

        raise ValueError("El valor introducido es erroneo")

    elif modo == "sumatorio":

        resultado = sumatorio(num)

    elif modo == "factorial":

        resultado = factorial(num)

    return resultado

print(aplicar_funcion(3, "factorial"))

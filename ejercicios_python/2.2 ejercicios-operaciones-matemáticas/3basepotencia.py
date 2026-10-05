base = int(input("Dime la base: "))
potencia = int(input("Dime la potencia: "))
resultado = 1

if base > 1:
    if potencia > 0:
        for i in range(1, potencia + 1):
            resultado = resultado * base

    print(resultado)
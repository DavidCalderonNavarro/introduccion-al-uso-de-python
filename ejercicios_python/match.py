dia = input("Introduce un día: ")
numero = int(input("Introduce un numero: "))

match dia:
    case "Lunes" | "Miercoles":
        print("Hay clase")
    case "Martes" | "Jueves" | "Viernes":
        print("No hay clase")
    case _:
        print("Error")

match numero:
    case n if n < 0:
        print("Negativo")
    case n if n > 0:
        print("Positivo")
    case _:
        print("Cero")
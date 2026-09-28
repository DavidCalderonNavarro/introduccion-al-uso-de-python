numero = int(input("Introduce un número: "))
dia = input("Introduce un día: ")

if numero > 0:
    print("Positivo")
elif numero < 0:
    print("Negativo")
else:
    print("Cero")

if dia == "Lunes" or dia == "Miercoles":
    print("Hay clases")
elif dia == "Martes" or dia == "Jueves" or dia == "Viernes":
    print("No hay clase")
else:
    print("Error")
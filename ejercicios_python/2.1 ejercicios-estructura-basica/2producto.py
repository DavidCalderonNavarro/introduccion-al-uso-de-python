precioFinal = 0

precio = float(input("Dime el precio del producto: "))

tipoIva = input("Dime el tipo de IVA: ")

if tipoIva == "General":
    precioFinal = precio * 1.21
elif tipoIva == "Reducido":
    precioFinal = precio * 1.10
elif tipoIva == "Superreducido":
    precioFinal = precio * 1.04

print("Tu precio final es: ", precioFinal)

match tipoIva:
    case "General":
        precioFinal = precio * 1.21
    case "Reducido":
        precioFinal = precio * 1.10
    case "Superreducido":
        precioFinal = precio * 1.04
    case _:
        print("Error")
        
print("Tu precio final es: ", precioFinal)
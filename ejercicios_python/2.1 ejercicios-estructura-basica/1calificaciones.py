nota = int(input("Dime tu nota: "))

# Con if:

if nota == 10 or nota == 9:
    print("Sobresaliente")
elif nota == 8 or nota == 7:
    print("Notable")
elif nota == 6 or nota == 5:
    print("Aprobado")
elif nota < 5 and nota >= 0:
    print("Suspenso")
else:
    print("Error")
    
# Con match:

match nota:
    case 10 | 9:
        print("Sobresaliente")
    case 8 | 7:
        print("Notable")
    case 6 | 5:
        print("Aprobado")
    case nota if nota < 5 and nota >= 0:
        print("Suspenso")
    case _:
        print("Error")
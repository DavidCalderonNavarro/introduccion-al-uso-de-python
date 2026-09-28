nota = int(input("Dime tu nota: "))

if nota == 10 or nota == 9:
    print("Sobresaliente")
elif nota == 8 or nota == 7:
    print("Notable")
elif nota == 6 or nota == 5:
    print("Aprobado")
elif nota < 5 and nota > 0:
    print("Suspenso")
else:
    print("Error")
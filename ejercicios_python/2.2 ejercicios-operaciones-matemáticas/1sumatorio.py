numero = int(input("Dime un numero: "))
sumatorio = 0

if numero >= 1:
    for i in range(1, numero + 1):
        sumatorio = sumatorio + i
else:
    print("Error")

print(sumatorio)

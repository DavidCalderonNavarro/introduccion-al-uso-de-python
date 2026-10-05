numero = int(input("Dime un numero: ")) + 1

if numero > 1:
    for i in range(1, numero, +1):
        print(i)
else:
    print("Error")
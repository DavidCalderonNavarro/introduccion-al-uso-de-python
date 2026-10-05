numero1 = int(input("Dime un numero: "))
numero2 = int(input("Dime otro numero: ")) + 1

for i in range(numero1, numero2, +1):

    primo = True

    if i < 2:
        primo = False

    for numPrimo in range(2,i):
        if i % numPrimo == 0:
            primo = False

    if primo:
        print(i)
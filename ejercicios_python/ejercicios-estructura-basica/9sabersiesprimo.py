numero = int(input("Dime un numero: "))
primo = True

if numero >= 2:

    for i in range(2, numero, 1):

        if numero % i == 0:
            primo = False

else:
    primo = False


if primo == True:
    print("Tu numero es primo")

else:
    print("Tu numero no es primo")
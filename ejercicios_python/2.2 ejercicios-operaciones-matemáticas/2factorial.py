numero = int(input("Dime un numero: "))
factorial = 1

if numero >= 1:
    for i in range(1, numero + 1):
        factorial = factorial * i
else:
    print("Error")

print(factorial)
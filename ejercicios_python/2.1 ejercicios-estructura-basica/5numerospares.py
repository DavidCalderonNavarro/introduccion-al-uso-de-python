num1 = int(input("Dime tu primer numero: "))
num2 = int(input("Dime tu primer numero: "))

if num1 > num2:
    print("Error")
else:
    
    for numero in range(num1, num2):
        
        if numero % 2 == 0:
            print(numero)

#Version con while

if num1 > num2:
    print("Error")
else:

    i = num1
    while i < num2:
        if i % 2 == 0:
            print(i)
        i = i + 1
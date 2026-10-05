edad = int(input("Dime tu edad: "))

if edad > 0:
    
    if edad >= 18:
        print("Eres mayor de edad")
        if edad > 120:
            print("y eres un vampiro")
    else:
        print("Eres menor de edad")
else:
    
    print("Error")
    
milimetros = int(input("Dime los milimetros de lluvia: "))

if milimetros < 60:
    print("No hay alerta")
elif milimetros >= 60 and milimetros < 120:
    print("Hay alerta amarilla")
elif milimetros >= 120:
    print("Hay alerta roja")
    
match milimetros:
    case m if m < 60:
        print("No hay alerta")
    case m if m >= 60 and milimetros < 120:
        print("Hay alerta amarilla")
    case m if m >= 120:
        print("Hay alerta roja")

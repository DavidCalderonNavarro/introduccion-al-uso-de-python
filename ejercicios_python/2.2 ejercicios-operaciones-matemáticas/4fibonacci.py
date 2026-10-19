numero = int(input("Introduce un número entero: "))

if numero < 0:
    print("Error: el número debe ser mayor o igual que 0.")
else:
    fibonacci = []
    a = 0
    b = 1

    for i in range(numero):
        fibonacci.append(a)
        a, b = b, a + b

    print("Lista de Fibonacci:", fibonacci)
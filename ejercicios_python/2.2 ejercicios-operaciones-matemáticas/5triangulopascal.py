filas = int(input("Introduce el número de filas: "))

if filas < 1:
    print("Error: el número debe ser mayor o igual que 1.")
else:
    triangulo = []

    for i in range(filas):
        fila = [1]

        for j in range(1, i):
            fila.append(triangulo[i - 1][j - 1] + triangulo[i - 1][j])

        if i > 0:
            fila.append(1)

        triangulo.append(fila)

    for fila in triangulo:
        print(fila)
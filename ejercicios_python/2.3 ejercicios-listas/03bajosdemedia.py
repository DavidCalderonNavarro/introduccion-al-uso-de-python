from datos import pokemons

contador = 0
suma = 0

for i in pokemons:
    contador += 1
    suma += i["altura_m"]

media = suma / contador

for i in pokemons:
    if i["altura_m"] < media:
        print("Nombre: ", i["nombre"],
              "Altura: ", i["altura_m"])
from datos import pokemons

contador = 0
suma = 0

for i in pokemons:
    contador += 1
    suma += i["altura_m"]

media = suma / contador

print("La media de altura es de ", media, "cm")
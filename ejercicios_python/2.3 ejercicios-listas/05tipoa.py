from datos import pokemons

for i in pokemons:
    for tipos in i:
        if tipos[-1] == "a":
            print(i)
            break


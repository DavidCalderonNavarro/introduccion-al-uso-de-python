from datos import pokemons

for i in pokemons[:]:
    if "Normal" in i["tipos"]:
        pokemons.remove(i)
        print(i)
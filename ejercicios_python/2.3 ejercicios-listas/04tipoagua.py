from datos import pokemons

for i in pokemons:
    if "Agua" in i["tipos"]:
        print("Nombre: ", i["nombre"],
              "Tipo: ", i["tipos"])
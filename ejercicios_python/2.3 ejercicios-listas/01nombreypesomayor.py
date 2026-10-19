from datos import pokemons

peso = 0
nombre = ""

for i in pokemons:

    if i["peso_kg"] > peso:
       peso = i["peso_kg"]
       nombre = i["nombre"]

print("El pokemon ", nombre , " es el que mas peso tiene con ", peso, "kg")
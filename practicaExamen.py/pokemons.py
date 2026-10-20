from datos import personajes

def ejercicio1():

    nuevo_pokemon = {
            "nombre": "Krokodile",
            "tipo": ["Tierra", "Siniestro"],
            "nivel": 40,
            "habilidades": ["Intimidación", "Autoestima"],
            "estadisticas": {
                "ataque": 229,
                "defensa": 158,
                "velocidad": 78
            }
        }
    personajes.append(nuevo_pokemon)

def ejercicio2():

    for pokemons in personajes:
        if pokemons["nivel"] > 30:
            print(pokemons["nombre"], pokemons["tipo"], pokemons["nivel"])

def ejercicio3():

    contador = 0
    media_velocidad = 0

    for pokemons in personajes:
        media_velocidad += pokemons["estadisticas"]["velocidad"]
        contador += 1

    media_velocidad = media_velocidad / contador

    for pokemons in personajes:
        if pokemons["estadisticas"]["velocidad"] > media_velocidad:
            print(pokemons["nombre"], pokemons["estadisticas"]["velocidad"])

def ejercicio4():

    for pokemons in personajes:
        if "Rayo" in pokemons["habilidades"]:
            pokemons["estadisticas"]["ataque"] += 10

            if pokemons["estadisticas"]["ataque"] > 100:

                pokemons["estadisticas"]["ataque"] = 100

        print(pokemons["nombre"], pokemons["estadisticas"]["ataque"])

def ejercicio5():

    print("Ejercicio 5")
    pokemon_referencia = personajes[0]

    for pokemons in personajes:
        if pokemons["nombre"] != "Pikachu":
            if pokemons["estadisticas"]["ataque"] > pokemon_referencia["estadisticas"]["defensa"]:
                print(pokemons)

def ejercicio6():

    print("Ejercicio 6")

    for pokemons in personajes:
        if pokemons["nivel"] < 20:
            personajes.remove(pokemons)

    print(personajes)
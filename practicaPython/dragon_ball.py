from datos import personajes

def ejercicio1():

    nuevo = {
        "nombre": "Gohan",
        "raza": "Saiyan",
        "nivel_pelea": 7000000,
        "tecnicas": ["Kamehameha", "Bola de fuego"],
        "atributos": {
            "fuerza": 79,
            "defensa": 90,
            "velocidad": 81
        }
    }

    personajes.append(nuevo)

def ejercicio2():

    for personaje in personajes:

        suma = 0
        suma = personaje["atributos"]["fuerza"] + personaje["atributos"]["defensa"] + personaje["atributos"]["velocidad"]
        media = suma /3

        if media > 85:
            print(personaje)

def ejercicio3():

    suma = 0
    contador = 0

    for personaje in personajes:

        suma +=  personaje["atributos"]["velocidad"]
        contador += 1

    media = suma / contador

    for personaje in personajes:

        if personaje["atributos"]["velocidad"] > media:
            print(personaje)

def ejercicio4():

    for personaje in personajes:

        if "Kamehameha" in personaje["tecnicas"]:
            personaje["atributos"]["fuerza"] += 8

            if personaje["atributos"]["fuerza"] > 100:

                personaje["atributos"]["fuerza"] = 100

            print(personaje["nombre"], personaje["atributos"]["fuerza"])

def ejercicio5():

    for personaje in personajes:
        if personaje["nombre"] == "Freezer":

            freezer = personaje

    for personaje in personajes:

        if personaje["nombre"] != "Freezer":

            if freezer["atributos"]["fuerza"] > personaje["atributos"]["defensa"]:

                print(personaje["nombre"], personaje["atributos"]["defensa"])

def ejercicio6():

    for personaje in personajes[:]:

        if personaje["raza"] == "Saiyan":

            personajes.remove(personaje)

    for personaje in personajes:

        print(personaje)
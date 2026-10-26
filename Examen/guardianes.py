from datos import personajes

def ejercicio1():

    nuevo_personaje = {
    "nombre": "Pepito",
    "raza": "Humano",
    "ocupacion": "Cazador de bestias",
    "estilo_combate": ["Respiración del Agua", "Respiración del Sol"],
    "atributos":{"fuerza": 75, "defensa": 68, "velocidad": 90}
    }

    personajes.append(nuevo_personaje)

def ejercicio2():

    suma = 0

    for personaje in personajes:

        suma = personaje["atributos"]["fuerza"] + personaje["atributos"]["defensa"] + personaje["atributos"]["velocidad"]
        media = suma / 3

        if media > 85:
            print(personaje)

def ejercicio3():

    suma = 0
    contador = 0

    for personaje in personajes:

        suma += personaje["atributos"]["fuerza"]
        contador += 1

    media = suma / contador

    for personaje in personajes:

        if personaje["atributos"]["fuerza"] > media:

            print(personaje)

def ejercicio4():

    for personaje in personajes:
            
            if "Respiración del Agua" in personaje["estilo_combate"]:
                personaje["atributos"]["defensa"] += 10
    
                if personaje["atributos"]["defensa"] > 100:
    
                    personaje["atributos"]["defensa"] = 100
    
            print(personaje["nombre"], personaje["atributos"]["defensa"])

def ejercicio5():

    zenitsu = ""

    for personaje in personajes:

        if personaje["nombre"] == "Zenitsu Agatsuma":

            zenitsu = personaje

    for personaje in personajes:

        if personaje["nombre"] != "Zenitsu Agatsuma":

            if zenitsu["atributos"]["fuerza"] > personaje["atributos"]["defensa"]:

                print(personaje["nombre"], personaje["atributos"]["fuerza"], personaje["atributos"]["defensa"])

def ejercicio6():

    for personaje in personajes[:]:

        if personaje["ocupacion"] == "Cazador de demonios":

            personajes.remove(personaje)

    for personaje in personajes:

        print(personaje)


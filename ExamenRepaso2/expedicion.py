from datos import personajes

def ejercicio1():

    lista1 = [personaje["nombre"] for personaje in personajes if personaje["afiliacion"] == "Equipo de Exploración" and personaje["vivo"] == True]

    print(lista1)

def ejercicio2():

    lista2 = [personaje["nombre"] for personaje in personajes if personaje["afiliacion"] == "Equipo Médico" and "Primeros auxilios" in personaje["habilidades"] and "Medicina" in personaje["habilidades"]]

    print(lista2)

def ejercicio3():

    lista3 = [(personaje["nombre"], personaje["afiliacion"]) for personaje in personajes if personaje["afiliacion"] != "Equipo de Exploración"]

    print(lista3)

def ejercicio4():

    lista4 = [personaje["nombre"] + " (" + personaje["afiliacion"] + ")" for personaje in personajes if personaje["registro_misiones"]["misiones_completadas"] >= 20]

    print(lista4)

def ejercicio5():

    lista5 = [(personaje["nombre"], personaje["estatura_m"] * 100) for personaje in personajes if personaje["estatura_m"] > 1.75]

    print(lista5)

def ejercicio6():

    lista6 = [habilidad for personaje in personajes for habilidad in personaje["habilidades"]]

    print(lista6)

def ejercicio7():

    lista7 = [personaje["nombre"] for personaje in personajes if personaje["registro_misiones"]["robots_solo"] + personaje["registro_misiones"]["robots_equipo"] >= 10]

    print(lista7)

def ejercicio8():

    lista8 = [{"nombre": personaje["nombre"], "robots_totales": personaje["registro_misiones"]["robots_solo"] + personaje["registro_misiones"]["robots_equipo"]} for personaje in personajes]

    print(lista8)

def ejercicio9():

    lista9 = sum([personaje["estatura_m"]  for personaje in personajes ]) / len(personajes)

    print(lista9)

def ejercicio10():

    media = sum([personaje["estatura_m"]  for personaje in personajes ]) / len(personajes)
    lista10 = [(personaje["nombre"], personaje["estatura_m"]) for personaje in personajes if personaje["estatura_m"] > media]

    print(lista10)

def ejercicio11():

    lista11 = [personaje["nombre"] for personaje in personajes if personaje["vivo"] and personaje["edad"] > 28 and personaje["afiliacion"] == "Equipo de Exploración" or personaje["afiliacion"] == "Equipo Médico"]

    print(lista11)

def ejercicio12():

    lista12 = [(personaje["nombre"], len(personaje["habilidades"])) for personaje in personajes if len(personaje["habilidades"]) >= 3 and personaje["registro_misiones"]["misiones_completadas"] > 20]
    print(lista12)


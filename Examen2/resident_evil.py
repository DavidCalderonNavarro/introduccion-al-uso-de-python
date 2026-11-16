from datos import personajes

def ejercicio1():

    lista1 = [personaje["nombre"] for personaje in personajes if personaje["afiliacion"] == "Policía de Racoon City"]

    print(lista1)

def ejercicio2():

    lista2 = [personaje["nombre"] for personaje in personajes if personaje["afiliacion"] == "Policía de Racoon City" and "Pistola Samurai Edge" in personaje["armas"] and "Lanzagranadas" in personaje["armas"]]

    print(lista2)

def ejercicio3():

    lista3 = [(personaje["nombre"], personaje["afiliacion"]) for personaje in personajes if personaje["afiliacion"] != "Policía de Racoon City"]

    print(lista3)

def ejercicio4():

    lista4 = [personaje["nombre"] + " (" + personaje["afiliacion"] + ")" for personaje in personajes if personaje["registro_misiones"]["misiones_completadas"] >= 20]

    print(lista4)

def ejercicio5():

    lista5 = [(personaje["nombre"], personaje["estatura_m"] * 100) for personaje in personajes if personaje["estatura_m"] > 1.70]

    print(lista5)

def ejercicio6():

    lista6 = [arma for personaje in personajes for arma in personaje["armas"]]

    print(lista6)

def ejercicio7():

    lista7 = [personaje["nombre"] for personaje in personajes if personaje["registro_misiones"]["zombies_solo"] + personaje["registro_misiones"]["zombies_equipo"] >= 100]

    print(lista7)

def ejercicio8():

    lista8 = [{"nombre": personaje["nombre"], "zombies_totales": personaje["registro_misiones"]["zombies_solo"] + personaje["registro_misiones"]["zombies_equipo"]} for personaje in personajes]

    print(lista8)

def ejercicio9():

    media = sum([personaje["estatura_m"] for personaje in personajes]) / len(personajes)
    
    print(media)

def ejercicio10():

    media = sum([personaje["estatura_m"] for personaje in personajes]) / len(personajes)

    lista10 = [(personaje["nombre"], personaje["estatura_m"]) for personaje in personajes if personaje["estatura_m"] > media]

    print(lista10)
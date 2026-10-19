from datos2 import personajes_frieren

for personajes in personajes_frieren:
    for afiliacion in personajes["afiliacion"]:
        if afiliacion == "Grupo de los Cuatro Héroes":
            print(personajes["nombre"], personajes["raza"], personajes["edad"])
            break
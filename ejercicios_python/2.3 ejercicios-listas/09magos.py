from datos2 import personajes_frieren

for personajes in personajes_frieren:
    for afiliacion in personajes["afiliacion"]:
        if afiliacion == "Magos de Primera Clase":
            print(personajes["nombre"], personajes["raza"])
            break
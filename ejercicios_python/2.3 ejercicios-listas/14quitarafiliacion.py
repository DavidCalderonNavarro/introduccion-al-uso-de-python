from datos2 import personajes_frieren

for personajes in personajes_frieren:
    if "Asociación Continental de Magia" in personajes["afiliacion"]:
        personajes["afiliacion"].remove("Asociación Continental de Magia")
        print(personajes)
from datos2 import personajes_frieren

for personajes in personajes_frieren:
    if personajes["raza"] == "Elfo":
        personajes["afiliacion"].append("Elfos Supervivientes del Examen de Python")
        print(personajes)
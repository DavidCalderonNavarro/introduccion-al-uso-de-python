from datos2 import personajes_frieren

for personajes in personajes_frieren:
    if personajes["raza"] == "Humano" and personajes["edad"] >= 100:
        personajes["raza"] = "Zombie"
        print(personajes)
from datos2 import personajes_frieren

for eliminados in personajes_frieren[:]:
    if eliminados["raza"] == "Demonio":
        personajes_frieren.remove(eliminados)
        print(eliminados)

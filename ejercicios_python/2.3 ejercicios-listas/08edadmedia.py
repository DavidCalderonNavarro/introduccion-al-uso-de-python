from datos2 import personajes_frieren

suma_edades = 0
n_humanos = 0

for personajes in personajes_frieren:
    if personajes["raza"] == "Humano":
        suma_edades += personajes["edad"]
        n_humanos += 1

media = suma_edades / n_humanos
print(media)
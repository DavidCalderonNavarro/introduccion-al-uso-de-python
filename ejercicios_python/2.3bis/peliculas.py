from datos import peliculas

def ejercicio1():

    nueva_pelicula = {
    "titulo": "Cars",
    "duracion": 116,
    "año_estreno": 2006,
    "edad_recomendada": 7,
    "generos": ["animación", "comedia", "aventura", "deporte", "cine familiar"]
    }

    peliculas.append(nueva_pelicula)

def ejercicio2():

    print("Ejercicio 2")

    media_duracion = 0
    contador = 0

    for peli in peliculas:
        media_duracion += peli["duracion"]
        contador += 1

    media_duracion = media_duracion / contador

    for peli in peliculas:
        if peli["duracion"] > media_duracion:
            print(peli["titulo"], peli["duracion"])

def ejercicio3():

    print("Ejercicio 3")

    for peli in peliculas:
        if "Drama" in peli["generos"]:
            peli["edad_recomendada"] = 18

def ejercicio4():

    print("Ejercicio 4")

    for peli in peliculas:
        if "Fantasía" in peli["generos"] and "Aventura" in peli["generos"]:
            print(peli["titulo"], peli["duracion"])

def ejercicio5():

    print("Ejercicio 5")

    for peli in peliculas:
        if peli["edad_recomendada"] >= 7 and peli["edad_recomendada"] <= 13:
            print(peli["titulo"], peli["edad_recomendada"])

def ejercicio6():

    print("Ejercicio 6")

    for peli in peliculas:
        if peli["edad_recomendada"] == 0:
            peli["generos"] += ["Infantil"]
            print(peli["titulo"], peli["generos"])

def ejercicio7():

    print("Ejercicio 7")

    peliculas_infantiles = []

    for peli in peliculas:
        if "Infantil" in peli["generos"]:
            peliculas_infantiles += [peli]

    print(peliculas_infantiles)

def ejercicio8():

    print("Ejercicio 8")

    for peli in peliculas[:]:
        if peli["edad_recomendada"] == 0:
            print(peli)
            peliculas.remove(peli)

from datos import series

"""
1. Muestra una lista con los títulos de las series que sean de Animación.
"""

serie1 = [serie["titulo"] for serie in series if "Animación" in serie["generos"]]

print(serie1)

"""
2. Muestra los títulos de las series que sean de Fantasía o Misterio.
"""

serie2 = [serie["titulo"] for serie in series if "Fantasía" in serie["generos"] or "Misterio" in serie["generos"]]

print(serie2)

"""
3. Muestra los títulos de las series que tengan una nota igual o superior a 9 y que
además tengan 3 o más géneros.
"""

serie3 = [serie["titulo"] for serie in series if serie["nota"] >= 9 and len(serie["generos"]) >= 3]

print(serie3)

"""
4. Muestra una lista de tuplas (titulo_serie, nota_dada) de las reseñas dejadas por el
usuario Elena.
"""

serie4 = [(serie["titulo"], reseña["nota"]) for serie in series for reseña in serie["reseñas"] if reseña["usuario"] == "Elena"]

print(serie4)

"""
5. Muestra una lista con los comentarios que tengan más de 40 caracteres.
"""

serie5 = [reseña["comentario"] for serie in series for reseña in serie["reseñas"] if len(reseña["comentario"]) > 40]

print(serie5)

"""
6. Muestra una lista de cadenas con el formato “La serie {titulo} tiene {n} reseñas”, para
todas las series.
"""

serie6 = [("La serie " + serie["titulo"] + " tiene " + len(reseña) + " reseñas") for serie in series for reseña in serie["reseñas"]]

print(serie6)

"""
7. 
"""
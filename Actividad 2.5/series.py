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

serie6 = [("La serie " + serie["titulo"] + " tiene " + str(len(reseña)) + " reseñas") for serie in series for reseña in serie["reseñas"]]

print(serie6)

"""
7. Muestra una lista de tuplas (titulo_serie, comentario) para todas las reseñas que
hayan dado una puntuación de 10.
"""

serie7 = [(serie["titulo"], reseña["comentario"]) for serie in series for reseña in serie["reseñas"] if reseña["nota"] == 10]

print(serie7)

"""
8. Muestra una lista de tuplas que incluya el título de la serie y “Obra maestra” si las
notas medias dadas en las reseñas es igual o superior a 9, y “Gran serie” en caso
contrario.
"""

serie8 = [(serie["titulo"] + ": Obra maestra") if sum(reseña["nota"] for reseña in serie["reseñas"]) / len(serie["reseñas"]) >= 9 else (serie["titulo"] + ": Gran serie") for serie in series]

print(serie8)

"""
9. Muestra una lista con todos los géneros de todas las series. No importa si hay
géneros duplicados.
"""

serie9 = [genero for serie in series for genero in serie["generos"]]

print(serie9)

"""
10. Muestra una lista con todos los nombres de los usuarios que hayan opinado en
alguna serie de Drama. No importa si hay nombres repetidos.
"""

serie10 = [reseña["usuario"] for serie in series for reseña in serie["reseñas"] if "Drama" in serie["generos"]]

print(serie10)
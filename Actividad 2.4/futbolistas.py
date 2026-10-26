from datos import jugadores

"""
1. Muestra una lista solo con los nombres de todos los futbolistas.
"""

nombres_futbolistas = [jugador["nombre"] for jugador in jugadores]

print(nombres_futbolistas)

"""
2. Muestra la lista de los jugadores que llevan el dorsal número 10.
"""

dorsal10 = [jugador for jugador in jugadores if jugador["dorsal"] == 10]

print(dorsal10)

"""
3. Muestra una lista con los nombres de los jugadores que pertenecen al "FC Barcelona".
"""

listaNombreBarcelona = [jugador["nombre"] for jugador in jugadores if jugador["equipo"] == "FC Barcelona"]

print(listaNombreBarcelona)

"""
4. Muestra una lista con los nombres de los jugadores que tienen una puntuación de pase igual o superior a 9 en sus atributos.
"""

paseMasDe9 = [jugador["nombre"] for jugador in jugadores if jugador["atributos"]["pase"] >= 9]

print(paseMasDe9)

"""
5. Muestra la lista de los jugadores que saben hacer la filigrana "ruleta".
"""

filigranaRuleta = [jugador for jugador in jugadores if "ruleta" in jugador["filigranas"]]

print(filigranaRuleta)

"""
6. Muestra una lista con los jugadores que tienen tiro >= 8 Y regate >= 9.
"""

tiroYregate = [jugador for jugador in jugadores if jugador["atributos"]["tiro"] >= 8 and jugador["atributos"]["regate"] >= 9]

print(tiroYregate)

"""
7. Crea una lista de cadenas de texto con la forma "Nombre (Equipo)" para cada jugador. Muéstrala.
"""

listaNombreEquipo = [[jugador["nombre"], jugador["equipo"]] for jugador in jugadores]

print(listaNombreEquipo)

"""
8. Crea una lista de tuplas con el nombre del jugador y el texto "Goleador" si su atributo
de tiro es mayor o igual a 9, o "Asistente" en caso contrario. Muéstrala.
"""

listaTupla = [(jugador["nombre"] + " Goleador" if jugador["atributos"]["tiro"] >= 9 else jugador["nombre"] + " Asistente") for jugador in jugadores]

print(listaTupla)

"""
9. Muestra una lista con los nombres de los jugadores que dominan más de 2 filigranas distintas.
"""

masDe2Filigranas = [jugador["nombre"] for jugador in jugadores if len(jugador["filigranas"]) > 2]

print(masDe2Filigranas)

"""
10. Extrae en una única lista todas las filigranas de todos los jugadores (no importa si
hay duplicadas) y muéstrala.
"""

todasLasFiligranas = [filigrana for jugador in jugadores for filigrana in jugador["filigranas"]]

print(todasLasFiligranas)


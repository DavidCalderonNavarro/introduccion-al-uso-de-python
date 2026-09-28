# Recorrer un rango

for i in range(1,10,2):
    print(i)
    
# Recorrer lista de elementos y diccionarios
frutas = ["Melon", "Uva", "Sandia"]

for fruta in frutas:
    print(fruta)
    
peliculas = [
    
    {"titulo " : "Resident Evil", "nota" : 6},
    {"titulo" : "Robocop", "nota" : 8},
    {"titulo" : "Terminator", "nota" : 7},
    {"titulo" : "Kárate a muerte en Torremolinos", "nota" : 5}
]

for pelicula in peliculas:
    if pelicula["nota"] >= 7:
        print(pelicula["titulo"])
        
texto = "Hola mundo"

for letra in texto:
    print(letra)
contador = 1

while contador <= 10:
    print(contador)
    contador += 1
    if contador == 5:
        break
    
animales = ["Lince iberico", "Quebrantahuesos", "Cabra montesa"]

while animales:
    animal = animales.pop(0)
    print(animal)
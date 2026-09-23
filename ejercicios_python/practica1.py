lista1 = ["Manzana", "Pera", "Melocotón"]

lista2 = ["Kiwi", "Sandía", "Melón"]

lista1.extend(lista2)

print(lista1[-1])

tupla = (3,5,7)

print(tupla[0])

inicio = int(input("Inicio: "))
fin = int(input("Final: "))
salto = int(input("Saltos: "))

rango = range(inicio, fin, salto)
print(rango)


class Personaje:

    def __init__ (self, vida: int, ataque: int):

        if vida <= 0 or ataque <= 0:
            raise ValueError("La vida y el ataque no puede ser negativo")

        self.vida = vida
        self.ataque = ataque

    def recibir_dano (self, cantidad: int):

        self.vida = max(0, self.vida - cantidad)

    def atacar (self, objetivo: Personaje):

        objetivo.recibir_dano(self.ataque)

class Guerrero(Personaje):

    def atacar(self, objetivo: Personaje):

        objetivo.recibir_dano(self.ataque * 2)

class Mago(Personaje):

    def __init__ (self, vida: int, ataque: int, mana: int):

        super().__init__(vida, ataque)
        self.mana = mana

    def atacar(self, objetivo: Personaje):

        #   El mago solo puede atacar con magia si solo tiene 5 de mana o mas, si no hace un ataque normal
        #   Si tiene mana triplica su ataque

        if self.mana >= 5:

            objetivo.recibir_dano(self.ataque * 3)
            self.mana -= 5

        else:

            objetivo.recibir_dano(self.ataque)

goku = Guerrero(100, 20)
ryu = Personaje(80, 30)
pepe = Mago(50, 20, 15)

goku.atacar(ryu)
ryu.atacar(goku)
pepe.atacar(goku)

print(goku.vida)
print(ryu.vida)
print(pepe.mana)
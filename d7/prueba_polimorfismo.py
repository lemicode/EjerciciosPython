palabra = "polimorfismo"
lista = ["Clases", "POO", "Polimorfismo"]
tupla = (1, 2, 3, 80)
for objeto in [palabra, lista, tupla]:
    print(len(objeto))


class Mago:
    def atacar(self):
        print("Ataque mágico")


class Arquero:
    def atacar(self):
        print("Lanzamiento de flecha")


class Samurai:
    def atacar(self):
        print("Ataque con katana")


persona1 = Arquero()
persona2 = Mago()
persona3 = Samurai()
personajes = [persona1, persona2, persona3]
for guerrero in personajes:
    guerrero.atacar()


class Mago():
    def defender(self):
        print("Escudo mágico")


class Arquero():
    def defender(self):
        print("Esconderse")


class Samurai():
    def defender(self):
        print("Bloqueo")


def personaje_defender(personaje):
    personaje.defender()

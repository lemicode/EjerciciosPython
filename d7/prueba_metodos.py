class Perro:
    def ladrar(self):
        print('Guau!')


mateo = Perro()
mateo.ladrar()


class Mago:
    def lanzar_hechizo(self):
        print("¡Abracadabra!")


merlin = Mago()
merlin.lanzar_hechizo()


class Alarma:
    def postergar(self, cantidad_minutos):
        print(f"La alarma ha sido pospuesta {cantidad_minutos} minutos")

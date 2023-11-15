class Mascota:
    @staticmethod
    def respirar():
        print("Inhalar... Exhalar")


class Jugador:
    vivo = False

    @classmethod
    def revivir(cls):
        cls.vivo = True


class Personaje:
    def __init__(self, cantidad_flechas):
        self.cantidad_flechas = cantidad_flechas

    def lanzar_flecha(self):
        self.cantidad_flechas -= 1

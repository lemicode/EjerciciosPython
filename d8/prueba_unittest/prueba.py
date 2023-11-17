import cambiar_texto
import unittest


class Probar(unittest.TestCase):

    # Importante que comience con la palabra 'test'
    def test_cambiar_mayusculas(self):
        resultado_funcion = cambiar_texto.mayusculas('hola')
        # El tercer parámetro (mensaje) es opcional
        self.assertEqual('HOLA', resultado_funcion, 'El resultado de la función no coincide con lo esperado')


# Importante
if __name__ == '__main__':
    unittest.main()

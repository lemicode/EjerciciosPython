"""
MacOS no reconocía el comando pip. Se solucionó así: python3 -m pip install --upgrade pip
Comando para la instalación de pylint: pip install pylint
Ejecución de pylint para este caso: pylint prueba_pylint.py -r y


Código original para analizar:
-----------------------------
def Sumar(número1, número2):
    return número1+número2

suma = Sumar(5,7)
print(suma)
-----------------------------


El siguiente código junto con este mensaje contienen las mejoras sugeridas por pylint.
Aunque algunas no fueron necesarias pero igual se implementaron.
Puntuación de pylint: 7.5/10 (A partir de 7 es aceptable).

Para desactivar mensajes de pylint en el reporte se crea un comentario, así:
    # pylint: disable=invalid-name
Pero no se recomienda, es mejor seguir las buenas prácticas de PEP-8 o solucionar los errores.
"""


def add(number_1: int, number_2: int) -> int:
    """
    This function takes two numbers as parameters and returns their sum

    :param number_1: (int) First number to add
    :param number_2: (int) Second number to add
    :return: (int) The sum of number_1 and number_2
    """
    return number_1 + number_2


addition = add(5, 7)
print(addition)

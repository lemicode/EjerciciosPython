"""
import time


def prueba_for(numero):
    lista = []
    for num in range(1, numero + 1):
        lista.append(num)
    return lista


def prueba_while(numero):
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista


# Forma con menor precisión para ciertos casos, por ejemplo
# acá si se pasa el parámetro 10 los valores no son fiables
# mientras en con 100.000 sí.


inicio = time.time()
prueba_for(100000)
final = time.time()
print(final - inicio)

inicio = time.time()
prueba_while(100000)
final = time.time()
print(final - inicio)

"""

# Otra forma un poco mejor

import timeit

declaracion1 = '''
prueba_for(10)
'''

setup1 = '''
def prueba_for(numero):
    lista = []
    for num in range(1, numero + 1):
        lista.append(num)
    return lista
'''

duracion1 = timeit.timeit(declaracion1, setup1, number=1000000)
print(duracion1)

declaracion2 = '''
prueba_while(10)
'''

setup2 = '''
def prueba_while(numero):
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista
'''
duracion2 = timeit.timeit(declaracion2, setup2, number=1000000)
print(duracion2)

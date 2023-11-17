def suma_infinita():
    x = 0
    while True:
        x += 1
        yield x


generador = suma_infinita()
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))


def multiplos_siete():
    i = 1
    while True:
        yield 7 * i
        i += 1


generador2 = multiplos_siete()
print(next(generador2))
print(next(generador2))
print(next(generador2))
print(next(generador2))
print(next(generador2))
print(next(generador2))
print(next(generador2))
print(next(generador2))


def contar_vidas():
    for mensaje in ["Te quedan 3 vidas", "Te quedan 2 vidas", "Te queda 1 vida", "Game Over"]:
        yield mensaje


perder_vida = contar_vidas()
print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))


def validar_iteracion():
    yield 111
    yield 222
    yield 333

iteracion = validar_iteracion()
print(next(iteracion))
print(next(iteracion))
print(next(iteracion))
print(next(iteracion)) # Aquí se genera un error voluntario como parte de la validación

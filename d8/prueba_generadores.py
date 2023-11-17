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

def decorador_turno(generar_turno, area):
    def nueva_funcion():
        print(f'\nSu turno para la {area} es: {next(generar_turno)}')
    return nueva_funcion


def generar_turno_perfumeria():
    i = 0
    while True:
        i += 1
        yield 'P-' + str(i)


def generar_turno_farmacia():
    i = 0
    while True:
        i += 1
        yield 'F-' + str(i)


def generar_turno_cosmetica():
    i = 0
    while True:
        i += 1
        yield 'C-' + str(i)

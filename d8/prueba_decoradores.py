def decorar(funcion):
    def otra_funcion(palabra):
        print('El nuevo texto es el siguiente:')
        funcion(palabra)
        print('Eso fue todo!')
    return otra_funcion

# Primera forma


@decorar
def mayusculas(texto):
    print(texto.upper())


@decorar
def minusculas(texto):
    print(texto.lower())


minusculas('HOLA')

# Segunda forma


def mayusculas2(texto):
    print(texto.upper())


def minusculas2(texto):
    print(texto.lower())


mayusculas2_decorada = decorar(mayusculas2)
mayusculas2_decorada('hola')

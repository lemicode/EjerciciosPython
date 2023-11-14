def suma_cuadrados(*args):
    return sum([num**2 for num in args])

def suma_absolutos(*args):
    return sum(map(abs, args))

def numeros_persona(nombre, *args):
    return f'{nombre}, la suma de tus números es {sum(args)}'
def cantidad_atributos(**kwargs):
    return len(kwargs)
print(cantidad_atributos(a = 2, b=4))

def lista_atributos(**kwargs):
    return list(kwargs.values())
print(lista_atributos(a=1, b=22))

def describir_persona(nombre, **kwargs):
    print(f"Características de {nombre}:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

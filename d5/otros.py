def devolver_distintos(*args):
    """
    Esta función devuelve el número máximo, menor o intermedio conforme a las validaciones
    :param args:
    :return:
    """
    suma = sum(args)
    lista = list(args)
    if suma > 15:
        return max(args)
    elif suma < 10:
        return min(args)
    else:
        lista.sort()
        return lista[1]
print(devolver_distintos(7, 4, 3))

def ordenar_sin_duplicados(palabra: str):
    return sorted(list(set(palabra)))
print(ordenar_sin_duplicados('ccbbaad'))

def validar_ceros(*args):
    if args.count(0) >= 2:
        return True
    else:
        return False
print(validar_ceros(1,0,2,0))

def contar_primos(num_max):
    lista = range(2, num_max + 1)
    primos = list(lista)
    for num in lista:
        i = 2
        multiplo = 2
        while multiplo <= num_max:
            multiplo = num * i
            if multiplo in primos:
                primos.remove(multiplo)
            i += 1
    print(f"Lista de números primos: {primos}")
    return len(primos)
print(f"Cantidad total de números primos: {contar_primos(10)}")

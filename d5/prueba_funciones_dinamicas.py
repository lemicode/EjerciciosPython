def todos_positivos(lista):
    for num in lista:
        if num < 0:
            return False
    return True
lista_numeros = [-1, 2, 3, -4]

def suma_menores(lista):
    suma = 0
    for num in lista:
        if num > 0 and num < 1000:
            suma += num
    return suma
lista_numeros = [-1, 50, 5, 1500]

def cantidad_pares(lista):
    conteo = 0
    for num in lista:
        if num % 2 == 0:
            conteo += 1
    return conteo
lista_numeros = [2, 4, 3, 9, 10]

from random import randint, choice

def lanzar_dados():
    dado1 = randint(1, 6)
    dado2 = randint(1, 6)
    return (dado1, dado2)
dado1, dado2 = lanzar_dados()
def evaluar_jugada(dado1, dado2):
    suma_dados = dado1 + dado2
    mensaje = ""
    if suma_dados <= 6:
        mensaje = f"La suma de tus dados es {suma_dados}. Lamentable"
    elif suma_dados > 6 and suma_dados < 10:
        mensaje = f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
    else:
        mensaje = f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"
    return mensaje

def reducir_lista(lista):
    lista_nueva = set(lista)
    numero_maximo = max(lista)
    lista_nueva.remove(numero_maximo)
    return list(lista_nueva)
lista_numeros = [1, 2, 3, 4, 4, 5]
lista_final = reducir_lista(lista_numeros)
def promedio(lista):
    suma = sum(lista)
    conteo = len(lista)
    return suma / conteo

def lanzar_moneda():
    moneda = ['Cara', 'Cruz']
    return choice(moneda)
lista_numeros = [1, 2, 3, 4]
moneda = lanzar_moneda()
def probar_suerte(moneda, lista):
    if moneda == 'Cara':
        print("La lista se autodestruirá")
        return []
    else:
        print( "La lista fue salvada")
        return lista

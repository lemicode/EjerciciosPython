from collections import Counter, defaultdict, deque

lista = [1, 2, 3, 6, 7, 1, 2, 4, 5, 5, 5, 5, 3, 2, 6, 7]
contador = Counter(lista)

mi_diccionario = defaultdict(lambda: "Valor no hallado")
mi_diccionario['edad'] = '44'
print(mi_diccionario['peso'])

# Estructura de datos también conocida como "cola de dos extremos"
lista_ciudades = deque(["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"])
lista_ciudades.append('derecha')
lista_ciudades.appendleft('izquierda')
print(lista_ciudades)

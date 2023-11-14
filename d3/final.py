texto = input("Ingrese el texto de su elección: ")
letras = []
texto = texto.lower()
letras.append(input("Ingrese la 1ra. letra: ").lower())
letras.append(input("Ingrese la 2da. letra: ").lower())
letras.append(input("Ingrese la 3ra. letra: ").lower())

print("\n")
print("CANTIDAD DE LETRAS")
cantidad_letra1 = texto.count(letras[0])
cantidad_letra2 = texto.count(letras[1])
cantidad_letra3 = texto.count(letras[2])
print(f"La letra '{letras[0]}' se encuentra repetidad {cantidad_letra1} veces en el texto.")
print(f"La letra '{letras[1]}' se encuentra repetidad {cantidad_letra2} veces en el texto.")
print(f"La letra '{letras[2]}' se encuentra repetidad {cantidad_letra3} veces en el texto.")

print("\n")
print("CANTIDAD DE PALABRAS")
palabras = texto.split()
print(f"El texto contiene {len(palabras)} palabras.")

print("\n")
print("LETRAS DE INICIO Y DE FIN")
letra_inicial = texto[0]
letra_final = texto[-1]
print(f"La letra inicial del texto es {letra_inicial} y la letra final es {letra_final}")

print("\n")
print("TEXTO INVERTIDO")
palabras.reverse()
texto_invertido = ' '.join(palabras)
print(f"El texto invertido es: '{texto_invertido}'")

print("\n")
print("BUSCANDO LA PALABRA PYTHON")
busqueda = 'python' in texto
dic = {True: 'sí', False: 'no'}
print(f"La palabra 'python' {dic[busqueda]} se encuentra.")

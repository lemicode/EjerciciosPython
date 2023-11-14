texto = open('texto.txt')
print(texto.read())
texto.close()

texto = open('texto.txt')
print(texto.readline())
texto.close()

texto = open('texto.txt')
print(texto.readlines()[1])
texto.close()

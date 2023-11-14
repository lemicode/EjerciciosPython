numero = 10
while numero >= 0:
    print(numero)
    numero -= 1

numero = 50
while numero >= 0:
    if numero % 5 == 0:
        print(numero)
    else:
        numero -= 1
        continue
    numero -= 1

lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]
for num in lista_numeros:
    if num < 0:
        break
    else:
        print(num)

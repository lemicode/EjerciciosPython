from random import randint

print('\nAdivina un número entero entre 1 y 100. Tienes 8 intentos.')
vidas = 0
num_ganador = randint(1, 100)
while vidas < 8:
    print(f'\nOPORTUNIDAD No. {vidas + 1}')
    num = int(input('Ingresa un número: '))
    if num not in range(1, 101):
        print('El número que ingresaste está fuera del rango.')
    elif num > num_ganador:
        print('El número que ingresaste es mayor al número ganador')
    elif num < num_ganador:
        print('El número que ingresaste es menor al número ganador')
    elif num == num_ganador:
        print(f'Adivinaste, el número ganador es {num_ganador}')
        break
    vidas += 1
mensaje = '\nJuego finalizado. '
if vidas == 8:
    mensaje += f'El número ganador era {num_ganador}.'
print(mensaje)

from random import choice
from os import system


def jugar_ahorcado():
    """
    Función para incializar el juego
    :return None:
    """
    seguir_jugando = True
    while seguir_jugando:
        lista_palabras = ["ajedrez", "telefono", "casa", "futbol", "cafe", "carro", "computador", "manzana", "naranja"]
        palabra = choice(lista_palabras)
        palabra_oculta, acierto = renderizar_palabra(palabra)
        longitud_palabra = len(palabra)
        vidas = longitud_palabra
        letras_erradas = []
        print('\n' + '*' * 20)
        print("JUEGO DEL AHORCADO")
        print('*' * 20 + '\n')
        print(f"La palabra oculta es: {palabra_oculta} (Tiene {longitud_palabra} caracteres)")
        while vidas > 0 and '-' in palabra_oculta:
            print(f'\nNo. de vidas: {vidas}')
            letra = input("Ingresa una letra: ")
            es_string = validar_string(letra)
            if not es_string:
                continue
            else:
                if letra in palabra_oculta:
                    print(f"Ya se encuentra esa letra: {palabra_oculta}")
                else:
                    palabra_oculta, acierto = renderizar_palabra(palabra, letra, palabra_oculta)
                    if not acierto:
                        vidas -= 1
                        letras_erradas.append(letra)
                        letras_erradas = list(set(letras_erradas))
                        print(f"Te equivocaste. Letras fallidas: {', '.join(letras_erradas)}")
                        if vidas == 0:
                            # system('cls') # clean screen
                            print(f'Se te acabaron las oportunidades, la palabra era: {palabra}')
                    else:
                        print(f'Acertaste: {palabra_oculta}')
                    if not '-' in palabra_oculta:
                        print(f'¡Ganaste, felicitaciones!')
        salir = input('\nSi deseas salir del juego ingresa la palabra "exit". De lo contrario presiona Enter: ')
        if salir == 'exit':
            seguir_jugando = False


def renderizar_palabra(palabra: str, letra: str = '', palabra_oculta: str = '') -> tuple:
    """
    Función que estructura la palabra con los campos ocultos, así como los aciertos
    :param palabra:
    :param letra:
    :param palabra_oculta:
    :return tuple:
    """
    acierto = letra in palabra
    contador = 0
    nueva_construccion = ''
    while contador < len(palabra):
        if letra == palabra[contador]:
            nueva_construccion += letra
        else:
            if len(palabra_oculta) > 0:
                nueva_construccion += palabra_oculta[contador]
            else:
                nueva_construccion += '-'
        contador += 1
    return nueva_construccion, acierto


def validar_string(letra: str) -> bool:
    """
    Función que valida el texto ingresado por el usuario
    :param letra:
    :return bool:
    """
    try:
        int(float(letra))
        return False
    except:
        if len(letra) != 1:
            return False
        return True


jugar_ahorcado()

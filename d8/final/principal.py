from numeros import generar_turno_perfumeria, generar_turno_farmacia, generar_turno_cosmetica, decorador_turno
import textwrap
from os import system


def iniciar_programa_turnos():
    try:
        turno_perfumeria = generar_turno_perfumeria()
        turno_farmacia = generar_turno_farmacia()
        turno_cosmetica = generar_turno_cosmetica()
        while True:
            system('clear')
            print(textwrap.dedent('''
                
                ***********
                Bienvenido!
                ***********
                
                Áreas Comerciales:
                
                [1] Perfumería
                [2] Farmacia
                [3] Cosmética
                 
            '''))
            numero_area = int(input('Por favor ingrese un número de Área: '))
            match numero_area:
                case 1:
                    turno = decorador_turno(turno_perfumeria, 'Perfumería')
                case 2:
                    turno = decorador_turno(turno_farmacia, 'Farmacia')
                case 3:
                    turno = decorador_turno(turno_cosmetica, 'Cosmética')
                case _:
                    input('\nEse número de Área no existe. Presione Enter para elegir nuevamente.')
                    continue
            turno()
            input('\nPresione Enter para obtener otro turno o finalizar.')
    except:
        iniciar_programa_turnos()


iniciar_programa_turnos()

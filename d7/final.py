import textwrap
from random import randint
from os import system

class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):
    numero_cuenta = randint(1000000000000, 9999999999999)
    balance = 0

    def __str__(self):
        return textwrap.dedent(f'''
            Bienvenido {self.nombre} {self.apellido}!
            
            A continuación se muestran sus datos bancarios:
             
             - Número de cuenta: {self.numero_cuenta}
             - Balance: {self.balance} 
        ''')

    def depositar(self):
        monto = int(input('Ingrese el monto que desea depositar: '))
        self.balance = int(self.balance) + monto
        self.mostrar_nuevo_balance()

    def retirar(self):
        monto = int(input('Ingrese el monto que desea retirar: '))
        if monto > self.balance:
            print('\nEl monto supera el balance de su cuenta.')
        else:
            self.balance = self.balance - monto
            self.mostrar_nuevo_balance()


    def mostrar_nuevo_balance(self):
        print(f'\nSu nuevo balance es {self.balance}.')

    def seleccionar_operacion(self):
        print(textwrap.dedent('''
            Operaciones Disponibles:

            [1] Depositar
            [2] Retirar
            [3] Salir
        '''))
        opcion = input('Ingrese el número de la operación que desea realizar: ')
        if opcion == '1':
            self.depositar()
        elif opcion == '2':
            self.retirar()
        elif opcion == '3':
            print('')
            exit()
        else:
            self.seleccionar_operacion()


def crear_cliente():
    nombre = input('Ingrese su primer nombre: ')
    apellido = input('Ingrese su primer apellido: ')
    cliente = Cliente(nombre, apellido)
    return cliente


def iniciar_cajero():
    system('clear')  # Para Windows usar 'cls'
    print ('*' * 17)
    print('Cajero Automático')
    print('*' * 17 + '\n\n')
    cliente = crear_cliente()
    salir = False
    while not salir:
        system('clear')
        print(cliente)
        cliente.seleccionar_operacion()
        if input('\nPara salir ingrese "Y", de lo contrario presione Enter: ').lower() == 'y':
            salir = True
            print('')


iniciar_cajero()

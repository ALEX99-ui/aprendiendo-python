from os import system

class Persona:

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return f'Nombre: {self.nombre}, Apellido: {self.apellido}'

class Cliente(Persona):

    def __init__(self, nombre, apellido, numero_cuenta, balance):
        super().__init__(nombre, apellido)                          #llamada al constructor de la clase padre
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        # Llama al __str__ de la clase padre para obtener su representación y añade la del hijo
        return f'{super().__str__()}, Numero cuenta: {self.numero_cuenta}, Balance: {self.balance}'


    def depositar(self):
        deposito = int(input('Ingrese la cifra a depositar: '))
        self.balance = self.balance + deposito


    def retirar(self):
        retiro = int(input('Ingrese la cifra a retirar: '))

        if self.balance - retiro < 0:
            print('No tienes suficientes fondos.')

        else:
            self.balance = self.balance - retiro
            print(f'Tu saldo final es: {self.balance}')




def crear_cliente():
    nombre = str(input('Ingrese su nombre: '))
    apellido = str(input('Ingrese su apellido: '))
    numero_cuenta = int(input('Ingrese su numero de cuenta: '))
    balance_inicial = int(input('ingrese el balance incial en su cuenta: '))
    return nombre, apellido, numero_cuenta, balance_inicial

def inicio():
    system('cls')
    eleccion = 'x'
    while not eleccion.isnumeric() or int(eleccion) not in range(1,4):
        print('Elige una opcion:')
        print('''
        [1] - Depositar
        [2] - Retirar
        [3] - Salir
        ''')
        eleccion = input()
    return int(eleccion)




parameters = crear_cliente()
cliente1 = Cliente(parameters[0], parameters[1], parameters[2], parameters[3])




while True:

    menu = inicio()
    system('cls')
    if menu == 1:
        cliente1.depositar()
        print(f'Su balance final es: {cliente1.balance}')

    elif menu == 2:
        cliente1.retirar()

    elif menu == 3:
        break




from random import *

nombre = input("Cual es tu nombre: ")
print(f'Bueno,{nombre}, he pensado un número entre 1 y 100, y tienes solo ocho intentos para adivinar cuál crees que es el número')

numero_pensado = randint(1, 100)
numero_usuario = 0
intentos = 0
max_intentos = 8

while numero_usuario != numero_pensado and intentos < max_intentos:
    intentos += 1
    numero_usuario = int(input('Ingrese un número: ',))
    if numero_usuario < 1 or numero_usuario > 100:
        print(f'El {numero_usuario} no esta permitido')
    elif numero_usuario < numero_pensado:
        print(f'El {numero_usuario}  es menor que el número pensado por la computadora.')
    elif numero_usuario > numero_pensado:
        print(f'El número que has ingresado es mayor que el número pensado por la computadora.')
    else:
        print(f'El número que has ingresado es igual al pensado por la computadora.')

if numero_usuario == numero_pensado:
    print(f"¡Felicidades! Has adivinado el número en {intentos} intentos.")
else:
    print(f"Lo siento, has alcanzado el límite de {max_intentos} intentos. El número que pensó la computadora era: {numero_pensado}")




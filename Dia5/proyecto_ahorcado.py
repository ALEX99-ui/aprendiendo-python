from random import choice, random

# inicio juego

def inicio_juego():
    print("******************************************")
    print("*                                        *")
    print("*          ¡Bienvenido al Ahorcado!      *")
    print("*                                        *")
    print("******************************************")
    print("\nInstrucciones:")
    print("1. Adivina la palabra secreta letra por letra.")
    print("2. Tienes un número limitado de intentos.")
    print("3. Cada letra incorrecta te acerca un paso más a ser 'ahorcado'.")
    print("4. La temática son: Animales")
    print("4. ¡Buena suerte!\n")

# lista de palabras para jugar 

def palabras_azar():
    lista = ['perro', 'gato', 'caballo', 'burro', 'elefante', 'avestruz', 'tigre', 'aguila', 'buho', 'jirafa','delfin',
            'zorro', 'oso', 'rinoceronte', 'mono', 'gorila', 'camello']
    palabra = choice(lista)
    return palabra

# convertir palabra a guiones bajos 

palabra_elegida = palabras_azar()
n_letras = len(palabra_elegida)

def guiones():

    guion = ''
    contador = 0

    while contador < n_letras:
        guion += '_'
        contador += 1
    return str(guion)


# pedir al usuario que elija una letra 

def validacion(letra_elegida):

    comprobar = True

    while comprobar == True:
        
        if letra_elegida.isalpha():
            
            print('si es valida')

        else:
            print('No es una letra valida, intentalo de nuevo.')

        print("quiere seguir jugando")

        pregunta = input()

        if(pregunta == 's'):
            continue
        else:
            comprobar = False

    




print(inicio_juego())
print('Tú palabra secreta es: ', guiones() )
letra_elegida = str(input('Escoge una letra: '))
print(validacion(letra_elegida))




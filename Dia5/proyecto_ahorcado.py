from random import choice, random
def palabras_azar():
    lista = ['perro', 'gato', 'caballo', 'burro']
    palabra = choice(lista)
    return palabra

palabra_elegida = palabras_azar()
def espacios(palabra_elegida):

    string = '_'

    for letra in palabra_elegida:
        string = string + letra + '_'


    return string

palabra_oculta = espacios(palabra_elegida)
print(palabras_azar())
print(palabra_oculta)

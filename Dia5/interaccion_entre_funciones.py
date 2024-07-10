from random import shuffle

# Lista Inicial
palitos = ['-', '--', '---', '----']

# Mezclar palitoa
def mezclar(lista):
    shuffle(lista)
    return lista

# Pedirle intento
def probar_suerte():
    intento = ''

    while intento not in ['1', '2', '3', '4']:
        intento = input('elige un numero del 1 al 4: ')

    return int(intento)

# Comprobar intento
def chequear_intento(lista,intento):
    if lista[intento - 1] == '-':
        print('a lavar los platos')
    else:
        print('esta vez te has salvado')

    print(f'te ha tocado el palito {lista[intento-1]}')


palitos_mezclados = mezclar(palitos)
seleccion = probar_suerte()
chequear_intento(palitos_mezclados,seleccion)

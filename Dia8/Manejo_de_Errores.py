def suma():
    n1 = int(input('numero 1: '))
    n2 = int(input('numero 2: '))
    print(n1 + n2)
    print('gracias por sumar')

try:
    # codigo que queremos probar
    suma()

except TypeError:
    # codigo a ejecutar si no hay un error

    print('estas intentado concatenar tipos distintos')

except ValueError:
    print('ese no es numero')

else:
    # codigo a ejecutar si no hay un error
    print('hiciste todo bien')

finally:
    # codigo que se va a ejecutar de todos modos

    print('eso fue todo')


# ejercicio
def pedir_numero():

    while True:
        try:
            numero = int(input('dame un numero: '))
        except:
            print('ese no es un numero')
        else:
            print(f'ingresaste el numero {numero}')
            break

    print('gracias')

pedir_numero()
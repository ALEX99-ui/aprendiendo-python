import random

def lanzar_moneda():
    moneda = ['Cara', 'Cruz']
    resultado = random.choice(moneda)
    return resultado

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def probar_suerte(resultado, lista_numeros):
    if resultado == 'Cara':
        print('La lista se autodestruirá')
        lista_numeros.clear()
        return lista_numeros
    else:
        print('La lista fue salvada')
        return lista_numeros

resultado = lanzar_moneda()
final = probar_suerte(resultado, lista_numeros)
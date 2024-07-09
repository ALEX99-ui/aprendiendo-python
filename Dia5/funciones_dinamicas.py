def chequear_3_cifras(numero):
    return numero in range(100, 1000)

resultado = chequear_3_cifras(520)
print(resultado)

# ejemplo
def chequear_cifras(lista):

    lista_3_cifras = []

    for n in lista:
        if n in range(100, 1000):
            return True
        else:
            pass

resultado1 = chequear_cifras([55,99,6000])
print(resultado1)

# practica
def todos_positivos(lista_numeros):
    for n in lista_numeros:
        if n > 0:
            pass
        else:
            return False
    return True

lista_numeros = [1, -50, 502, -5000, 755, 600, 33, 61]

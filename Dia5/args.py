# ejemplo
def suma(*args):
    total = 0

    for arg in args:
        total += arg
    return total

print(suma(5,6,8,200,8,15,20))


#manera mas corta
def suma2(*args):
     return sum(args)

print(suma2(5,6,12,15))

#practica 2
def suma_absolutos(*args):
    total = 0

    for arg in args:
        if arg < 0:
            total += arg * -1
        else:
            total += arg
            print(total)
    return total

suma_absolutos(1, 2, 3)

#practica 3
def numeros_persona(nombre, *args):
    suma_numeros = 0
    for arg in args:
        suma_numeros += arg

    return (f'{nombre}, la suma de tus números es {suma_numeros}')
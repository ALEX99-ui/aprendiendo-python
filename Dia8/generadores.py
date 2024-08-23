def mi_generador():
    x = 1
    yield x

    x += 1
    yield x

    x += 1
    yield x


g = mi_generador()
print(next(g))
print(next(g))
print(next(g))

#ejercicio
def mi_generador():
    x = 0  # Iniciar desde 0
    while True:
        yield x
        x += 1

generador = mi_generador()

print(next(generador))  # Esto imprimirá 1

# ejercicio 2
def multiplicacion():
    x = 0
    while True:
        mult = x + 7
        yield mult
        x = mult

generador = multiplicacion()

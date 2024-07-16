def ceros_vecinos(*args):

    contador = 0

    for n in args:

        if args[contador] == 0 and args[contador + 1] == 0:
            return True

        else:
            contador += 1
    return False

print(ceros_vecinos(1,2,3,4,5,6,0,0))
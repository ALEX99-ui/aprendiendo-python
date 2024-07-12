def veces_consecutivas(*args):

    for arg in range(len(args) - 1):
        if args[arg] == args[arg+1]:
            return True
    return False

resultado = veces_consecutivas(1,2,0,0,4,5,6)
print(resultado)
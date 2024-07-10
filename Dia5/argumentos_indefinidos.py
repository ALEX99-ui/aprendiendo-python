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
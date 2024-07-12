def suma(**kwargs):

    total = 0

    for clave,valor in kwargs.items():
        print(f'{clave} = {valor}')
        total += valor
    return total

print(suma(x=3, y=4, z=5))

#ejemplo
def prueba(num1, num2, *args, **kwargs):

    print(f'el primer valor es {num1}')
    print(f'el segundo valor es {num2}')

    for arg in args:
        print(f'arg = {arg} ')

    for clave,valor in kwargs.items():
        print(f'{clave} = {valor}')


args = [100,200,300,500]
kwargs = {'x':'uno', 'y':'dos', 'z':'tres'}

prueba(15,50, *args, **kwargs)

#practica 1
def cantidad_atributos(**kwargs):
    return len(kwargs)

# practica 2
def lista_atributos(**kwargs):
    return list(kwargs.values())

valores_atributos = lista_atributos(attr1='valor1', attr2='valor2', attr3='valor3')

print(valores_atributos)

#practica 3
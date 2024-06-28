lista = ['a', 'b', 'c']
for letra in lista:
    numero_letra = lista.index(letra) + 1
    print(f'letra {numero_letra}: {letra}')

#ejemplo
lista = ['pablo', 'laura', 'fede', 'luis', 'julia']
for nombre in lista:
    if nombre.startswith('l'):
        print(nombre)
    else:
        print('nombre que no comienza con L')

#ejemplo 2
numeros = [1, 2, 3, 4, 5]
mi_valor = 0

for numero in numeros:
    mi_valor = mi_valor + numero
    print(mi_valor)

#ejemplo 3
palabra = 'python'

for letra in palabra:
    print(letra)

#ejemplo 4
for a,b in [[1,2],[3,4]]:
    print(a)
    print(b)

#ejemplo 4
dic = {'clave1':'a','clave2':'b','clave3':'c'}

for item in dic.items()
    print(item)
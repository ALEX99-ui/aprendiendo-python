lista = ['a','b','c','d']
indice = 0

for item in lista:
    print(indice,item)
    indice += 1

#manera mas limpia de hacerlo
lista1 = ['a','b','c','d']

for item in enumerate(lista1):
    for i in item:
        print(i)
    print(item)

#ejemplo
lista2 = ['a','b','c','d']

mis_tuples = list(enumerate(lista2))
print(mis_tuples[1][0])

#practica 1 enumerador
lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for indice,nombre in enumerate(lista_nombres):

    print(f'{nombre} se encuentra en el índice {indice}')

#practica 2 enumerador
cadena = 'Python'

lista_indices = [(indice, caracter) for indice, caracter in enumerate(cadena)]
print(lista_indices)

#practica 3 enumerador
lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

# Iteramos sobre la lista utilizando enumerate para obtener índices y nombres
for indice, nombre in enumerate(lista_nombres):
    # Verificamos si el nombre empieza con 'M'
    if nombre.startswith('M'):
        # Imprimimos el índice
        print(indice)


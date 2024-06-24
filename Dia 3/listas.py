mi_lista = ['a', 'b', 'c']
mi_lista2 = ['d', 'e', 'f']

#concatenacion
mi_lista3 = mi_lista + mi_lista2
#agrega elementos a la lista
mi_lista3.append('g')

#elimina elementos de la lista
mi_lista3.pop() #elimina el ultimo elemento de la lsta cuando los () estan vacios, púedo usar la funcion dentro de otra variable

eliminado = mi_lista3.pop()

print(eliminado)
print(mi_lista3)

#ordenar elementos de una lista
lista = ['g','o','b','m','c']

# sort sirve para ordenar los elementos dentro de una lista
lista.sort()

#reverse es un comando que pone lo ultimo de primero
lista.reverse()
print( nueva_lista)
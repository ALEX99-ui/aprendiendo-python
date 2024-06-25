mi_set = set([1,2,3,4,5,6,7,8,9,10])
print(mi_set)

#sin usar la palabra set
otro_set = {1,2,3,4,5,6,7,8,9,10}
print(otro_set)

#usando el cmd len para conocer el largo de la funcion
mi_set1 = set([1,2,3,4,5,6,7,8,9,10])
print(len(mi_set1))

#hacer consultas del set
mi_set2 = set([1,2,3,4,5,6,7,8,9,10])
print(2 in mi_set2)

#union de sets
s1 = {1,2,3}
s2 = {4,5,6}
s3 = s1.union(s2)
print(s3)

#metodo add para agregar elementos
set1 = {1,2,3}

set1.add(4)
print(set1)

#eliminar usando .remove()
set2 = {1,2,3,4,5,6,7,8,9,10}
set2.remove(4)
print(set2)

#metodo .pop() elimina cualquiera de los elementos si lo dejo vacio
set3 = {1,2,3,4,5,6,7,8,9,10}
sorteo = set3.pop()
print(sorteo)

#metodo .clear() si se deja vacio se limpia todo dentro del set
set4 = {1,2,3,4,5,6,7,8,9,10}
set4.clear()
print(set4)

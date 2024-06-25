#anidar
mi_tuple = (1,2,(10,20),3,4)
print(mi_tuple[2][0])

#haciendo castings
mi_tuple = list(mi_tuple)
print(type(mi_tuple))

# Definir una tupla
mi_tupla = (1, 2, 2, 3, 4, 2, 5, 2)

# Contar la cantidad de veces que aparece el valor 2 en la tupla
cantidad = mi_tupla.count(2)

print(cantidad)

# convertir una tupla en lista ejercicio
mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2)
mi_lista = list(mi_tupla)
print(mi_lista)

#extraer  elementos de una tupla en 4 variables
mi_tupla = (1, 2, 3, 4)

a = mi_tupla[0]
b = mi_tupla[1]
c = mi_tupla[2]
d = mi_tupla[3]

print(a, b, c, d)
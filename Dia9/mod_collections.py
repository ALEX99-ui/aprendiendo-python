from collections import namedtuple

Persona = namedtuple('Persona', ['nombre', 'altura', 'peso'])
ariel = Persona('Ariel', 1.76, 79)
print(ariel.peso)


# ejemplo 2
from collections import defaultdict

mi_dic = defaultdict(lambda: 'nada')

mi_dic['uno'] = 'verde'

print(mi_dic['dos'])
print(mi_dic)


# ejercicio 1
from collections import Counter

lista = [1, 2, 3, 6, 7, 1, 2, 4, 5, 5, 5, 5, 3, 2, 6, 7]

contador = Counter(lista)
print(contador)

#ejercicio 2
from collections import defaultdict

mi_diccionario = defaultdict(lambda: "Valor no hallado")

mi_diccionario['edad'] = 44

print(mi_diccionario)

#ejercicio 3
from collections import deque

ciudades = ["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"]
lista_ciudades = deque(ciudades)
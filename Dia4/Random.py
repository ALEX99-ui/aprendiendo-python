from random import *

aleatorio = randint(1, 100)
print(aleatorio)

#uniform

aleatorio1 = round(uniform(1 ,5),1)
print(aleatorio1)

#usando random
aleatorio2 = random()
print(aleatorio2)

#usando choice
colores = ['red', 'green', 'blue']
aleatorio3 = choice(colores)
print(aleatorio3)

# ejemplo usando shuffle para mezclar solo se puede usar con numeros
numeros = list(range(5,50,5))

shuffle(numeros)
print(numeros)

#practica usando randint()
from random import *
aleatorio = randint(1,10)
print(aleatorio)

#practica usando random() para obtener decimal entre cero y uno
from random import *
aleatorio = random()
print(aleatorio)

#practica usando choice()
from random import *
nombres = ["Carlos", "Julia", "Nicole", "Laura", "Mailen"]

sorteo = choice(nombres)
print(sorteo)
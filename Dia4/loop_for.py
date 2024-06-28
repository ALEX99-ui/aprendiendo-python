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

for item in dic.items():
    print(item)

#Practica loop for 1
alumnos_clase = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás", "Daniela"]

for alumno in alumnos_clase:
    print("Hola " + alumno)

#practica loop for 2
lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_numeros = 0

for numero in lista_numeros:
    suma_numeros = suma_numeros + numero

print(suma_numeros)

#practica loop for 3
lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares = 0
suma_impares = 0

for numero in lista_numeros:
    if numero % 2==0:
        suma_pares += numero
    else:
        suma_impares += numero
print("pares", suma_pares)
print("impares", suma_impares)
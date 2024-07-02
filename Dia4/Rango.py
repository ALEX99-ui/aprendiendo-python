for numero in range(5):
    print(numero)

#ejemplo
lista = list(range(1,101))
print(lista)

#pratica rango 2
#Utilizando la función range(), crea en una única linea de código una lista formada por todos los números múltiplos de 3 desde el 3 al 300 (inclusive). Almacena dicha lista en la variable mi_lista
mi_lista = list(range(3, 301, 3))
print(mi_lista)

#practica rango 3
suma_cuadrados = 0

for numero in range(1, 16):
    cuadrado = numero ** 2
    suma_cuadrados += cuadrado

print(suma_cuadrados)
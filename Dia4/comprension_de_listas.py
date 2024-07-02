palabra = 'python'

lista = [letra for letra in palabra] #una letra por cada letra que haya en palabra

print(lista)

# ejemplo
lista1 = [n / 2 for n in range(0,21,2)]
print(lista1)

# usando if
lista2 = [n if n * 2 > 10 else 'no' for n in range(0,21,2)] #orden correcto de escribir la funcion si se añade if else

print(lista2)

#ejemplo
pies = [10,20,30,40,50]
metros = [p / 3.281 for p in pies]
print(metros)

#practica 1 elevando a cuadrado
valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_cuadrado = [numero ** 2 for numero in valores]
print(valores_cuadrado)

#practica 2
valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_pares = [valor for valor in valores if valor % 2 == 0 and valor == int(valor)]
print(valores_pares)

#practica 3
temperatura_fahrenheit = [32, 212, 275]
grados_celsius = [(grados_fahrenheit-32) * (5/9) for grados_fahrenheit in temperatura_fahrenheit]
print(grados_celsius)


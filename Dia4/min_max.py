menor = min(58,96,72,64,35)
mayor = max(58,96,72,64,35)
print(menor, mayor)

# otra manera de hacerlo
lista = [58,96,72,64,35]

print(f'el menor es {min(lista)} y el mayor es {max(lista)}')

#usando strings
nombres = ['Juan', 'Pablo', 'Alicia', 'Carlos']
print(min(nombres))
dic = {'C1':45, 'C2':11}
print(min(dic.values()))

#practica 1 mostrar el valor maximo
lista_numeros = [44542247/2, 21310/5, 2134747*33, 44556475, 121676, 6654067, 353254, 123134, 55**12, 611**5]
valor_maximo = max(lista_numeros)
print(valor_maximo)

#practica 2 calcular diferencia entre el max y el min
lista_numeros = [44542247, 21310, 2134747, 44556475, 121676, 6654067, 353254, 123134, 552512, 611665]
rango = max(lista_numeros) - min(lista_numeros)
print(rango)

#practica 3
diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}

edad_minima = min(diccionario_edades.values())
ultimo_nombre = max(diccionario_edades)

print(edad_minima, ultimo_nombre)
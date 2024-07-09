def suma_menores(lista_numeros):

    for numero in lista_numeros:
        if numero > 0 and numero < 1000:
            suma = suma + numero
        print(suma)

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8]
print(suma_menores(lista_numeros))





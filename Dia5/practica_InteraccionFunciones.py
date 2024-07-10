lista_numeros = [1, 2, 15, 7, 2]

def reducir_lista(lista_numeros):
    mi_lista = set(lista_numeros)
    valor_maximo = max(mi_lista)
    mi_lista.remove(valor_maximo)
    nueva_lista = list(mi_lista)
    lista_final = nueva_lista
    return lista_final

def promedio(lista_final):
    suma = sum(lista_final)
    num_elementos = len(lista_final)
    promedio = suma / num_elementos
    return promedio


resultado = promedio(lista_numeros)
print(resultado)
def devolver_distintos(a,b,c):

    lista = [a,b,c]

    if sum(lista) > 15:
        numero_max = max(lista)
        return numero_max


    elif sum(lista) < 10:
        numero_menor = min(lista)
        return numero_menor

    else:
        lista_ordenada = sorted(lista)
        resultado = lista_ordenada[1]
        return resultado

total = devolver_distintos(5,3,5)
print(total)
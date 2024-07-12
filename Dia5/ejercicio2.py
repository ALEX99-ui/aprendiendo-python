def palabra_orden(palabra):

    letras_unicas = set(palabra) # Convertir la cadena a un conjunto para eliminar duplicados

    letras_ordenadas = sorted(letras_unicas) # Convertir el conjunto a una lista y ordenarla alfabéticamente

    resultado = ''.join(letras_ordenadas)   # Unir los elementos de la lista en una cadena

    return resultado

palabra = input('ingrese palabra: ')

resultado = palabra_orden(palabra)
print(resultado)

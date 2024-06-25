texto = input("ingrese un texto o articulo que desee:").lower()
print(f'texto seleccionado: {texto}')

selecciona_letra = "selecciona tres letras a su elección. "
print(selecciona_letra)
letra1 = input("ingrese la primera letra: ")
letra2 = input("ingrese la segunda letra: ")
letra3 = input("ingrese la tercera letra: ")
lista = [letra1, letra2, letra3]
print(f'letras seleccionadas: {lista}')

contador1 = texto.count(letra1)
contador2 = texto.count(letra2)
contador3 = texto.count(letra3)

print(f'el numero de letras seleccionadas que hay en el texto es: {contador1}, {contador2}, {contador3}')

palabras = texto.split()
cantidad_palabras = len(palabras)
print(f'en el texto hay {cantidad_palabras} palabras')

primera_letra = texto[0]
ultima_letra = texto[-1]
print(f'primera letra del texto: {primera_letra[0]}')
print(f'ultima letra del texto: {ultima_letra[-1]}')

invertido = texto[::-1]
print(f'invertido del texto: {invertido}')

palabra = "python"
consulta_texto = palabra in texto
print(f'esta la palabra python?: {consulta_texto}')

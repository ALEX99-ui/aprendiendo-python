#Práctica Sub - Strings 1
frase = "Controlar la complejidad es la esencia de la programación"
print(frase[:9])

#Práctica Sub - Strings 2
frase = "Nunca confíes en un ordenador que no puedas lanzar por una ventana"
print(frase[8::3])

#Práctica Sub - Strings 3
frase = "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"
print(frase[::-1])

#Práctica Métodos de String 1
frase = "Especialmente en las comunicaciones electrónicas, la escritura enteramente en mayúsculas equivale a gritar."

print(frase.upper())

#Práctica Métodos de String 2
lista_palabras = ["La", "legibilidad", "cuenta."]
frase = " ".join(lista_palabras)
print(frase)

#Práctica Métodos de String 3
frase = "Si la implementación es difícil de explicar, puede que sea una mala idea."
print(frase.replace("difícil", "fácil").replace("mala", "buena"))

#Práctica Propiedades de Strings 1
palabra = "Repetición"
print(palabra * 15)

#Práctica Propiedades de Strings 2
haiku = '''
Tierra mojada
mis recuerdos de viaje,
entre las lluvias
'''
print("agua" not in haiku)

#Práctica Propiedades de Strings 3
palabra = "electroencefalografista"
print(len(palabra))


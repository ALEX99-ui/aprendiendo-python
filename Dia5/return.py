def multiplicar(numero1, numero2):
    total = numero1 * numero2
    return total

resultado = multiplicar(5,10)
print(resultado)

 #practica 1 return
def potencia(numero1, numero2):
    total = numero1 ** numero2
    return total

resultado = potencia(3, 4)
print(resultado)

#practica 2 return
def usd_a_eur(valor):
    total = valor * 0.90
    return total

dolares = usd_a_eur(500)
print(dolares)

#practica 3 return
def invertir_palabra(string):
    invertir = string.upper()[::-1]
    return invertir

palabra = invertir_palabra("python")
print(palabra)
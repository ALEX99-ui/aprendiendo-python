def chequear_3_cifras(numero):
    return numero in range(100, 1000)

resultado = chequear_3_cifras(520)
print(resultado)

# ejemplo
def chequear_cifras(lista):

    lista_3_cifras = []

    for n in lista:
        if n in range(100, 1000):
            return True
        else:
            pass

resultado1 = chequear_cifras([55,99,6000])
print(resultado1)

# practica
def todos_positivos(lista_numeros):
    for n in lista_numeros:
        if n <= 0:
            return False
    return True

lista_numeros = [1, -50, 502, -5000, 755, 600, 33, 61]
print(todos_positivos(lista_numeros))  # Este imprimirá False ya que hay números negativos


#practica 2 funciones dinamicas

def suma_menores(lista_numeros):
    suma = 0  # Inicializamos la variable suma en 0

    for numero in lista_numeros:
        if numero > 0 and numero < 1000:  # Condición para sumar solo los números entre 0 y 1000
            suma = suma + numero
    return suma  # Devolvemos la suma total (se corrigió la indentación de return)

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8]
print(suma_menores(lista_numeros))  # Imprimimos el resultado de la función

# practica 3

def cantidad_pares(lista_numeros):
    contador = 0
    for numero in lista_numeros:
        if numero % 2 == 0:
            contador += 1
    return contador


lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8]
print(cantidad_pares(lista_numeros))

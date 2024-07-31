# crear un programa modular que calcule el area de un triangulo valores de entrada por teclado
def calcular_area(a, b):
    area = (b * a)/ 2
    return area

print('ingresar altura')
a = float(input())
print('ingresar base')
b = float(input())

print('el area es: ' + str(calcular_area(a, b)))



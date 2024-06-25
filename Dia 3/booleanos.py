var1 = True
var2 = False
print(var1)

#de manera indirecta
numero = 5 != 2+3 #puedo usar >, <, ==, >=, <=
print(numero)

#puedo ser mas explicito
numero1 = bool(5 > 6)
print(numero1)

#ejemplo con lista
lista = [1,2,3,4,5]
control = 6 not in lista
print(control)
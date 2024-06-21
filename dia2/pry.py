# solicita al usuario ingresar su nombre
nombre = input("cual es tu nombre?")
print("Hola " + nombre)

# pregunta al usuario cuanto ha vendido este mes
venta = int(input("cuanto has vendido este mes?"))

comision = (venta * 13)/100
print(nombre + " tu comision de venta es:  " + str(comision))


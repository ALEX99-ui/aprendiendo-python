nombre = input("cual es tu nombre?")
print("Hola " + nombre)
venta = int(input("cuanto has vendido este mes?"))

comision = (venta * 13)/100
comision = round(comision)
print(f"hola {nombre}, tus comisiones de este mes es ${comision}")


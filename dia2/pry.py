nombre = input("cual es tu nombre?")
print("Hola " + nombre)

venta = int(input("cuanto has vendido este mes?"))

comision = round(venta * 13/ 100)

print(f"hola {nombre}, tus comisiones de este mes es ${comision}")


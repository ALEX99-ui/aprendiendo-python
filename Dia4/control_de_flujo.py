if 10 > 9:
    print('es correcto')

# ejemplo
x = True
if True:
    print('es correcto')

#ejemplo 2
if 5 == 2:
    print('es correcto')
else:
    print('no es correcto')

#ejemplo 3
mascota = 'pez'

if mascota == 'gato':
    print('tienes un gato')
elif mascota == 'perro':
    print('tienes un perro')
elif mascota == 'pez':
    print('tienes un pez')
else:
    print('no se que animal tienes')

#ejemplo 4
edad = 17
calificacion = 9

if edad < 18:
    print('eres menor de edad')
    if calificacion >= 7:
        print('Aprobado')
    else:
        print('No aprobado')
else:
    print('eres adulto')

#practica control de flujo 1
num1 = int(input("Ingresa un número:"))
num2 = int(input("Ingresa otro número:"))

f"{num1} es mayor que {num2}"
"num2 es mayor que num1"
"num1 y num2 son iguales"

if num1 > num2:
    print(f"{num1} es mayor que {num2}")
elif num1 == num2:
    print(f"{num1} y {num2} son iguales")
else:
    print(f"{num2} es mayor que {num1}")

#practica control de flujo 2
edad = 16
tiene_licencia = False

if edad >= 18 and tiene_licencia:
    print("Puedes conducir")
elif edad < 18:
    print("No puedes conducir aún. Debes tener 18 años y contar con una licencia")
elif edad >= 18 and not tiene_licencia:
    print("No puedes conducir. Necesitas contar con una licencia")

#practica control de flujo 3
habla_ingles = True
sabe_python = False

if sabe_python and habla_ingles:
    print("Cumples con los requisitos para postularte")
elif not sabe_python and not habla_ingles:
    print("Para postularte, necesitas saber programar en Python y tener conocimientos de inglés")
elif not sabe_python and habla_ingles:
    print("Para postularte, necesitas saber programar en Python")
elif sabe_python and not habla_ingles:
    print("Para postularte, necesitas tener conocimientos de inglés")

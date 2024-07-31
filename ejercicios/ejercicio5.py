# escribe un programa que, al recibir como dato un numero entero positivo N, calcule el 
# resultado de la siguiente serie: 
# 
# 1 + (1/2) + (1/3) + (1/4) + ... + (1/N)
#
# si el usuario escribe un numero incorrecto, el programa no se ejecuta. En cambio,
# pregunta de nuevo por la informacion hasta que el dato ingresado sea correcto. 

comprobar = True

while comprobar == True:
   
    n = int(input('Ingrese numero entero positivo: '))

    if n > 0: 

        resultado = 0

        for i in range(1, n+1):

            resultado += (1/i)

        print('el resultado de la serie es: ', resultado)

        comprobar = False 

    else: 
        print('el numero ingresado no es correcto, intentelo nuevamnente')
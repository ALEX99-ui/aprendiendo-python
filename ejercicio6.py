# escribe un programa que, al recibir como dato un numero entero positivo N, calcule el 
# resultado de la siguiente serie: 
# 
# 1 / (1/2) * (1/3) / (1/4) * ... (*/) (1/N)
#
# si el usuario escribe un numero incorrecto, el programa no se ejecuta. En cambio,
# pregunta de nuevo por la informacion hasta que el dato ingresado sea correcto. 

comprobar = True

while comprobar == True:

    n = int(input('ingrese un numero entero positivo: '))

    if n > 0: 

        comprobar = False

        resultado = 1

        for i in range(2, n+1):

            if i % 2 == 0:

                resultado = resultado / (1/i)
            
            else: 
                resultado = resultado * (1/i)
        
        print('el resultado de la serie es ', resultado)

    else:

        print('el numero ingresado no es correcto, intentelo nuevamente')
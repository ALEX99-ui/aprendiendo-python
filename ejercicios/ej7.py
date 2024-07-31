# construye un programa que, al recibir como datos N numeros naturales, determine
# cuantos de ellos son positivos, negativos o nulos.
#
# si el usuario escribe un numero incorrecto, el programa no se ejecuta. En cambio, 
# pregunta de nuevo por la informacion hasta que el dato ingresado sea correcto. 

comprobar = True

while comprobar == True:

    n = int(input('ingrese la cantidad de datos que desea procesar: '))

    if n > 0:

        positivos = 0
        negativos = 0
        nulos = 0

        for i in range(n):
            
            comprobar = False

            dato = int(input('ingrese un numero natural: '))

            if dato > 0:
                positivos += 1
            
            elif dato < 0:
                negativos += 1
            
            else:
                nulos += 1

        print('la cantidad de numeros positivos fue: ', positivos,
            '\nla cantidad de numeros negativos fue: ', negativos,
            '\nLa cantidad de numeros nulos fue: ', nulos)
            
    else:
        
        print('el numero ingresado no es correcto, intentelo nuevamente')
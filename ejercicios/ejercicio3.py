# escribe un programa que permita generar la tabla de multiplicar de un numero entero
# positivo N, comenzando desde 1
# si el usuario escribe un numero incorrecto, el programa no se ejecuta. En cambio,
# pregunta de nuevo por la informacion hasta que el dato ingresado sea correcto 



comprobar = True

while comprobar == True:

    n = int(input('Ingrese un numero entero positivo: '))

    if n > 0:

        for i in range(1, 11):

            print(n, 'por', i, 'es igual a: ', n*i)

        comprobar = False
        
    else: 

        print('el numero ingresado no es correcto, intentelo de nuevo')
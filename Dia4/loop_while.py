monedas = 5

while monedas > 0:
    print(f'tengo {monedas} monedas')
    monedas -= 1
else:print('no tengo mas dinero')

#ejemplo
respuesta = 's'

while respuesta == 's':
    respuesta = input('quieres seguir? (s/n)')
else:
    print('gracias')

#ejemplo 2
nombre = input('tu nombre: ')

for letra in nombre:
    if letra == 'r':
        break            #interrumpe el programa, si uso el cmd (continue) el programa no se interrumpe pero solo corta la letra que se declaro.
    print(letra)          # utilizo el cmd (pass) para reservar un espacio sin terminar el codigo y poder continuar con otro

#practica loop while 1
#Crea un Loop While que se imprima en pantalla los números del 10 al 0, uno a la vez.
numero = 10

while numero >= 0:
    print(numero)
    numero -= 1

#practica loop while 2
numero = 50

while numero >= 0:
    if numero % 5 == 0:
        print(numero)
    numero -= 1

# practica interrupcion de flujo
lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]
for numeros in lista_numeros:
    if numeros < 0:
        break
    print(numeros)


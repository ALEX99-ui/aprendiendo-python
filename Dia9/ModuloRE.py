import re

texto = 'Si necesitas ayuda llama al (658)-598-9977 las 24 horas al servicio de ayuda online'

patron = 'ayuda'

for hallazago in re.finditer(patron, texto):
    print(hallazago.span())



# ejemplo 2

texto = 'llama al 525-525-6588 ya mismo'

patron = re.compile(r'(\d{3})-(\d{3})-(\d{4})')

resultado = re.search(patron, texto)

print(resultado.group(3))


# ejemplo 3

clave = input('Clave: ')

patron = r'\D{1}\w{7}'

chequear = re.search(patron, clave)

print(chequear)


# ejemplo 4

texto = 'no atendemos el lunes por la tarde'

buscar = re.findall(r'[^\s]+', texto)

print(''.join(buscar))



# ejercicio 5

def verificar_saludo(frase):
    patron = r'hola|Hola|HOLA'

    verificar = re.match(patron, frase)

    if verificar:
        print("Ok")
    else:
        print("No has saludado")
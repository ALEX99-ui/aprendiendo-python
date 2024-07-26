mi_archivo = open('prueba.txt')

una_linea = mi_archivo.readline()
print(una_linea.upper())

una_linea = mi_archivo.readline()
print(una_linea.rstrip())               #rstrip() se usa para quitar el salto de linea

una_linea = mi_archivo.readline()
print(una_linea)

# se puede iterar dentro de las lineas de un archivo

for l in mi_archivo:
    print('aqui dice: ' + l)


# trabajando con readlines()

todas = mi_archivo.readlines()

toda = todas.pop()

print(toda)





mi_archivo.close()
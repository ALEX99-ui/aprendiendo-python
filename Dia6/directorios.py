import os 

ruta = os.getcwd()  #get current working directioner 

print(ruta)

# chdir() change directory, establecer ruta distinta de trabajo 

ruta1 = os.chdir('C:\\Users\\urrea\\alternativa')

archivo = open('alternativo.txt')
print(archivo.read())

# mkdir() crear una carpeta nueva

#ruta2 = os.mkdir('C:\\Users\\urrea\\alternativa\\otra')

#archivo1 = open('alternativo.txt')
#print(archivo1.read())

#
ruta3 = 'C:\\Users\\urrea\\PycharmProjects\\testProject1\\Dia6\\prueba1.txt'

elemento = os.path.basename(ruta3)  # dirname(), split() para tupla
print(elemento)

# rmdir() para remover directorios

#os.rmdir('C:\\Users\\urrea\\alternativa\\otra')

# como abrir un archivo sin usar os 

otro_archivo = open('C:\\Users\\urrea\\alternativa\\otro_archivo.txt')
print(otro_archivo.read())


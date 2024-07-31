archivo = open('prueba.txt', 'a')

archivo.write('bienvenido ')
archivo.close()

# ejercicio 
# Lista de la última sesión a registrar
registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]

arc = open("registro.txt", "a")

for item in registro_ultima_sesion:

    arc.writelines(item + "\t")

arc.close()

arc = open("registro.txt", "r")

print(arc.read())

#ejercicio 1
archivo = open("mi_archivo.txt", "w")
archivo.write("Nuevo texto")
archivo.close()
archivo = open("mi_archivo.txt", "r")
print(archivo.read())

#ejercicio2

archivo = open("mi_archivo.txt","a")
archivo.write("Nuevo inicio de sesión")
archivo.close()
archivo = open("mi_archivo.txt", "r")
print(archivo.read())

#ejercicio 3
registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]

registro = open("registro.txt", "a")
for item in registro_ultima_sesion:
    registro.writelines(item + '\t')

registro.close()
registro = open("registro.txt", "r")
print(registro.read())

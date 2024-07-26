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


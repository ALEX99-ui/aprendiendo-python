archivo = 'ejemplo.txt'
def abrir_leer(archivo):
    archivo = open(archivo)
    return archivo.read()


 #ejercicio2
"contenido eliminado"

archivo = 'ejemplo.txt'
def sobrescribir(archivo):
    archivo = open(archivo, 'w')
    return archivo.write('contenido eliminado')

# ejercicio3

"se ha registrado un error de ejecución"

archivo = 'ejemplo.txt'

def registro_error(archivo):
    archivo = open(archivo, 'a')
    return archivo.write('se ha registrado un error de ejecución')

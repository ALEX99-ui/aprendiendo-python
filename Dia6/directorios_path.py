from pathlib import Path 

carpeta = Path('/Users/urrea/alternativa') / 'otro_archivo.txt'


mi_archivo = open(carpeta)
print(mi_archivo.read())


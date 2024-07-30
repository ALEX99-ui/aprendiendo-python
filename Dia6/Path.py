from pathlib import Path, PureWindowsPath

carpeta = Path('C:/Users/urrea/PycharmProjects/testProject1/Dia6/prueba1.txt')

print(carpeta.read_text())   # otros metodos: name(), suffix es una funcion no un metodo,  me muestra el tipo de archivo y muchos mas.

#metodo para ver si este archivo existe

ruta_windows = PureWindowsPath(carpeta)

print(ruta_windows)

if not carpeta.exists():
    print('este archivo no existe')

else: 
    print('genial, existe')
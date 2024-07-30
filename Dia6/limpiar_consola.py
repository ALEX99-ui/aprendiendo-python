import os 

fuente = 'hola soy fuente'

print(fuente)

def clear_console():
    if os.name == 'nt': 
        os.system('cls')

clear_console()
from random import choice

# inicio juego

def inicio_juego():

    print("*          ¡Bienvenido al Ahorcado!      *")
    print("\nInstrucciones:")
    print("1. Adivina la palabra secreta letra por letra.")
    print("2. Tienes un número limitado de intentos.")
    print("3. Cada letra incorrecta te acerca un paso más a ser 'ahorcado'.")
    print("4. La temática son: Animales")
    print("4. ¡Buena suerte!\n")

# lista de palabras para jugar 

def palabras_azar():
    lista = ['perro', 'gato', 'caballo', 'burro', 'elefante', 'avestruz', 'tigre', 'aguila', 'buho', 'jirafa','delfin',
            'zorro', 'oso', 'rinoceronte', 'mono', 'gorila', 'camello']
    palabra_original = choice(lista).lower()
    return palabra_original

# convertir palabra a guiones bajos 

palabra_original = palabras_azar()

palabra_oculta = ['_' for _ in palabra_original]

letras_adivinadas = []


def mostrar_palabra_oculta(palabra_oculta):

    return ''.join(palabra_oculta)



def desarrollo():

    countervidas = 0
    vidas = 8

    while '_' in palabra_oculta and countervidas < vidas:

        
        
        print(f'palabra oculta: {mostrar_palabra_oculta(palabra_oculta)}')

        letra = input('Adivina una letra: '.lower())

        if letra in letras_adivinadas:
            counter = 0
            counter2 = 0
            for i in palabra_original:
                if(i == letra):
                    counter +=1
            for i in letras_adivinadas:
                if(i == letra):
                    counter2 += 1
            if(counter2 == counter):
                print('Ya has adivinado esa letra. Intenta con otra.')
                continue
                
        

        if letra in palabra_original:

            for i, l in enumerate(palabra_original): 
                                                          # 'i' es un numero que representa la posicion de cada letra en la palabra y 'l' es cada letra en la palabra orignal
                if l == letra:                            # 'enmerate(palabra_original)' es una funcion que nos da tanto la posicion ('i') como la letra ('l') en cada repeticion del bucle
                    print('Adivino correctamente')
                    if(palabra_oculta[i] == letra):
                        continue
                    palabra_oculta[i] = letra              #Esto reemplaza el guion en la posición 'i' de la palabra oculta (palabra_oculta) con la letra correcta (letra).
                    letras_adivinadas.append(letra)
                    break
                   
        else:
            print('La letra no esta en la palabra. Intente nuvamente')
            countervidas += 1
            print(f'te quedan {vidas - countervidas} vidas')
        
    print(f'palabra oculta: {mostrar_palabra_oculta(palabra_oculta)}')



print(inicio_juego())
print(desarrollo())




#ejemplo
nombres = ['Ana', 'Hugo','Valeria']
edad = [65,29,42]
ciudades = ['Lima','Madrid','Mexico']

zipped = list(zip(nombres, edad, ciudades))

for nombre,edad,ciudad in zipped:
    print(f'{nombre} tiene {edad} años y vive en {ciudad}')

#practica 1 zip
capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

zipped = list(zip(capitales, paises))

for capital,pais in zipped:
    print(f'la capital de {pais} es {capital}')

#practica

español = ['uno', 'dos', 'tres', 'cuatro', 'cinco']
portugues = ['um', 'dois', 'três', 'quatro', 'cinco']
ingles = ['one', 'two', 'three', 'four', 'five']

numeros = list(zip(español, portugues, ingles))

for numero in numeros:
    print(numeros)
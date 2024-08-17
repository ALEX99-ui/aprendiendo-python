class Animal:

    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print('este animal ha nacido')

    def hablar(self):
        print('este animal emite un sonido')

class Pajaro(Animal):

    def __init__(self, edad, color, altura_vuelo):
        super().__init__(edad, color)
        self.altura_vuelo = altura_vuelo
    def hablar(self):
        print('pio')

    def volar(self, metros):
        print(f'el pajaro vuela {metros} metros')

piolin = Pajaro(2, 'amarillo', 60)

mi_animal = Animal(5, 'negro')

# segundo ejemplo
class Padre:
    def hablar(self):
        print('hola')


class Madre:
    def reir(self):
        print('ja ja ja')

    def hablar(self):
        print('que tal')
class Hijo(Padre, Madre):
    pass

class Nieto(Hijo):
    pass

mi_nieto = Nieto()

print(Nieto.__mro__)
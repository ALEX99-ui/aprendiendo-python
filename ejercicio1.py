import math

def area_circulo(r):
    area = math.pi * math.pow(r, 2)
    return area 

print('ingresa radio del circulo')
r = float(input())

print('el area del circulo es ' + str(area_circulo(r)))

def calcular_edad(nac, actual):
    edad = actual - nac
    return edad 

print('ingrese año de nacimiento')
nac = int(input())
print('ingrese año actual')
actual = int(input())

print('su edad es ' + str(calcular_edad(nac, actual)))
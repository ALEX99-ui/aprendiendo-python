a = 10
b = 5
c = 15

mi_bool = a < b and c > b
print(mi_bool)

#2 ejemplo
mi_bool1 = (4 < 5) and (5 == 2+3)
print(mi_bool1)

#3 ejemplo
texto = "esta frase es breve"
texto1 =  ('frase' in texto) and ('breve' in texto)
print(texto1)

#4 ejemplo
ejemplo = not ('a' == 'a')
print(ejemplo)

#Práctica Operadores Lógicos 1
num1 = 36
num2 = 72/2
num3 = 48
mi_bool = num1 > num2 and num1 < num3

print(mi_bool)

#Práctica Operadores Lógicos 2
num1 = 36
num2 = 72/2
num3 = 48
mi_bool = num1 > num2 or num1 < num3

#Práctica Operadores Lógicos 3
frase = "Cuando algo es lo suficientemente importante, lo haces incluso si las probabilidades de que salga bien no te acompañan"
palabra1 = "éxito"
palabra2 = "tecnología"

mi_bool = not (palabra1 and palabra2) in frase

print(mi_bool)
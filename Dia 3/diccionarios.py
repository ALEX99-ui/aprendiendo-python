diccionario = {'c1':'valor1', 'c2':'valor2'}
print(diccionario)

resultado = diccionario['c1']
print(resultado)

#ejemplo
cliente = {'nombre':'Juan', 'apellido':'Fuentes', 'peso':88, 'talla':1.76}
consulta = (cliente['talla'])
print(consulta)

#2 ejemplo
dic = {'c1':55, 'c2':[10,20,30], 'c3':{'s1':180, 's2':200}}
print(dic['c3']['s2'])

#3 ejemplo
dic2 = {'c1':['a', 'b', 'c'], 'c2':['d', 'e', 'f']}
print(dic2['c2'][1].upper())

#agregar elementos al diccionario
dic3 = {1:'a', 2:'b'}
print(dic3)

dic3[3] = 'c'
print(dic3)

#sobre escribir un elemento del diccionario
dic3[2] = 'B'
print(dic3)

#conocer todas las claves que hay en el diccionario
print(dic3.keys())
#conocer los valores
print(dic3.values())
#para conocer todo lo que hay dentro del diccionario
print(dic3.items())

#ejercicio udemy para actualizar y agregar en una misma linea
mi_dic = {"nombre":"Karen", "apellido":"Jurgens", "edad":35, "ocupacion":"Periodista"}
nuevos_elementos = {'ocupacion':'Editora', 'edad':36, 'pais':'Colombia'}
mi_dic.update(nuevos_elementos)
print(mi_dic)

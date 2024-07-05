dic = {'clave1':100, 'clave2':500}

a = dic.popitem()
print(a)

#practica 1 metdos y ayuda, uso de lstrip() para eliminar elementos
cadena = ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"

x = cadena.lstrip(',:%_#')

print(x)

#practica 2 metodos y ayuda, uso de insert() para añadir elementos.
frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]

x1 = frutas.in sert(3, 'naranja')  #el 3 es la posicion y naranja es el elemento a añadir

print(x1)

#practica 3 metodos y ayudas, uso de isdisjoint()
marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}

marcas_tv = {"Sony", "Philips", "Samsung", "LG"}

x2 = marcas_smartphones.isdisjoint(marcas_tv)

print(x2)


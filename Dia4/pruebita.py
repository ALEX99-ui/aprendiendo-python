lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
lista = []

for item in enumerate(lista_nombres):
    for i in item:
        lista.append(i)
    print(f'{lista[1]} se encuentra en el índice {lista[0]}')
    lista.clear()


cadena = input("ingrese una cadena de caracteres..")

lista = cadena.split()

cantidad = 0

for i in range(len(lista)):
    if lista.count(lista[i]) > cantidad:
        mas_repetida = lista[i]
        cantidad = lista.count(lista[i])

print('la palabra mas repetida es "{}" y se repitio {} veces'.format(mas_repetida, cantidad))
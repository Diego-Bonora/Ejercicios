def ingresar():
    lista = []
    for i in range(5):
        numero = int(input("ingrese un numero.."))
        lista.append(numero)
    return lista

def indice(lista):
    indice = int(input("ingrese un numero.."))
    while indice < 1 or indice > len(lista):
        indice = int(input("ingrese un numero menor o igual a {} y mayor a 0..".format(len(lista))))
    return indice

def ordenados(lista,numero):
    lista.append(0)
    verificacion = True
    for i in range(numero):
        if lista[i] < lista [i+1]:
            verificacion = False
    return verificacion

lista = ingresar()

print("hasta que numero quieres verificar?")
numero = indice(lista)

T_F = ordenados(lista,numero)

print(T_F)
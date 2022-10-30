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

def intercambio(lista,numero,numero_nuevo):
    lista[numero - 1] = numero_nuevo
    return lista


lista = ingresar()

print("hasta que numero quieres verificar?")
numero = indice(lista)

numero_nuevo = int(input("ingrese un nuevo numero.."))

lista = intercambio(lista,numero,numero_nuevo)
print(lista)
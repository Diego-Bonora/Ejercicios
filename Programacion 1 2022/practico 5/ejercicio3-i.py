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

def nueva_lista(lista,numero):
    nueva_lista = [0] * numero
    for i in range(numero):
        nueva_lista[i] = lista[i]
    return nueva_lista

def pares(lista):
    pares = []
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            pares.append(lista[i])
    return pares

def multiplicacion(lista):
    total = 1
    for i in range(len(lista)):
        total*= lista[i]
    return total


lista = ingresar()

print("hasta que numero quieres verificar?")
numero = indice(lista)

lista_nueva = nueva_lista(lista,numero)

pares_lista = pares(lista_nueva)
if len(pares_lista) == 0:
    print(0)
else:
    multiplicacion_lista = multiplicacion(pares_lista)

    print(multiplicacion_lista)



def ingresar():
    lista = []
    for i in range(5):
        numero = int(input("ingrese un numero.."))
        lista.append(numero)
    return lista

def lugares(lista,numero):
    lugares = []
    for i in range(len(lista)):
        if lista[i] == numero:
            lugares.append(i+1)
    return lugares

lista = ingresar()

numero = int(input("ingrese un numero para buscar en la lista.."))

lugares_numero = lugares(lista,numero)

print(lugares_numero)
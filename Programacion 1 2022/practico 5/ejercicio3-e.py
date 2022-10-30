def ingresar():
    lista = []
    for i in range(5):
        numero = int(input("ingrese un numero.."))
        lista.append(numero)
    return lista

def ocurrencias(lista, numero):
    cantidad_ocurrencias = lista.count(numero)
    return cantidad_ocurrencias
    
lista = ingresar()

numero = int(input("ingrese un numero para ver las ocurrencias de el.."))

repetidos = ocurrencias(lista,numero)

print("la cantidad de veces que se repitio el {} en la lista es {}".format(numero,repetidos))

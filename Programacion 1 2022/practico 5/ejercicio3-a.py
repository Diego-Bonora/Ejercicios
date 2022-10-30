def desplegar(lista):
    for i  in range(len(lista)):
        print(lista[i])

def ingresar():
    lista = []
    for i in range(5):
        numero = int(input("ingrese un numero.."))
        lista.append(numero)
    return lista


lista = ingresar()
desplegar(lista)
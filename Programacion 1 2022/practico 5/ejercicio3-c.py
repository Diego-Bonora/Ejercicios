def ingresar():
    lista = []
    for i in range(5):
        numero = int(input("ingrese un numero.."))
        lista.append(numero)
    return lista

def suma_lista(lista):
    suma = 0
    for i in range(len(lista)):
        suma+= lista[i]
    return suma

lista = ingresar()
suma = suma_lista(lista)

print("la suma de los numeros de la lista es {}".format(suma))

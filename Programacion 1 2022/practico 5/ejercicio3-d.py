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

def suma_lista(lista,indice_a,indice_b):
    suma = 0
    for i in range(indice_a-1,indice_b):
        suma+= lista[i]
    return(suma)

lista = ingresar()

print("desde que numero quieres sumar?..")
indice_a = indice(lista)

print("hasta que nuemero quieres sumar?..")
indice_b = indice(lista)

suma_entra_indices = suma_lista(lista,indice_a,indice_b)

print(suma_entra_indices)
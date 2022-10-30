def ingresar():
    lista = []
    for i in range(5):
        numero = int(input("ingrese un numero.."))
        lista.append(numero)
    return lista

def maximo(lista):
    valor_mayor = 0
    for i in range(len(lista)):
        if lista[i] > valor_mayor:
            valor_mayor = lista[i]
    return valor_mayor

lista = ingresar()
valor_mayor = maximo(lista)

print("el numero mayor es {}".format(valor_mayor))
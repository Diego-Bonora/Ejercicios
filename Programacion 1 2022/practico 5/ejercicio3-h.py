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

def duplicas(lista_nueva):
    verificacion = False
    for i in range(len(lista_nueva)):
        if lista_nueva.count(lista_nueva[i]) > 1:
            verificacion = True
            break
    return verificacion

lista = ingresar()

print("hasta que numero quieres verificar?")
numero = indice(lista)

lista_nueva = nueva_lista(lista,numero)

T_F = duplicas(lista_nueva)

print(T_F)
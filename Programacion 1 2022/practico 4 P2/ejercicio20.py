numero = int(input("ingrese hasta que tabla quieres hacer.."))

lista = [0] * (numero + 1)

for i in range(1,numero + 1):
    tabla = []
    for n in range(11):
        multiplicacion = i * n
        tabla.append(multiplicacion)
    lista[i] = tabla
lista.remove(0)
for i in range(len(lista)):
    lista[i].remove(0)
    print(lista[i])

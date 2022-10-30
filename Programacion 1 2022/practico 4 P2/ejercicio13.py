lista = []

for i in range(4):
    numero = int(input("ingrese un numero.."))
    lista.append(numero)

lista.sort(reverse=True)
print(lista)
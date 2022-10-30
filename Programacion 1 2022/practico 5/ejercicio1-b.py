lista = []

for i in range(5):
    numero = float(input("ingrese un numero con coma.."))
    lista.append(numero)

print(lista)
nuevo_numero = float(input("ingresa un nuevo numero para remplasarlo por uno de la lista.."))

while True:
    lugar = int(input("en que lugar quieres ingresar el nuevo numero?.."))

    if lugar <= 5:
        break
    else:
        print("ingrese un numero menor o igual a 5")

lista[lugar - 1] = nuevo_numero

print(lista)
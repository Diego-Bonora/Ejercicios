lista = []

for i in range(3):
    numero = int(input("ingrese un numero..."))
    lista.append(numero)

mediana = lista
mediana.sort()

print("la mediana de",lista,"es",mediana[1])

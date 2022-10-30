from queue import Empty

numeros = []
print("ingrese 5 numeros..")
for i in range(5):
    numero = int(input("ingrese un numero.."))
    numeros.append(numero)
remuve = Empty

for i in range(len(numeros)):
    for v in range(len(numeros)):
        if v != i and numeros[v] != remuve:
            if numeros[i] == numeros[v]:
                print("el numero {} es identico".format(numeros[i]))
                remuve = numeros[v]     
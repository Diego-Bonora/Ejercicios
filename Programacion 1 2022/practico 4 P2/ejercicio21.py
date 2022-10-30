lista = []

print("ingrese 4 numeros para ver todas sus permutaciones..")
for i in range(4):
    numero = int(input("ingrese un numero.."))
    lista.append(numero)

def permutations(start, end=[]):
    if len(start) == 0:
        print(end)
    else:
        for i in range(len(start)):
            permutations(start[:i] + start[i+1:], end + start[i:i+1])
            
permutations(lista)

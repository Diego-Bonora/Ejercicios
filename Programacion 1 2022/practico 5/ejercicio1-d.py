lista_a = [10] * 10
lista_b = [20] * 20

print(lista_a)
print(lista_b)

for i in range(len(lista_a)):
    lista_b[2 + i] = lista_a[i]

print(lista_a)
print(lista_b)
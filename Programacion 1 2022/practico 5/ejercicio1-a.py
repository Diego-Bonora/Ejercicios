lista = []

for i in range(10):
    string = input("ingrese caracteres a tu gusto..")
    lista.append(string)

while True:
    numero = int(input("ingrese un numero.."))

    if numero <= 10:
        break
    else:
        print("ingrese un numero menor o igual a 10")

print(lista[numero - 1])
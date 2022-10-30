numero = int(input("ingrese un numero.."))

lista =[]
i = numero

while i >= 1:
    if numero % i == 0:
        lista.append(i)
    i-= 1

if len(lista) % 2 == 0:
    print("el numero de divisores es par")
else:
    print("el numero de divisores es impar")

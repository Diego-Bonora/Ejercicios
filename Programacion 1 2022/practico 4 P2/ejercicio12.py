def positivo(numero):
    if numero < 0:
        numero * -1
    return numero

def mayor_10d(numero):
    if len(str(numero)) > 10:
        print("overflow")
        exit()

numero1 = int(input("ingrese un numero.."))
numero1 = positivo(numero1)

numero2 = int(input("ingrese un numero.."))
numero2 = positivo(numero2)

mayor_10d(numero1)
mayor_10d(numero2)

suma = numero1 + numero2

mayor_10d(suma)
print(suma)
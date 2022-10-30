def factorial(numero):
    resultado = numero
    if numero == 0:
        return 1
    else:
        for i in range(numero-1):
            resultado = resultado * (numero-1)
            numero = numero-1
        return resultado

numero = int(input("ingrese un numero "))
print(numero)
print(factorial(numero))
def par_inpar(numero):
    if numero % 2 == 1:
        return "inpar"
    else:
        return "par"


numero = int(input("ingrese un numero "))
print(numero)
print(par_inpar(numero))
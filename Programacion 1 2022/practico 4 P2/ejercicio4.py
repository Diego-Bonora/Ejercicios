def vocal(caracter):
    vocal = False
    vocales = ["a","A","e","E","i","I","o","O","u","U"]
    for i in range(len(vocales)):
        if caracter == vocales[i]:
            vocal = True
            print("es vocal")
            break
    if vocal == False:
        print("no es vocal")

caracter = input("ingrese un solo caracter..")
vocal(caracter)
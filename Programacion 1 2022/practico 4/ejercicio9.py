def piramide(altura):
    asterisco = "*"
    blank = " "
    espacio = altura - 1
    cantidad = 1
    for i in range(altura):
        print((blank * espacio) + (asterisco * cantidad))
        cantidad+= 2
        espacio-= 1
    
altura = int(input("ingrese la altura de la piramide "))
print(altura)
piramide(altura)
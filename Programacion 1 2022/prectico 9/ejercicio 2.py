def numero_1al5():
    while True:
        eleccion = int(input("\ningrese un numero del 1 al 5.."))
        if eleccion >= 1 and eleccion <= 5:
            return eleccion
        else:
            print("\nelija un numero del 1 al 5")
        
def numero():
    while True:
        try:
            numero = float(input("\ningrese un numero.."))
        except:
            print("\ningrese un caracter numerico")
        else:
            return numero

while True:
    print("""
    bienvenido a la calculadora
    elija una opcion para continuar
    1)sumar
    2)multiplicar
    3)restar
    4)dividir
    5)salir
    """)

    numero1 = numero()
    numero2 = numero()

    eleccion = numero_1al5()

    print("numero 1 es:{}, numero 2 es:{}\n".format(numero1, numero2))

    if eleccion == 1:
        suma = numero1 + numero2
        print("la suma tutal es {}".format(suma))

    elif eleccion == 2:
        multiplicacion = numero1 * numero2
        print("la multiplicacion total es {}".format(multiplicacion))

    elif eleccion == 3:
        resta = numero1 - numero2
        print("la resta total es {}".format(resta))

    elif eleccion == 4:
        if numero2 == 0.0:
            raise ZeroDivisionError("no se puede dividir entre 0")
        else:
            division = numero1 / numero2
            print("la division total es {}".format(division))

    elif eleccion == 5:
        exit()

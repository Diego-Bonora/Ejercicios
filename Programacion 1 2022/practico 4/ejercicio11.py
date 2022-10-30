lista_F = [["1.Azul","2","Primera"],["2.Roja","1","Primera"],["3.Verde","3","Segunda"],["4.Rosa","2","Segunda"],["5.Gris","1","Tercera"]]

def Listado():
    for i in lista_F:
        Habitacion, Camas, Plantas = i
        print ("{:<10} {:<5} {:<10}".format(Habitacion, Camas, Plantas))

print(lista_F[0][0][0])

def Habitacion_elejida(eleccion):
    encontrado = False
    for i in range(len(lista_F)):
        Habitacion, Camas, Plantas = lista_F[i]
        if eleccion == lista_F[i][0][0]:
            print ("{:<5} {:<10}".format(Camas, Plantas))
            encontrado = True
    if encontrado == False:
        print("Error, el numero",eleccion,"no esta asociado a ninguna habitacion")

while True:
    print("""
        Elija una opcion
    1.Mostrar todas las habitaciones
    2.Monstrar habitacion a eleccion
    3.Cerrar programa
    """)
    eleccion = int(input("..."))
    if eleccion == 1:
        Listado()
    elif eleccion == 2:
        eleccion_habitacion = input("elija una habitacion ")
        Habitacion_elejida(eleccion_habitacion)
    elif eleccion == 3:
        break
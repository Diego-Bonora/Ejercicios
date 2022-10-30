class Bombilla:
    def __init__(self,name,estado) -> None:
        self.name = name
        self.estado = estado

    def interruptor(self):
        if self.estado == "OFF":
            self.estado = "ON"
        else:
            self.estado = "OFF"

class Termica:
    def __init__(self,estado) -> None:
        self.estado = estado

    def interruptor_termica(self):
        if self.estado == "OFF":
            self.estado = "ON"
        else:
            self.estado = "OFF"

if __name__ == "__main__":
    llave_termica = Termica("ON")
    lista_bombillas = []

    numero = int(input("cuantas bombillas tienes en la casa..."))
    for i in range(numero):
        agregar = ("bombilla_"+str(i+1))
        lista_bombillas.append(agregar)
    print(lista_bombillas)

    for i in range(len(lista_bombillas)):
        lista_bombillas[i] = Bombilla(lista_bombillas[i],"OFF")

    prendidas = []
    while True:
        print("""
        ingrese 1 si quiere ver el estado de las bombillas
        ingrese 2 si quiere ver el estado de la termica
        ingrese 3 si quiere apretar el interruptor de una bombilla
        ingrese 4 si quiere apretar el interruptor de la termica
        ingrese otro numero si quiere salir del programa
        """)

        numero_elejido = int(input("ingrese un numero..."))

        if numero_elejido == 1:

            for i in range(len(lista_bombillas)):
                print(lista_bombillas[i].estado)

        elif numero_elejido == 2:

            print(llave_termica.estado)

        elif numero_elejido == 3:

            print("que interruptor quiere apretar...")
            for i in range(len(lista_bombillas)):
                print(i+1,")",lista_bombillas[i].name)
            eleccion = int(input("ingrese un numero..."))

            while True:

                if eleccion <= 0 or eleccion > len(lista_bombillas):
                    print("elija una opcion valida")
                    eleccion = int(input("ingrese un numero..."))

                else:
                    if llave_termica.estado == "OFF":
                        if prendidas.count(eleccion-1) == 0:
                            prendidas.append(eleccion-1)
                        else:
                            prendidas.remove(eleccion-1)
                    else:
                        Bombilla.interruptor(lista_bombillas[eleccion - 1])
                    break

        elif numero_elejido == 4:

            if llave_termica.estado == "ON":
                for i in range(len(lista_bombillas)):
                        if lista_bombillas[i].estado == "ON":
                            prendidas.append(i)
                for i in range(len(prendidas)):
                    Bombilla.interruptor(lista_bombillas[prendidas[i]])

            else:
                for i in range(len(prendidas)):
                    Bombilla.interruptor(lista_bombillas[prendidas[i]])
                prendidas = []
            Termica.interruptor_termica(llave_termica)

        else:
            print("que tengas un lindo dia :)")
            exit()
class Tablero:
    def __init__(self) -> None:
        self._posicion = [["" for i in range(3)] for i in range(3)]

    @property
    def posicion(self):
        return self._posicion

    @posicion.setter
    def posicion(self,valores):
        self.posicion[valores[0]][valores[1]] = valores[2]

    def verificador(self,fila,columna):
        if self.posicion[fila][columna] == "":
            return True
        else:
            return False

    def ganador(self):
        True_False = "NO"
        cruz_arriba_abajo = [self._posicion[0][0],self._posicion[1][1],self._posicion[2][2]]
        cruz_abajo_arriba = [self._posicion[0][2],self._posicion[1][1],self._posicion[2][0]]
        cant_cruz = self._posicion[0].count("X") + self._posicion[1].count("X") + self._posicion[2].count("X")
        cant_circulo = self._posicion[0].count("O") + self._posicion[1].count("O") + self._posicion[2].count("O")
        columnas = []
        for i in range(3):
            col = [row[i]for row in self._posicion]
            columnas.append(col)
        for i in range(3):
            if columnas[i].count("X") == 3:
                True_False = "SI"
        for i in range(3):
            if columnas[i].count("O") == 3:
                True_False = "SI"
        for i in range(3):
            if self._posicion[i].count("X") == 3:
                True_False = "SI"
        for i in range(3):
            if self._posicion[i].count("O") == 3:
                True_False = "SI" 
        if  cruz_arriba_abajo.count("X") == 3 or cruz_arriba_abajo.count("O") == 3:
            True_False = "SI"
        if  cruz_abajo_arriba.count("X") == 3 or cruz_abajo_arriba.count("O") == 3:
            True_False = "SI"
        if cant_cruz + cant_circulo == 9:
            True_False = "EMPATE"
        return True_False

    def __str__(self) -> str:
        return "{}\n{}\n{}".format(self._posicion[0],self._posicion[1],self._posicion[2])

if __name__ == "__main__":
    tateti = ""
    valor = "X"

    def correcto(valor):
        while True:
            numero = int(input("ingrese un numero para la {}..".format(valor)))
            if numero < 1 or numero > 3:
                print("elija un numero entre 0 y 3")
            else:
                return numero

    def turno(valor):
        if valor == "X":
            valor = "O"
        else:
            valor = "X"
        return valor

    while True:
        if tateti == "":
            print("ingrese 1 si quiere inicializar un juego")
            print("ingrese 2 si quiere salir del programa")

            eleccion = int(input("ingrese un numero.."))
            while eleccion != 1 or eleccion !=2:
                if eleccion == 1:
                    tateti = Tablero()
                    break
                elif eleccion == 2:
                    exit()
                else:
                    print("elija un numero valido")
                    eleccion = int(input("ingrese un numero.."))
     
        else:
            while True:
                print("")
                print("es el turno de {}".format(valor))
                print("elija fila y columna para poner {}".format(valor))

                fila = correcto("fila")
                columna = correcto("columna")
                print("")
                posicion = [fila-1,columna-1,valor]
                
                if tateti.verificador(posicion[0],posicion[1]) == False:
                    print("elija otra fila y columna")
                    while tateti.verificador(posicion[0],posicion[1]) == False:

                        fila = correcto("fila")
                        columna = correcto("columna")
                        print("")
                        posicion = [fila-1,columna-1,valor]
                        
                        if tateti.verificador(posicion[0],posicion[1]) == False:
                            print("elija otra fila y columna")
                        else:
                            tateti.posicion = posicion 
                            print(tateti)
                            if tateti.ganador() == True:
                                print("ganador {}".format(valor))
                                exit()
                            valor = turno(valor)
                else:
                    tateti.posicion = posicion 
                    print(tateti)
                    if tateti.ganador() == "SI":
                        print("ganador {}".format(valor))
                        exit()
                    elif tateti.ganador() == "EMPATE":
                        print("Es un Empate")
                        exit()
                    valor = turno(valor)
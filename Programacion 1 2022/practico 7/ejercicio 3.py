class Jugador:
    def __init__(self) -> None:
        self._nombre = None
        self._cedula = None
        self._edad = None
        self._experiencia = None
        self._posicion = None

    @property
    def nombre(self):
        return self._nombre

    @property
    def cedula(self):
        return self._cedula

    @property
    def edad(self):
        return self._edad

    @property
    def experiencia(self):
        return self._experiencia

    @property
    def posicion(self):
        return self._posicion

    @nombre.setter
    def nombre(self,nombre):
        self._nombre = nombre

    @cedula.setter
    def cedula(self,cedula):
        self._cedula = cedula

    @edad.setter
    def edad(self,edad):
        self._edad = edad

    @experiencia.setter
    def experiencia(self,experiencia):
        self._experiencia = experiencia

    @posicion.setter
    def posicion(self,posicion):
        self._posicion = posicion

    def __str__(self) -> str:
        return "Nombre Completo:{}, Cedula:{}, Edad:{}, Años de Experiencia:{}, Posicion que Juega:{}".format(self._nombre, self._cedula, self._edad, self._experiencia, self._posicion)

class Equipo:
    def __init__(self) -> None:
        self._nombre = [None]
        self._titulares = [None]
        self._suplentes = [None]

    @property
    def nombre(self):
        return self._nombre

    @property
    def titulares(self):
        return self._titulares

    @property
    def suplentes(self):
        return self._suplentes

    @nombre.setter
    def nombre(self,nombre):
        self._nombre = nombre

    @titulares.setter
    def titulares(self,titular):
        self._titulares.append(titular)

    @suplentes.setter
    def suplentes(self,suplente):
        self._suplentes.append(suplente)
        
    def __str__(self) -> str:
        return " Nombre del equipo:{}\n Titulares:{}\n Suplentes:{}".format(self._nombre, self._titulares, self._suplentes)

if __name__ == "__main__":
    equipo = Equipo()
    jugador_1 = Jugador()
    jugador_2 = Jugador()

    nombre_equipo = input("ingrese el nombre de su equipo..")

    equipo.nombre = nombre_equipo

    jugador_1.nombre = "Diego bonora"
    jugador_1.cedula = 554874512    
    jugador_1.edad = 24
    jugador_1.experiencia = 10
    jugador_1.posicion = "pivot"

    jugador_2.nombre = "jorge gregor"
    jugador_2.cedula = 554236541    
    jugador_2.edad = 24
    jugador_2.experiencia = 6
    jugador_2.posicion = "alero"

    print(jugador_1)
    print(jugador_2)

    equipo.titulares = str(jugador_1)
    equipo.suplentes = str(jugador_2)

    print(equipo)
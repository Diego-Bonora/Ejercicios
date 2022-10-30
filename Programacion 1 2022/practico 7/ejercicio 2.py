class Persona:
    def __init__(self,Nombre=None ,Cedula=None ,Telefono=None ,Direccion=None, Tarjeta=None) -> None:
        self._Nombre = Nombre
        self._Cedula = Cedula
        self._Telefono = Telefono
        self._Direccion = Direccion
        self._Tarjeta = Tarjeta

    @property
    def Nombre(self):
        return self._Nombre

    @property
    def Cedula(self):
        return self._Cedula

    @property
    def Telefono(self):
        return self._Telefono

    @property
    def Direccion(self):
        return self._Direccion

    @property
    def Tarjeta(self):
        return self._Tarjeta

    @Nombre.setter
    def Nombre(self,nombre):
        self._Nombre = nombre

    @Cedula.setter
    def Cedula(self,cedula):
        self._Cedula = cedula

    @Telefono.setter
    def Telefono(self,telefono):
        self._Telefono = telefono

    @Direccion.setter
    def Direccion(self,direccion):
        self._Direccion = direccion

    @Tarjeta.setter
    def Tarjeta(self,tarjeta):
        self._Tarjeta = tarjeta

    def __str__(self) -> str:
        return "Nombre:{}, Cedula:{}, Telefono:{}, Direccion:{}, Tarjeta-->{}".format(self._Nombre, self._Cedula, self._Telefono, self._Direccion, self._Tarjeta)

class Tarjeta:
    def __init__(self, Banco=None, Numero=None, Verificador=None) -> None:
        self._Banco = Banco
        self._Numero = Numero
        self._Verificador = Verificador

    @property
    def Banco(self):
        return self._Banco

    @property
    def Numero(self):
        return self._Numero

    @property
    def Verificador(self):
        return self._Verificador

    @Banco.setter
    def Banco(self,banco):
        self._Banco = banco
    
    @Numero.setter
    def Numero(self,numero):
        self._Numero = numero

    @Verificador.setter
    def Verificador(self,verificador):
        self._Verificador = verificador

    def __str__(self) -> str:
        return "Banco:{}, Numero:{}, Verificador:{}".format(self._Banco, self._Numero, self._Verificador)

if __name__ == "__main__":
    persona = Persona()
    tarjeta = Tarjeta()

    banco = str(input("ingrese de que banco es su tarjeta.."))
    tarjeta.Banco = banco

    numero = int(input("ingrese el numero de su tarjeta.."))
    tarjeta.Numero = numero

    verificador = int(input("ingrese el numero verificador de la tarjeta.."))
    tarjeta.Verificador = verificador

    nombre = str(input("ingrese su nombre.."))
    persona.Nombre = nombre

    cedula = int(input("ingrese su cedula sin puntos ni guion.."))
    persona.Cedula = cedula

    telefono = int(input("ingrese su telefono sin espacios.."))
    persona.Telefono = telefono

    direccion = str(input("ingrese su direccion.."))
    persona.Direccion = direccion

    persona.Tarjeta = tarjeta

    print(persona)
class Persona:
    def __init__(self,Nombre=None ,Cedula=None ,Telefono=None ,Direccion=None):
        self._Nombre = Nombre
        self._Cedula = Cedula
        self._Telefono = Telefono
        self._Direccion = Direccion

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

    def __str__(self) -> str:
        return "Nombre:{}, Cedula:{}, Telefono:{}, Direccion:{}".format(self._Nombre, self._Cedula, self._Telefono, self._Direccion)

if __name__ == "__main__":
    persona = Persona()

    nombre = str(input("ingrese su nombre.."))
    persona.Nombre = nombre

    cedula = int(input("ingrese su cedula sin puntos ni guion.."))
    persona.Cedula = cedula

    telefono = input("ingrese su telefono sin espacios..")
    persona.Telefono = telefono

    direccion = str(input("ingrese su direccion.."))
    persona.Direccion = direccion

    print(persona)
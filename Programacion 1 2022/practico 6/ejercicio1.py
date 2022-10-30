class Bombilla:
    def __init__(self,estado) -> None:
        self.estado = estado

    def interruptor(self):
        if self.estado == "OFF":
            self.estado = "ON"
        else:
            self.estado = "OFF"


if __name__ == "__main__":
    luz = Bombilla("OFF")

while True:
    print("ingrece 1 si quiere encender la luz, ingrese 2 para salir")
    ingresar = int(input("ingrese un numero..."))
    if ingresar == 1:
        Bombilla.interruptor(luz)
        print(luz.estado)
    else:
        exit()


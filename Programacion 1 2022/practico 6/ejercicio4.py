from turtle import circle


class Sintonizador:
    def __init__(self,frecuencia) -> None:
        self.frecuencia = frecuencia

    def Up(self):
        if self.frecuencia == 108:
            self.frecuencia = 80
        else:
         self.frecuencia += 0.5

    def Down(self):
        if self.frecuencia == 80:
            self.frecuencia = 108
        else:
            self.frecuencia -= 0.5

if __name__ == "__main__":
    radio = Sintonizador(80)


while True:
    print("""
    ingrese 1 si quiere cambiar para la siguiente frecuencia
    ingrese 2 si quiere cambiar para la anterior frecuencia
    ingrese otro numero para salir del programa
    """)

    print(radio.frecuencia)

    numero = int(input("ingrese un numero..."))

    if numero == 1:
        Sintonizador.Up(radio)
    elif numero == 2:
        Sintonizador.Down(radio)

    else:
        exit()
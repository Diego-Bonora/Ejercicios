class CuentaCorriente:
    def __init__(self,saldo) -> None:
        self.saldo = saldo

    def Agregar_dinero(self,cantidad):
        self.saldo += cantidad

    def Sacar_dinero(self,cantidad):
        if self.saldo >= cantidad:
            self.saldo -= cantidad
        else:
            print("no hay suficiente saldo para retirar dinero de la cuenta")

if __name__ == "__main__":
    cuenta_1 = CuentaCorriente(0)

while True:
    print("""
    ingrese 1 si quiere ver su saldo
    ingrese 2 si quiere agregar dinero a la cuenta
    ingrese 3 si quiere retirar dinero a la cuenta
    ingrese otro numero si quiere salir del sistema
        """)

    numero = int(input("ingrese un numero..."))

    if numero == 1:
        print(cuenta_1.saldo)
    elif numero == 2:
        cantidad = int(input("ingrese la cantidad que quiere agregar..."))
        CuentaCorriente.Agregar_dinero(cuenta_1,cantidad)
        print(cuenta_1.saldo)
    elif numero == 3:
        cantidad = int(input("ingrese la cantidad que quiere agregar..."))
        CuentaCorriente.Sacar_dinero(cuenta_1,cantidad)
        print(cuenta_1.saldo)
    else:
        exit()
    
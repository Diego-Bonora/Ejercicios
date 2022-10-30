from dis import disco


def capacidad(capacidad):
    tamaño = [0,0,0,0]
    tamaño[0] = capacidad[0] * capacidad[1] * capacidad [2] * capacidad[3]
    tamaño[1] = tamaño[0] / 1024
    tamaño[2] = tamaño[1] / 1024
    tamaño[3] = tamaño[2] / 1024
    return tamaño

disco_duro = []

cilindros = int(input("ingrese la cantidad de cilindros que tiene "))
pistas = int(input("ingrese la cantidad de pistas que tiene "))
sectores = int(input("ingrese la cantidad de sectores que tiene "))
bytes = int(input("ingrese la cantidad de bytes que tiene "))

disco_duro.append(cilindros)
disco_duro.append(pistas)
disco_duro.append(sectores)
disco_duro.append(bytes)

print (capacidad(disco_duro))

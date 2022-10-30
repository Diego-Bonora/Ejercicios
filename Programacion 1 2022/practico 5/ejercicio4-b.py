def cuadrada(matriz):
    verificacion = False
    if len(matriz) == len(matriz[0]):
        verificacion = True
    return verificacion

matriz = [[1,2,3],[4,5,6],[7,8,9]]
T_F = cuadrada(matriz)

print(T_F)
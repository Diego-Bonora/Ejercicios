def columna(matriz,numero):
    columna = []
    for i in range(len(matriz)):
        columna.append(matriz[i][numero - 1])
    return columna

def duplicados(columna):
    T_F = False
    for i in range(len(columna)):
        if columna.count(columna[i]) > 1:
            T_F = True
    return T_F

def ingresar(matriz):
    numero = int(input("ingrese un numemro.."))
    while numero < 1 or numero > len(matriz):
        numero = int(input("ingrese un numero menor o igual a {} y mayor a 0..".format(len(matriz))))
    return numero
    
matriz = [[1,2,3],[4,5,6],[7,8,9]]

numero = ingresar(matriz)

columna_matriz = columna(matriz,numero)
print(columna_matriz)

T_F = duplicados(columna_matriz)
print(T_F)
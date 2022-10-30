def cantidad_columnas(matriz):
    mas_larga = 0
    for i in range(len(matriz)):
        if len(matriz[i]) >= mas_larga:
            mas_larga = i
    return mas_larga
        
matriz = [[1,2,3],[4,5,6],[7,8,9]]

mas_larga = cantidad_columnas(matriz)

print(len(matriz[mas_larga]))
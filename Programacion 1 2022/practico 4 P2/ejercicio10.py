def eliminar_caracteres(caracteres,cantidad):
    nueva_cadena = ""
    for i in range(cantidad,len(caracteres)):
        nueva_cadena = nueva_cadena + caracteres[i]
    print(nueva_cadena)

cadena = input("ingrese una cadena de caracteres")
cantidad = int(input("cuantos caracteres quieres eliminar?.."))

eliminar_caracteres(cadena,cantidad)
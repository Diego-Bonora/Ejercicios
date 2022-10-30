def letras_par(variable):
    for i in range(len(variable)):
        if i % 2 == 0:
            print(variable[i])


variable = input("ingrese una cadena de caracteres..")
letras_par(variable)

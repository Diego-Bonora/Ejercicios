def collect_data(user_info):
    if(user_info[3] == "Edad"):
        print("Ingrese su edad: ")
        user_info.append(int(input()))
    elif(user_info[3] == "Correo"):
        user_correo = input("Ingrese su correo: ")
        if(user_correo.index("@") == 5 ):
            user_info.append(user_correo)
        else:
            print(str_name)

try:
    # collect_data(["Nombre", "Apellido", "Contacto"])
    # collect_data(["Nombre", "Apellido", "Contacto", ""])
    # collect_data(["Nombre", "Apellido", "Contacto", "Edad"])
    collect_data(["Nombre", "Apellido", "Contacto", "Correo"])
except IndexError:
    print("la lista esta incompleta")
except NameError:
    print("no hay una clase con ese nombre")
except ValueError:
    print("el argumento es incorrecto")
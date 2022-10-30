nombre = input("ingrese su nombre..")
apellido = input("ingrese su apellido..")

nombre_r = "".join(reversed(nombre))
apellido_r = "".join(reversed(apellido))

print(nombre_r + ",",apellido_r)
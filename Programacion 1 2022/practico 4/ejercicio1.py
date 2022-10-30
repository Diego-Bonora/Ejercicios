def convercion(celcius):
    farenheit = 9/5 * celcius + 32 
    return farenheit

print("transformacion a farenheit")
celcius = int(input("ingrece grados celcius "))
print(celcius,"grados celcius son",convercion(celcius),"grados farenheit")
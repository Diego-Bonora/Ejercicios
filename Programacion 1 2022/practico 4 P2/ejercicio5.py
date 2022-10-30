numero = int(input("ingrese un numero positivo.."))

if numero <= 0:
    numero = numero * -1

numero_str = str(numero)
suma = 0
for i in range(len(numero_str)):
    suma+= int(numero_str[i]) 
    print(numero_str[i])  
  
print(suma)
print(numero)

while numero >= 0:
    numero-= suma
    if numero < 0:
        exit
    else:
        print(numero)
meses = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]

fecha = input("ingrese una fecha dd/mm/aa..")

dia=fecha[0:2]
mes = fecha[3:5]
year = fecha[6:10]

print("{} de {} del {}".format(dia,meses[int(mes) - 1],year))
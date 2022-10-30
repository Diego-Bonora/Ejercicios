def bisiesto(año):
     return año % 4 == 0 and año % 100 != 0 or año % 400 == 0

def verificar(año):
     if bisiesto(año) == False:
        diasMes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return diasMes
     else:
        diasMes = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return diasMes

def fecha(x):
    x=[]
    Año=int(input("Año:"))
    Mes=int(input("Mes:"))
    if Mes > 12:
        print("ERROR")
        exit()
    Dia=int(input("Dia:"))  
    diasMes=verificar(Año)
    if Dia > diasMes[Mes]:
        print("ERROR")
        exit()
    x.append(Año)
    x.append(Mes)
    x.append(Dia)
    return x

def SumaFechas(mayor,menor):
    diasMes = verificar(menor[0])
    finAño = 0

    finMes = diasMes[menor[1]] - menor[2]
    print(finMes)
    i = menor[1] + 1 
    while i <= 12:
        finAño+= diasMes[i]
        i+= 1 

    SumTotal = finAño + finMes

    SumaAños = menor[0] + 1
    SumaDias = 0

    while SumaAños < mayor[0]:
        if bisiesto(SumaAños) == False:
            SumaDias= SumaDias + 365
            SumaAños+= 1
        else:
            SumaDias= SumaDias + 366
            SumaAños+= 1
        
    SumTotal+= SumaDias

    diasMes = verificar(mayor[0])
    FinMeses = 0
    i = 1
    while i < mayor[1]:
        FinMeses+= diasMes[i]
        i+= 1
    FinMeses+= mayor[2]
    SumTotal+= FinMeses

    return SumTotal

def SumaFechasIguales(mayor,menor):

    diasMes = verificar(menor[0])
    total=0
    i = menor[1]

    total=diasMes[i] - menor[2]
    menor[2] = 0
    i+= 1

    if i < mayor[1]:
        while i < mayor[1]:
            total+=diasMes[i]
            i+= 1
        total+= mayor[2] - menor[2]
        return total

    else:
        total+= mayor[2] - menor[2]
        return total

fechaTotal=[]
fecha1=[]
fecha2=[]

fecha1=fecha(fecha1)
fecha2=fecha(fecha2)

print("Fecha 1 es:",fecha1)
print("Fecha 2 es:",fecha2)

if fecha1[0] > fecha2[0]:
    fechaTotal=(SumaFechas(fecha1,fecha2))
    print("1")
elif fecha2[0] > fecha1[0]:
    fechaTotal=(SumaFechas(fecha2,fecha1))
    print("2")
elif fecha1[1] > fecha2[1]:
    fechaTotal=SumaFechasIguales(fecha1,fecha2)
    print("3")
elif fecha2[1] > fecha1[1]:
    fechaTotal=SumaFechasIguales(fecha2,fecha1)
    print("4")
else:
    if fecha1[2] > fecha2[2]:
        fechaTotal = fecha1[2] - fecha2[2]
    else:
        fechaTotal = fecha2[2] - fecha1[2]
print("entre",fecha1,"y",fecha2,"hay",fechaTotal,"dias")
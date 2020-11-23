numero=1
i=0
suma=0
while numero==True:
    xstr=input("Introduzca un número:")
    numero=bool(xstr)
    if xstr!="":
        i=i+1
        suma=suma+float(xstr)
        media=suma/i
    
print("La media aritmética es: ",media," y la suma: ",suma)


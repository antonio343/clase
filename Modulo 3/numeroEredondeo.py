e=1
i=1
factorial=1
fraccion=0
decimal=int(input("¿Cuantos decimales quieres?"))

while (i<50):
    factorial=factorial*i
    fraccion=1/factorial
    i=i+1
    e=e+fraccion

x=round(e, decimal)
print("El valor del número e es: ",x)
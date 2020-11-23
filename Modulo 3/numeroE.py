e=1
i=1
factorial=1
fraccion=0
error=input("¿Que precisión quieres?")
error=1/(10**error)

errorAnt=0
fin = False
while (not fin):
    factorial=factorial*i
    fraccion=1/factorial
    errorAnt=e
    
    e=e+fraccion
    i=+1
    if((e-errorAnt)< float(error)):
        fin = True
x=round(decimales: e)
print("El valor del número e es: ",e)

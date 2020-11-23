#Hay que crear una variable donde esta el objetivo, una lo que se va
# suman y otra donde esta lo que queda por cambiar
dinero=100
acumulado=0
resto=100
#Variable lista con billetes
billetes=[[3,20],[5,10],[2,5]]
#variable cambio
cambio2=[[0,20],[0,10],[0,5]]
cambio=cambio2.copy()

#soluciones posibles
solucion=((0,0,0),(0,0,0),(0,0,0))

i=0
    
while resto > billetes[i][1] and billetes[i][1]>0 and resto>dinero:
    billetes[i][1]-=1
    cambio[i][1]+=1
    acumulado=acumulado+ billetes[i][1]*billetes[i][0]
    resto=dinero - acumulado
    cambio[i][0].append(1)
i+=1





l=input("Dame una serie de numeros: ")

l1=l.split()
lista=[]
for e in l1:
    lista.append(float(e))

listado=lista
listado.sort()
cifras=len(lista)
suma=sum(listado)
media=(suma/cifras)

if cifras%2==0:
    a=int(cifras/2)
    mediana=(listado[a]+listado[a+1])/2
    print("La suma es: ",suma,", la media: ",media," y la mediana: ",mediana)
else:
    print("La suma es: ",suma,", la media: ",media," y la mediana",listado[cifras//2])





inicio=int(input("Dame el valor inicial: "))
fin=int(input("Dame el valor final: "))
l=input("Que frase quieres despiezar?")
# salto=int(input("Dame el intervalo: "))

# l=[]
# b=inicio

# while b<fin:
#     l.append(b)
#     b=b+salto


# print (l)
i=inicio
while i-1<fin:
    print (i)
    i+=1
i=inicio
if i%2 ==0:
    i+=1
while i-1<fin:
    print(i)
    i+=2
i=0
for letra in l:
    print (l[i])
    i+=1

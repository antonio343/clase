m = [[1,2],[3,4],[5,6]]
n = [[5,10,15,0],[0,0,20,0]]



# filas y columnas del resultado
a = len(m)  # filas de m
filas = a
d = len(n[0])  # columnas de n
columnas = d

b = len(m[0])  # columnas de m
c = len(n)  # filas de n

if b != c:
    print("Error, no calculable")
    exit(1)
#generar matriz resultado vacia
m3 = []
# for i in range(a):
#     x = []
#     for j in range(b):
#         x.append(0)
#     m3.append(x)
# calcular r[0][0] le llamo x
x = 0
for k in range(len(m)):
    for j in range(len(n[0])):
        x=[]
        for i in range(b):
            sumando = m[k][i] * n[i][j]
            x=x+sumando
        m3.append(x)
    print(m3)
    print(x)    
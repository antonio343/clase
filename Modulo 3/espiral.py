
import turtle


t = turtle.Turtle()

t.up()  # lápiz "arriba" (no pintar)
t.goto(0, 0)  # movimiento directo a coordenadas, por sencillez (no es lo habitual)
t.down()



vueltas=int(input("Cuantas vueltas quieres?"))
lado=1
radio=5
i=0
a=1

#Cuenta las vueltas que hace
while a<vueltas:
    #hace el medio circulo en avances de grado a grado
    while(i<180):
        t.forward(a*lado)
        t.right(1)
        i+=1
    i=0
    a+=1

turtle.mainloop()

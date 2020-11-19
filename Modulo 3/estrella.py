import turtle


t = turtle.Turtle()

t.up()  
t.goto(-150, 150)  
t.down()

SIDE_LENGTH=50
puntas=int(input("Cuantas puntas quieres?"))

if(puntas%2 ==0):
    a=360/(2*puntas)
    b=90
    c=180-b-a
    uno=c/2
    dos=180-b-uno
    i=2
    while(i!= puntas):
        t.forward(SIDE_LENGTH)
        t.right(180-uno)
        t.forward(SIDE_LENGTH)
        t.left(dos)
        i+=1
    
else:
    angle=360/(2*puntas)
    i=0
    while (i!= puntas):
        t.forward(SIDE_LENGTH)
        t.right(180-angle)
        i+=1
# === FIN DE PARTE A MODIFICAR ===

# Esto es necesario para que la ventana no se cierre al final. Dejar tal cual
turtle.mainloop()

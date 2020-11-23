#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def cuadrados(l,n):
    import turtle

    t = turtle.Turtle()
    t.up()  # lápiz "arriba" (no pintar)
    t.goto(-150, 150)  # movimiento directo a coordenadas, por sencillez (no es lo habitual)
    t.down()

    SIDE_LENGTH = l
    angle = 90
    i=0
    while i<n:
        t.forward(l)
        t.right(angle)
        t.forward(l)
        t.right(angle)
        t.forward(l)
        t.right(angle)
        t.forward(l)
        t.right(angle)
        t.up()
        t.forward(2*l)
        t.down()
        i+=1

    turtle.mainloop()
def poligonos(l,n):
    import turtle

    t = turtle.Turtle()
    t.up()  # lápiz "arriba" (no pintar)
    t.goto(-150, 150)  # movimiento directo a coordenadas, por sencillez (no es lo habitual)
    t.down()

   
    angle = 360/n
    i=0
    a=0
    while i<n:
        while a<n:
            t.forward(l)
            t.right(angle)
            a+=1
        a=0
        t.up()
        t.forward(2*l)
        t.down()
        i+=1
        
    turtle.mainloop()
def espiral(l,n):
    import turtle

    t = turtle.Turtle()
    t.up()  # lápiz "arriba" (no pintar)
    t.goto(-150, 150)  # movimiento directo a coordenadas, por sencillez (no es lo habitual)
    t.down()

    SIDE_LENGTH = l
    angle = 90
    angle2=360/n
    i=0
    while i<n:
        t.forward(l)
        t.right(angle)
        t.forward(l)
        t.right(angle)
        t.forward(l)
        t.right(angle)
        t.forward(l)
        t.right(angle)
        t.right(angle2)
        
        i+=1

    turtle.mainloop()

# cuadrados(20,5)
# poligonos(20,5)
espiral(20,15)
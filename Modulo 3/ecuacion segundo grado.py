calculo =-1
while calculo <0:
    xstr = input("Dame el parametro A de la ecuacion")
    if (xstr.isdigit()):
        a=int(xstr)
        xstr = input("Dame el parametro B de la ecuacion")
        if (xstr.isdigit()):
            b=int(xstr)
            xstr = input("Dame el parametro C de la ecuacion")
            if (xstr.isdigit()):
                c=int(xstr)
                calculo= b*b-4*a*c
                if calculo < 0:
                    print("Los parametros no son válidos")
x1=(-b+(calculo)**0.5)/(2*a)
x2=(-b-(calculo)**0.5)/(2*a)
print("Las soluciones son:",x1,x2)
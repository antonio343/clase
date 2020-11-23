cadena ="Escribe lo que que quieras quieras"
subcadena=""
for i in cadena.split():
    if subcadena.find(i) >=0:
        print(i," está repetida")
    subcadena = subcadena +" "+ i

print(subcadena)
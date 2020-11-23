def area_circunferencia(r):
    area=3.1416*r*r
    return(area)
def palabra_larga(lista):
    l=len(lista)
    i=0
    mayor=""
    while i<l:
        a=len(lista[i])
        if len(mayor)<a:
            mayor=lista[i]
        i+=1
    return mayor
def longitud_palabras(lista):
    longitud=0
    for l in lista:
        longitud=longitud+len(l)
        
    return longitud
print(area_circunferencia(5))
a=["hola","mundo"]
print(palabra_larga(a))
print(longitud_palabras(a))
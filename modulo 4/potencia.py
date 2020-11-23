def potencia(base,exponente):
    if exponente <0:
        return 1/potencia(base,-exponente)
    if exponente ==0:
        return 1
    else:
        return base*potencia(base,exponente-1)
    
   

print( potencia(5,3))
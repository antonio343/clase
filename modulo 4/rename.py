def irpf(salario,base=12.5,prorrateo=0):
    """Entra el salario y la base, opcionalmente un parametro para prorratear
    Si no se da el valor de la bas3e por defecto es 12.5"""
    if type(salario)==float and type(base)==float:
        if prorrateo==True:
            return (salario*(1+2/12))*(base/100)
        elif prorrateo==False:
            return salario*(base/100)
    else:
        return None
    

print(irpf(100.0,4.0))

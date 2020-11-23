#PEdir un numero a convertir y base, se debe escribir el numero en la nueva
#La base original es 10 y las nuevas bases validas son de 2 a 9

valor=int(input("¿Qué número quieres convertir?"))
base=int(input("¿Que base quieres?"))
if(base<2 or base>9):
    base=int(input("Esa base no puede hacerse ¿Que base quieres?"))

def cambio_de_base(valor, base):
    
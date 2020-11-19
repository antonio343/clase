numero=int(input("¿Que número quieres comprobar?"))
denominador=2
resto=2.1
while denominador < resto:
    resto= numero%denominador
    if resto==0:
        print("El numero no es primo")
    denominador+=1
print("El numero es primo")
        


    
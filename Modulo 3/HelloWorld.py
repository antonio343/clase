import sys

print("Hello world, I am",sys.executable, sys.version)

x=input("Dame un numero mayor que cero: ")
x = int(x)

if x < 0:
    print('Negative changed to zero')
    x = 0
print(f"El valor final de x es: {x}")
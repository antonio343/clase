xstr = input("Dame un n8umero mayor que cero")
x=int(xstr)
if x < 0:
    print('Negative changed to zero')
    x = 0
else:
    if x == 0:
        print('Zero')
    elif x == 1 or x < 2.0:
        print('Single')
        if x==1:
            print('Es un 1 redondo')
    else:
        print('More')

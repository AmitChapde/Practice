def isSquare(x1, y1, x2,  y2,  x3,  y3,  x4,  y4):
    flag1=0
    flag2=0
    if ((x4-x1)==(x2-x3)):
        flag1=1
    if ((y4-y1)==(y2-y3)):
        flag2=1
    if flag1 & flag2:
        print("Its A Square")
    else:
        print("Its not ")

k=isSquare(20,10,10,20,20,20,10,10)

import math
def powerofanother(x,y):
    for i in range(1,y+1):
        if x**i==y:
            return 1
        else:
            return 0

k=powerofanother(2,8)
print(k)


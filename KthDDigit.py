import math

def KthDigit(a,b,k):
    m=int(math.pow(a,b))
    count = 0 
    while (m>0 and count<k):
        Num = m%10
        count += 1 
        if count==k:
            return Num

        m //= 10

        
p=KthDigit(5,2,2)
print(p)
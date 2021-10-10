def Revdigits(n):
    rnum=0
    while n != 0:
        digit=n%10
        rnum=rnum*10+digit
        n //= 10
    return rnum


a=Revdigits(1345)
print(a)
    
def sumofdigits(n):
    temp=n
    sum=0
    while temp>0:
        digit=temp%10
        sum+=digit
        temp //=10

    
    return sum



a=sumofdigits(2100)
print(a)      

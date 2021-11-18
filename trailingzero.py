def trailingzero(n):
    fact=1
    count=0
    for i in range(1,n+1):
        fact=fact*i
    
    while(fact>0):
        k=fact%10 #it will return k=0
        fact=fact//10#example if fact is 120 it will become 12
        if k==0:
            count+=1
        if k!=0:
            break
    return count

    
    

k=trailingzero(100)
print(k)




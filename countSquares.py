import math
def Countsquares(n):
    count=0
    for i in range(1,n+1):
        srt=math.sqrt(i)
        if srt*srt==i and i<n:
            count+=1
    return count


k=Countsquares(3)
print(k)

            
            

            



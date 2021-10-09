class Cnumber:
    def closestNumber(self,n:int,m:int):
         # Find the quotient
        q=int(n/m)
        # 1st possible closest number
        n1=m*q

        # 2nd possible closest number
        if n*m >0:
            n2=(m*(q+1))
        else:
            n2=(m*(q-1))

        # if true, then n1 is the required closest number
        if (abs(n-n1) < abs(n-n2)):
            return n1

        # else n2 is the required closest number
        return n2 



K=Cnumber()
l=K.closestNumber(-15,6)
print(l)



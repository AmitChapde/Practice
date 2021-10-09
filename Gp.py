import math

class Answer:
    def Nth_term(self, a:int, r:int, n:int):
        c=int(math.pow(r,n-1))
        return a*c







a=Answer()
b=a.Nth_term(2,2,4)
print(b)
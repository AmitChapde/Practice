class Solution:
    def nthTermOfAP(self,A1:int,A2:int,N:int):
        return A1+(N-1)*(A2-A1)





a=Solution()
b=a.nthTermOfAP(2,3,4)
print(b)



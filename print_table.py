class solution:
    #by putting collen infront of the parameter we can specify the datatpe of the parameter
    def getTable(self,N:int):
        for i in range(1,11):
            print(f"{N*i}")



#driver code which needs to be written in coding interviews
# if __name__=='__main__':
#     t=int(input())
#     for _ in range(t):
#         N=int(input())
#         ob=solution()
#         ans=ob.getTable(N)
#         for i in ans:
#             print(i,end='')
#         print()

obj=solution()
ans=obj.getTable(5)
print(ans)
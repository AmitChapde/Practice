def kth_min(A,k):
    A.sort()
    return A[k-1]


A=[2,112,1344,134,545,566,573]
k=1
m=kth_min(A,k)
print(m)
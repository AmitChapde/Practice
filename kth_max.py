def kth_max(A,k):
    A.sort(reverse=True)
    return A[k-1]


A=[2,112,1344,134,545,566,573]
k=1
m=kth_max(A,k)
print(m)
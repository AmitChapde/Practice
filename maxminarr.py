def maxmin(A):
    n=len(A)
    max=A[0]
    min=A[0]
    for i in range(n):
        if A[i]>max:
            max=A[i]
        if A[i]<min:
            min=A[i]
    return max,min


A=[5,6]
k=maxmin(A)
print(k)

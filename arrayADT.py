class ArrayOperations:
    def binarysearch_iterative(self,A, key):
        l = 0
        r = len(A)-1
        while l <= r:
            mid = (l + r) // 2
            if key == A[mid]:
                return mid
            elif key < A[mid]:
                r = mid - 1
            elif key > A[mid]:
                l = mid + 1
        return -1
    
    def AddElement(self,e,index):
        A.insert(e,index)

    def RemoveElement(self,e):
        A.remove(e)

A = [15,21,47,84,96]
a=ArrayOperations()
found =a.binarysearch_iterative(A,84)
print('Result: ',found)
a.AddElement(3,1)
print(A)
a.RemoveElement(1)
print(A)

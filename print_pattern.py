def print_pat(n,counter):
    for i in range(n,0,-1):
        print(i,end='')
        for j in range(1,n-counter):
            print(i,end='')
print("\n")

def print_times(times):
    s=0
    while s<times:
        print_pat(times,s)
        s+=1
        print("\n")
    



print_times(3)
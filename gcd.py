import math
def calc_gcd(a,b):
    #choose smaller number
    if a>b:
        smaller=b
    else:
        smaller=a
    for i in range(1,smaller+1):
        if  ((a%i==0) and (b%i==0)):
            gcd=i
    return gcd


n1=98
n2=56

print(f"the gcd of {n1} and {n2} is {calc_gcd(n1,n2)}")


k=math.gcd(n1,n2)
print("gcd:",k)

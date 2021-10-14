def arraygcd(x,y):
    while(y):
        x,y=y,x%y

    return x

l=[2,4,6,8,16]

num1=l[0]
num2=l[2]
gcd=arraygcd(num1,num2)

for i in range(2,len(l)):
    gcd=arraygcd(gcd,l[i])

print(gcd)
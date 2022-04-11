from pprint import pp


def Binarytodecimal(n):
    num=n;
    dvalue=0;

    base=1 
    temp=num;
    while(temp):
        last_digit=temp%10
        temp=int(temp/10)
        dvalue+=last_digit*base
        base*=2
    return dvalue

a=Binarytodecimal(101)
print(a)
print("present");
class ans:
    def ArmstrongNumber(self,num):
        sum=0
        temp=num
        while temp>0:
            digit = temp % 10
            sum = sum + digit ** 3
            temp = temp // 10

        if num==sum:
            return("Yes")
        else:
            return("No")


a=ans()
b=a.ArmstrongNumber(371)
print(b)
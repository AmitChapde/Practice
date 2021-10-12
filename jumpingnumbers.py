
class Queue:
    def __init__(self):
        self._lst=[]

    def __len__(self):
        len(self._lst)==0
    
    def isempty(self):
        return len(self._lst)==0

    def Enqueue(self,e):
        self._lst.append(e)

    def Dequeue(self):
        if self.isempty():
            print("Queue is empty")
            return
        return self._lst.pop(0)

# Prints all jumping numbers smaller than or equal to
# x starting with 'num'. It mainly does BFS starting
# from 'num'.

def BFS(x,num):
    q=Queue()
    q.Enqueue(num)

    # BFS starting from 1
    while (not q.isempty()):
        num=q.Dequeue()

        if num<=x:
            print(str(num),end=" ")
            last_digit=num%10

        # If last digit is 0, append next digit only
            if last_digit == 0:
                q.Enqueue((num * 10) + (last_digit + 1))

        #if last digit is 9,append next digit only 
            elif last_digit==9:
                q.Enqueue((num * 10)+(last_digit - 1))
        
         # If last digit is neighter 0 nor 9, append
            # both previous digit and next digit
            else:
                q.Enqueue((num * 10) + (last_digit - 1))
                q.Enqueue((num * 10) + (last_digit + 1))



# Prints all jumping numbers smaller than or equal to
# a positive number x
def printjumping(x):
    print(str(0),end=" ")
    for i in range(1,10):
        BFS(x,i)


x=40
printjumping(x)

   




    
    
        
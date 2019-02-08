class stack_fullerror(Exception):
    pass
class stack_emptyerror(Exception):
    pass

class Stack_array:
    def __init__(self,max_size):
        self.items=[None]*max_size
        self.count=0
   
    def is_empty(self):
        return self.count==0

    def size(self):
        return self.count

    def is_full(self):
        return self.count==len(self.items)

    def push(self,data):
        if self.is_full():
            raise stack_fullerror('Overflow')

        self.items[self.count]=data
        self.count+=1

    def pop(self):
        if self.is_empty():
            raise stack_emptyerror('underflow')
        x=self.items[self.count-1]
        self.items[self.count-1]=None
        self.count-=1
        return x

    def display(self):
        print(self.items)


    
obj=Stack_array(10)
while True:
    print("1.Push:")
    print("2.Pop:")
    print("3.Display")
    print("4.exit")
    i=int(input('enter a choice :'))
    if i==1:
        data1=int(input('enter the data :'))
        obj.push(data1)
    elif i==2:
        print(obj.pop())
    elif i==3:
        obj.display()
    
    elif i==4:
        break

            
class Stack_Empty_Error(Exception):
    pass
class Node:
    def __init__(self,value):
        self.info=value
        self.link=None

class Stack_linked_list:
    def __init__(self):
        self.top=None

    def is_empty(self):
        return self.top==None

    def size(self):
        if self.is_empty():
            return 0
        p=self.top
        count=0
        while p is None:
            p=p.link
            count+=1
        return count

    def push(self,data):
        temp=Node(data)
        temp.link=self.top
        self.top=temp
        

    def pop(self):
        if self.is_empty():
            raise Stack_Empty_Error("Stack Empty")
        x=self.top.info
        self.top=self.top.link
        return x

    def display(self):
        if self.is_empty():
            print('stack empty')
        p=self.top
        while p is not None:
            print(p.info," ")
            p=p.link

obj=Stack_linked_list()
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

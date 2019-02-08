class  Node:
    def __init__(self,data):
        self.info=data
        self.prev=None
        self.next=None

class double_linked_list:
    def __init__(self):
        self.start=None

    def display_list(self):
        if self.start is None:
            print('list is empty')
            return
        
        p=self.start
        while p is not None:
            print(p.info," ",end="")
            p=p.next
        print()

    def insert_at_start(self,x):
        temp=Node(x)
        if self.start is None:
            self.start=temp
            temp.next=None
            temp.prev=None
            return
        
        temp.next=self.start.next
        self.start=temp
        temp.prev=None

    def insert_at_end(self,x):
        temp=Node(x)
        if self.start is None:
            self.start=temp
            return
        p=self.start
        while p.next is not None:
            p=p.next
        p.next=temp
        temp.prev=p
        temp.next=None


    def create_list(self):
        n=int(input('enter the no.  of nodes :'))
        for i in range(n):
            print('Node ',i)
            data=int(input('enter the data : '))
            self.insert_at_end(data)

    
obj=double_linked_list()
while True:
    print("1.Create a list :")
    print("2.Display a list :")
    print("3.exit")
    i=int(input('enter a choice :'))
    if i==1:
        obj.create_list()
    elif i==2:
        obj.display_list()
    elif i==3:
        break




            
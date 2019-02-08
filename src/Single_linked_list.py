class Node:
    def __init__(self,value):
        self.info=value
        self.link=None

class Single_linked_list:
    def __init__(self):
        self.start=None
    
    def display_list(self):
        if self.start is None:
            print('Empty list')
        else:
            print('List:')
            p=self.start
            while p is not None:
                print(p.info," ",end=" ")
                p=p.link
            print()
    
    def count_nodes(self):
        count=0
        p=self.start
        while p is not None:
            count+=1
            p=p.link
        print('no of nodes: ',count)
    
    def search(self,num):
        position=1
        p=self.start
        while p is not None:
            if p.info==num:
                break
            else:
                position+=1
        print('element found at position : ',num)

    def insert_at_begining(self,data):
        temp=Node(data)
        temp.link=self.start
        self.start=temp
    
    def insert_at_end(self,data):
        temp=Node(data)
        if self.start is None:
            self.start=temp
            return
        
        p=self.start
        while p.link is not None:
            p=p.link
        temp.link=None
        p.link=temp
            

    def create_list(self):
        num=int(input('enter the no. of nodes : '))
        if num==0:
            return
        for i in range(0,num):
            print('node: ',i)
            data=int(input('enter the data : '))
            self.insert_at_end(data)

    def insert_after(self,x,data):
        p=self.start
        while p is not None:
            if p.info==x:
                break
            p=p.link
        if p is None:
            print('element ',x,'not found')
        else:
            temp=Node(data)
        temp.link=p.link
        p.link=temp

    def insert_before(self,x,data):
        p=self.start
        if p is None:
            print('empty list')
        else:    
            while p is not None:
                if p.link.info==x:
                    break
                p=p.link
            if p is None:
                print('element ',x,'not found')
            else:
                temp=Node(data)
                temp.link=p.link
                p.link=temp
    #def insert_at_pos(self,data,pos):
     #   p=self.start
      #  i=1
       # while i<pos and p is not None:
        #    if i==pos:
         #       break
          #  p=p.link
           # i+=1

    def reverse_list(self):
        prev=None
        p=self.start

        while p is not None:
            next=p.link
            p.link=prev
            prev=p
            p=next
        self.start=prev
    
    def bubble_sort_exdata(self):
        end=None
        while end != self.start.link:
            p=self.start
            while end != p.link:
                q=p.link
                if p.info > q.info:
                    p.info,q.info=q.info,p.info
                p=p.link
            end=p

    def bubble_sort_exlinks(self):
        end=None
        while end != self.start.link:
            r=p=self.start
            while end != p.link:
                q=p.link
                if p.info > q.info :
                    p.link=q.link
                    q.link=p
                    if p != self.start:
                        r.link=q
                    else:
                        self.start=q
                    p,q=q,p
                r=p
                p=p.link
            end=p

    #def merge_sort

    def has_cycle(self):
        if self.find_cycle() is None:
            return False
        else:
            return True

    def find_cycle(self):
        if self.start is None or self.start.link is None:
            return None
        else:
            slowr=self.start
            fastr=self.start
            while fastr is not None or fastr.link is not None:
                slowr=slowr.link
                fastr=fastr.link.link
                if slowr==fastr:
                    return slowr
            return None

    def remove_cycle(self):
        p=self.find_cycle()
        q=self.find_cycle()
        cycle_lenght=1
        q=q.link
        while q!=p:
            cycle_lenght+=1
            q=q.link
        length_rem=0
        r=self.start
        while r!=p:
            r=r.link
            p=p.link
            length_rem+=1
        total_length=length_rem+cycle_lenght
        s=self.start
        for i in range(0,total_length-1):
            s=s.link

        s.link=None



        

obj=Single_linked_list()
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

            




class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def append(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        temp=self.head
        while temp.next!=None:
            temp=temp.next
        temp.next=new_node
    def display(self):
        temp=self.head
        while temp:
            print(temp.data,end='->')
            temp=temp.next
        print("None")
    def cnt(self):
        co=0
        s=0
        temp=self.head
        while temp:
            co+=1
            if temp.data%2==0:
                s+=temp.data
            temp=temp.next
        print(co)
        print(s)
    def prime(self):
        temp=self.head
        while temp:
            flag=0
            for i in range(2,temp.data//2):
                if temp.data%i==0:
                    flag=1
                    break
            if flag==1:
                print(temp.data,"Not prime")
            else:
                print(temp.data,"Prime")
            temp=temp.next
l1=LinkedList()
l1.append(7)
l1.append(10)
l1.append(3)
l1.append(6)
l1.append(14)
l1.display()
l1.cnt()
l1.prime()
def printt(q):
    t=q.head
    for i in range(q.length):
        print(str(t.val)+"->",end="")
        t=t.next

class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
        
class Queue:
    def __init__(self):
        self.length=0
        self.head=None
        self.tail=None
        
    def enqueue(self,val):
        n=Node(val)
        if(self.length==0):
            self.head=n 
            self.tail=n 
        else:
            self.tail.next=n
            self.tail=n
        self.length+=1
        return self
        
    def dequeue(self):
        if(self.length==0):
            return None
        elif(self.length==1):
            t=self.head
            self.head=None
            self.tail=None
            self.length-=1
            return t 
        else:
            t=self.head
            self.head=self.head.next
            self.length-=1
            return t
        
q=Queue()
q.enqueue(4)
q.enqueue(5)
q.enqueue(4)
q.enqueue(5)
q.enqueue(4)
q.enqueue(5)

v=q.dequeue()
print(v.val)
printt(q)
        
def printt(s):
    t=s.tos
    for i in range(s.length):
        print(str(t.val)+"->",end="")
        t=t.next

class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

class Stack:
    def __init__(self):
        self.length=0
        self.tos=-1
        
    def push(self,val):
        n=Node(val)
        if(self.length==0):
            self.tos=n 
        else:
            n.next=self.tos
            self.tos=n  
        self.length+=1 
        return self.length
    
    def pop(self):
        if(self.length==0):
            return None
        else:
            t=self.tos
            self.tos=self.tos.next
            self.length-=1
            return t
        
s=Stack()

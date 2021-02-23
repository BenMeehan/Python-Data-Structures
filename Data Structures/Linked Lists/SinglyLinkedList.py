class Node:
  def __init__(self,val):
    self.val=val
    self.next=None

class SinglyLinkedList:
  def __init__(self):
    self.head=None
    self.tail=None
    self.length=0
  
  def push(self,val):
    n=Node(val)
    if(self.head==None):
      self.head=n
      self.tail=n
    else:
      self.tail.next=n
      self.tail=n
    
    self.length+=1
    return self

  def unshift(self,val):
    n=Node(val)
    if(self.length==0):
      self.head=n
      self.tail=n
    else:
      n.next=self.head
      self.head=n
    self.length+=1
    return self
  
  def pop(self):
    if(self.length==0):
      return None
    if(self.length==1):
      t=self.tail
      self.head=None
      self.tail=None
      self.length-=1
      return t
    else:
      current=self.head
      temp=current
      while(current.next!=None):
        temp=current
        current=current.next
      
      self.tail=temp
      self.tail.next=None
      self.length-=1
      if(self.length==0):
        self.head=None
        self.tail=None
      return current

  def shift(self):
    if(self.length==0):
      return None
    temp=self.head
    self.head=self.head.next
    self.length-=1
    if(self.length==0):
        self.tail=None
    return temp

  def get(self,index):
    temp=self.head
    if(index<0 or index>self.length-1):
      return None
    else:
      i=0
      while(i!=index):
        temp=temp.next
        i+=1
      return temp.val
  
  def set(self,index,new_val):
    temp=self.head
    if(index<0 or index>self.length-1):
      return False
    else:
      i=0
      while(i!=index):
        temp=temp.next
        i+=1
    temp.val=new_val
    self.length+=1
    return True

  def insert(self,index,val):
    temp=self.head
    if(index<0 or index>self.length+1):
      return False
    elif(index==self.length+1):
      self.push(val)
      return True
    elif(index==0):
      self.unshift(val)
    else:
      n=Node(val)
      i=0
      while(i!=index-1):
        temp=temp.next
        i+=1
      front=temp.next
      temp.next=n
      n.next=front
      self.length+=1
      return True
  
  def remove(self,index):
    temp=self.head
    if(index<0 or index>self.length):
      return False
    elif(index==self.length-1):
      return self.pop()
    elif(index==0):
      return self.shift()
    else:
      i=0
      while(i!=index-1):
        temp=temp.next
        i+=1
      val=temp.next
      temp.next=temp.next.next
      self.length-=1
      return val

  def reverse(self):
    node=self.head
    self.head=self.tail
    self.tail=node

    prev=None
    next=None

    for i in range(0,self.length):
      next=node.next
      node.next=prev
      prev=node
      node=next

    return self

def printt(dl):
  t=dl.head
  for i in range(dl.length):
    print(str(t.val)+"<->",end="")
    t=t.next
  print("\n")

class Node:
  def __init__(self,val):
    self.val=val
    self.next=None
    self.prev=None

class DoublyLinkedList:
  def __init__(self):
    self.length=0
    self.head=None
    self.tail=None

  def push(self,val):
    n=Node(val)
    if self.length==0:
      self.head=n
      self.tail=n
    else:
      self.tail.next=n
      n.prev=self.tail
      self.tail=n
    self.length+=1
    return self

  def pop(self):
    if(self.length==0):
      return None
    elif(self.length==1):
      t=self.tail
      self.head=None
      self.tail=None
      self.length-=1
      return t
    else:
      tail=self.tail
      prev=self.tail.prev
      tail.prev=None
      prev.next=None
      self.tail=prev
      self.length-=1
      return tail

  def shift(self):
    if(self.length==0):
      return None
    else:
      old=self.head
      if(self.length==1):
        self.head=None
        self.tail=None
        self.length-=1
        return old
      else:
        self.head=old.next
        self.head.prev=None
        old.next=None
        self.length-=1
        return old

  def unshift(self,val):
    n=Node(val)
    if(self.length==0):
      self.head=n
      self.tail=n
    else:
      n.next=self.head
      self.head.prev=n
      self.head=n
    self.length+=1
    return self

  def at(self,index):
    t=self.get(index)
    return t.val

  def get(self,index):
    if(index<0 or index>=self.length):
      return None
    else:
      if(index<=self.length//2):
        counter=0
        t=self.head
        while(counter!=index):
          t=t.next
          counter+=1
        return t
      else:
        counter=self.length-1
        t=self.tail
        while(counter!=index):
          t=t.prev
          counter-=1
        return t

  def set(self,index,val):
    t=self.get(index)
    if(t!=None):
      t.val=val
      return True
    else:
      return False

  def insert(self,index,val):
    if(index<0 or index>self.length):
      return None
    elif(index==0):
      self.unshift(val)
    elif(index==self.length):
      self.push(val)
    else:
      n=Node(val)
      next=self.get(index)
      prev=next.prev
      prev.next=n
      next.prev=n
      n.prev=prev
      n.next=next
      self.length+=1
    return True

  def remove(self,index):
    if(index<0 or index>=self.length):
      return False
    elif(index==0):
      n=self.get(0)
      self.shift(index)
    elif(index==self.length-1):
      n=self.get(index)
      self.pop(index)
    else:
      n=self.get(index)
      prev=n.prev
      next=n.next
      prev.next=next
      next.prev=prev
      n.prev=None
      n.next=None
      self.length-=1
    return n

dl=DoublyLinkedList()


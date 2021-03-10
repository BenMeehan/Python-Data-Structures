class Node:
    def __init__(self,val,priority):
        self.val=val
        self.priority=priority

class PriorityQueue: #Using Min Heap
    def __init__(self):
        self.values=[]
    
    def Enqueue(self,val,priority):
        n=Node(val,priority)
        self.values.append(n)
        
        index=len(self.values)-1
        
        while True:
            parentidx=int((index-1)/2)
            parent=self.values[parentidx]
            if n.priority>=parent.priority:
                break
            
            self.values[parentidx]=n
            self.values[index]=parent
            index=parentidx
            
    def Dequeue(self):
        Maxi=self.values[0]
        end=self.values.pop()
        if len(self.values)>0:
            self.values[0]=end
            self.sinkdown()
        return Maxi
        
    def sinkdown(self):
        idx=0;
        element=self.values[idx]
        length=len(self.values)-1
        
        while True:
            left_idx=2*idx+1
            right_idx=2*idx+2
            
            swap=None 
            if left_idx<length:
                if self.values[left_idx].priority<element.priority:
                    swap=left_idx
            
            if right_idx<length:
                if((self.values[right_idx].priority>element.priority and swap==None) or (self.values[right_idx].priority>self.values[left_idx].priority and swap!=None)):
                    swap=right_idx
                    
            if swap==None:
                break
            else:
                self.values[idx]=self.values[swap]
                self.values[swap]=element
                idx=swap
h=PriorityQueue()
h.Enqueue(10,2)
h.Enqueue(1,1)
h.Enqueue(7,5)
h.Enqueue(4,0)
h.Enqueue(12,1)
# h.Dequeue()
for i in h.values:
    print(i.val)
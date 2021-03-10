class MaxHeap:
    def __init__(self):
        self.values=[]
    
    def insert(self,val):
        self.values.append(val)
        
        index=len(self.values)-1
        
        while True:
            parentidx=int((index-1)/2)
            parent=self.values[parentidx]
            if val<=parent:
                break
            
            self.values[parentidx]=val
            self.values[index]=parent
            index=parentidx
            
    def extractMax(self):
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
                if self.values[left_idx]>element:
                    swap=left_idx
            
            if right_idx<length:
                if((self.values[right_idx]>element and swap==None) or (self.values[right_idx]>self.values[left_idx] and swap!=None)):
                    swap=right_idx
                    
            if swap==None:
                break
            else:
                self.values[idx]=self.values[swap]
                self.values[swap]=element
                idx=swap
h=MaxHeap()
h.insert(10)
h.insert(1)
h.insert(7)
h.insert(4)
h.insert(12)
h.extractMax()
print(h.values)
class Node:
    def __init__(self,val):
        self.val=val
        self.left=None 
        self.right=None 

class BinarySearchTree:
    def __init__(self):
        self.root=None
        
    def insert(self,val):
        n=Node(val)
        if self.root==None:
            self.root=n
            return self
        else:
            temp=self.root
            while(True):
                if(val<temp.val):
                    if(temp.left==None):
                        temp.left=n 
                        return self
                    else:
                        temp=temp.left
                elif(val>temp.val):
                    if(temp.right==None):
                        temp.right=n 
                        return self
                    else:
                        temp=temp.right
                else:
                    return self
    def search(self,val):
        if(self.root and self.root.val==val):
            return True
        else:
            temp=self.root
            while True:
                if temp.val==val:
                    return True
                elif temp.val>val:
                    if temp.left!=None:
                        temp=temp.left
                    else:
                        return False
                elif temp.val<val:
                    if temp.right!=None:
                        temp=temp.right
                    else:
                        return False


def bfs(b):
    queue=[]
    visited=[]
    queue.append(b.root)
    
    while(len(queue)>0):
        visited.append(queue[0])
        if(queue[0].left!=None):
            queue.append(queue[0].left)
        if(queue[0].right!=None):
            queue.append(queue[0].right)
        
        queue.pop(0)
    
    for i in visited:
        print(i.val,end=" ")
    

b=BinarySearchTree()
b.insert(10)
b.insert(8)
b.insert(100)
b.insert(160)
b.insert(1)
b.insert(12)

bfs(b)

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

b=BinarySearchTree()
b.insert(10)
b.insert(90)
b.insert(7)
b.insert(7)
b.insert(1)
b.insert(9)
b.insert(67)
b.insert(70)

print(b.search(67))

print(b.root.right.val)
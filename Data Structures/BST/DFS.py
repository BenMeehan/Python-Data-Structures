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

def depth_first_search_preorder(b):
    visited=[]
    def traverse(node):
        visited.append(node.val)
        if(node.left):
            traverse(node.left)
        if(node.right):
            traverse(node.right)
    traverse(b.root)
    print(visited)
    
def depth_first_search_postorder(b):
    visited=[]
    def traverse(node):
        if(node.left):
            traverse(node.left)
        if(node.right):
            traverse(node.right)
        visited.append(node.val)
    traverse(b.root)
    print(visited)

def depth_first_search_inorder(b):
    visited=[]
    def traverse(node):
        if(node.left):
            traverse(node.left)
        visited.append(node.val)
        if(node.right):
            traverse(node.right)
    traverse(b.root)
    print(visited)

b=BinarySearchTree()
b.insert(10)
b.insert(2)
b.insert(5)
b.insert(1)
b.insert(12)
b.insert(18)

depth_first_search_preorder(b)
depth_first_search_postorder(b)
depth_first_search_inorder(b)

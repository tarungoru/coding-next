class Node:
    def __init__(self,val):
        self.left=None
        self.right=None
        self.val=val
def printlevel(root):
    s1=[root]
    flag=True
    s2=[]
    res=0
    while s1 or s2:
        sum=0
        while s1:
            root=s1.pop(0)
            sum+=root.val
            if root.left:
                s2.append(root.left)
            if root.right:
                s2.append(root.right)
            res=max(res,sum)
            
        print()
        sum=0
        while s2:
            root=s2.pop(0)
            sum+=root.val
            if root.left:
                s1.append(root.left)
            if root.right:
                s1.append(root.right)
            res=max(res,sum)
        
    return res
        
        
root=Node(1)
root.left=Node(2)
root.right=Node(30)
root.left.left=Node(4)
root.left.right=Node(5)
root.right.left=Node(6)
root.right.right=Node(7)
print(printlevel(root))

"general solution for good nodes recursive"

Input: root = [3,1,4,3,null,1,5]
Output: 4
  
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def goodNodes(root):
    temp=root.val
    def helper(root,temp):
        if root==None:
            return 0
        res=1 if root.val>=temp else 0
        temp=max(temp,root.val)
        res+=helper(root.left,temp)+helper(root.right,temp)
        return res
    return helper(root,temp)
root=Node(3)
root.left=Node(1)
root.right=Node(4)
root.left.left=Node(3)
root.right.right=Node(5)
root.right.left=Node(1)
print(goodNodes(root))


"iterative approach solution"


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def goodNodes(root):
    stack=[(root,float("-inf"))]
    res=0
    while stack:
        root,maxval=stack.pop()
        if root.val>=maxval:
            res+=1
        maxval=max(root.val,maxval)
        if root.left:
            stack.append((root.left,maxval))
        if root.right:
            stack.append((root.right,maxval))
    return res
    
root=Node(3)
root.left=Node(1)
root.right=Node(4)
root.left.left=Node(3)
root.right.right=Node(5)
root.right.left=Node(1)
print(goodNodes(root))



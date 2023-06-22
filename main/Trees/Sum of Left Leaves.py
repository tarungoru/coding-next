# using recursion

Input: root = [3,9,20,null,null,15,7]
Output: 24


class Node:
    def __init__(self,val):
        self.left=None
        self.right=None
        self.val=val
def sumof(root):
    def helper(node,lef):
            if not node:
                return 0
            if not node.left and not node.right and lef:
                return node.val
            l=helper(node.left,True)
            r=helper(node.right,False)
            return l+r
    return helper(root,False)
        

    
    
root=Node(1)
root.left=Node(2)
root.left.left=Node(3)
root.right=Node(4)
root.right.left=Node(5)
root.right.right=Node(5)
sumof(root)

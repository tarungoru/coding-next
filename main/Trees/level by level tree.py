# normal method using iteration

class Node:
    def __init__(self,val):
        self.left=None
        self.right=None
        self.val=val
def printlevel(root):
    s1=[root]
    flag=True
    s2=[]
    while s1 or s2:
        while s1:
            root=s1.pop(0)
            print(root.val,end=' ')
            if root.left:
                s2.append(root.left)
            if root.right:
                s2.append(root.right)
        print()
        while s2:
            root=s2.pop(0)
            print(root.val,end=' ')
            if root.left:
                s1.append(root.left)
            if root.right:
                s1.append(root.right)
        print()
        
        
root=Node('a')
root.left=Node('b')
root.right=Node('c')
root.left.left=Node('d')
root.left.right=Node('e')
root.right.left=Node('f')
root.right.right=Node('g')
printlevel(root)


#using the recursion method

class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None
 
def printlevelorder(root):
    h = height(root)
    for i in range(1, h + 1):
        printGivenLevel(root, i)
        print()
def printGivenLevel(root, level):
    if root is None:
        return root
 
    if level == 1:
        print(root.data, end=' ')
    elif level > 1:
        printGivenLevel(root.left, level - 1)
        printGivenLevel(root.right, level - 1)
def height(node):
    if node is None:
        return 0
    else:
        # Compute the height of each subtree
        lheight = height(node.left)
        rheight = height(node.right)
 
        # Use the larger one
        if lheight > rheight:
            return lheight+1
        else:
            return rheight+1
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
printlevelorder(root)
